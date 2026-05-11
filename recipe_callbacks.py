from dash import Dash, Input, Output, State, no_update, ctx
from auto_callbacks import get_component_id, get_convert_index
from dash.exceptions import PreventUpdate
# recipe_manager から recipe_handler と 共通関数をインポート
from recipe_manager import recipe_handler, generate_recipe_display_values
from recipe_edit1_layout import (
    recipe_name_data as reci1_name,
    step_data as reci1_step_data,
    textbox_data as reci1_textbox_data,
    reci1_textbox_indicators,
)
from recipe_edit2_layout import (
    step_data as reci2_step_data,
    textbox_data as reci2_textbox_data,
    reci2_textbox_indicators,
)
from recipe_edit3_layout import (
    step_data as reci3_step_data,
    textbox_data as reci3_textbox_data,
    reci3_textbox_indicators,
)
from recipe_edit4_layout import (
    step_data as reci4_step_data,
    textbox_data as reci4_textbox_data,
    reci4_textbox_indicators,
)
from recipe_manager_layout import(
    sig_list as recipe_manager_sig_list
)

# PLC通信ハンドラ
from tcp_client import tcp_client_handler

# C#通信用
from constans import DeviceEnum, DEVICE_DATA_EXTENDED, BASE_STYLES_MAP
from data_queue import data_queue_handler

from error_log import error_log_handler
# 画面管理用
from page_manager import page_handler

from dash import no_update

# レシピデータとアドレスをPLC送信形式に変換するヘルパー関数
def _prepare_recipe_data_for_plc():    
    # 現在編集中のレシピの全データを取得
    recipe_num = recipe_handler.edit_recipe_num
    # self.recipe_data に直接アクセス
    full_recipe_data = recipe_handler.recipe_data[recipe_num]['data'] 
    # layout1のリストのアドレスを参照する
    all_step_data = reci1_step_data + reci2_step_data + reci3_step_data + reci4_step_data

    # 事前に書き込み前通知を送る
    dev = {"sw_address": 3610}
    tcp_client_handler.write_device_bit(dev)
    
    # 3. 全ステップの全パラメータを処理
    for i,step_dict in enumerate(full_recipe_data):
        # step_dictの値をリストとして取得 (キーの順序が step_param_layout の順序と一致していることが前提)
        step_param_layout = step_dict               # ステップデータのアドレスを取得
        step_values = list(step_dict.values())

        # 1ステップのアドレスと値のリスト
        addresses = []
        values = []
        
        for param_index, _ in enumerate(step_param_layout):
            # アドレスを受け取る
            item = all_step_data[i][param_index]
            plc_address = item['address']
            dev_format = item['input_format']
            
            # 対応する値を取得
            if param_index < len(step_values):
                # PLCに送信する値は整数型 (Word) を想定
                try:
                    if dev_format == 'REAL':
                        value = float(step_values[param_index])
                    else:
                        # 'INT' 'UINT'
                        value = int(step_values[param_index])
                except ValueError:
                    # 値が数値でない場合はスキップまたはエラー処理
                    continue 

                addresses.append(plc_address)
                values.append(value)
            
        print(f'ステップ{i+1}のレシピデータの送信をリクエストしました')
        error_log_handler.print_log("INFO", f'ステップ{i+1}のレシピデータの送信をリクエストしました')
        # ステップごとにリストを送信する
        tcp_client_handler.write_Rdevice_word_bulk(addresses, values, i+1)

    return

def updata_textbox_children(textbox_children_indicators):
    # D5000のデータ取得と安全チェック
    D5000_list, offset5 = data_queue_handler.safe_plc_data_access(DeviceEnum.MIX_D5000, len(textbox_children_indicators))
    # D6000のデータ取得と安全チェック
    D6000_list, offset6 = data_queue_handler.safe_plc_data_access(DeviceEnum.REAL_D6000, len(textbox_children_indicators))

    # どちらか一方でも no_update が返された場合（データリストではなく no_update のリストが返される）
    # D5000_list の最初の要素が no_update なら、未準備と判断できる
    if D5000_list and D5000_list[0] == no_update:
        return D5000_list 
    
    # D6000_list の最初の要素が no_update なら、未準備と判断できる
    if D6000_list and D6000_list[0] == no_update:
        return D6000_list 
    
    updated_values = []
    max_offset = 10000   # アドレスの最大値を想定

    # PLCデータを使うロジック
    for data in textbox_children_indicators:
        address = data['address']
        format_specifier = data['format']

        address_index = 0
        device_value = 0
        value_str = ''

        try:
            if (address >= offset5) and (address < offset6):
                # D5000～
                address_index = get_convert_index(data, DeviceEnum.MIX_D5000.value)
                device_value = D5000_list[address_index]
            elif (address >= offset6) and (address < max_offset):
                # D6000～
                address_index = get_convert_index(data, DeviceEnum.REAL_D6000.value)
                device_value = D6000_list[address_index]

            # FormatSpecifierからPLC用の書式文字列を取得して使用
            format_str = format_specifier.value
            value_str = f'{device_value:{format_str}}'
        except IndexError as e:
            # 範囲外エラーが発生した場合
            value_str = 'ERR'
            error_log_handler.print_log("WARNING", f"警告: データアクセスエラー (アドレス: {address}, エラー: {e})")
        updated_values.append(value_str)
    return updated_values

# センサー、またIO信号の「Lime」「Red」の色を変更します。(M600～番地に対応。X0～にも対応)
def update_sensor_style3400(draw_list):
    # ユーティリティ関数で安全にデータ取得
    M3400_list, offset = data_queue_handler.safe_plc_data_access(
        DeviceEnum.BITS_M3400, 
        len(draw_list)
    )
    
    # データが未準備の場合（deviceがNoneの場合）は no_update のリストをそのまま返す
    if offset is None:
        return M3400_list # [no_update, no_update, ...] のリスト

    new_styles = []
    plc_value = False

    for item in draw_list:
        original_address = item['address']
        address = original_address - offset
       
        # M3400～ のデバイス
        try:
            reverse = item.get('reverse', False)
            plc_value = M3400_list[address] ^ reverse
        except IndexError:
            # リストが空ではないが、インデックスがオーバーした場合（データ定義ミスなどの場合）
            print(f'警告: M600_list の長さ {len(M3400_list)} に対して、要求アドレス {original_address} (-{offset})が範囲外です。')
            plc_value = False # 安全策として False (OFF) に設定

        # 1. レイアウト生成時と同じように、ベーススタイルと座標から完全なスタイルを再構成
        base_style = BASE_STYLES_MAP[item['style_type']].copy()
        base_style['left'] = item['left']
        base_style['top'] = item['top']
                    
        # 3. 状態に応じて色を上書き（元の座標などの情報は維持される）
        if plc_value:
            base_style['backgroundColor'] = 'lime'
            base_style['boxShadow'] = 'none' #'0 0 5px lime' 
        else:
            base_style['backgroundColor'] = 'gray'
            base_style['boxShadow'] = 'none' #'0 0 5px lime'
            
        new_styles.append(base_style)
        
    return new_styles

def register_recipe_callback(app: Dash):
    
    # レシピ名の表示を更新するコールバック
    @app.callback(
        Output('recipe_name1', 'children'), # recipe_edit1_layout.pyで定義されているID
        Input('recipe-mode-store', 'data')  # モード変更時（＝画面遷移時）にトリガー
    )
    def update_recipe_name(data):
        # レシピ名を取得
        recipe_name = recipe_handler.get_recipe_name()
        
        return recipe_name
    
    # --------------------------------------------------------
    # モニター値の更新
    # --------------------------------------------------------
    @app.callback(
        [Output(item['id'], 'children') for item in reci1_textbox_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_reci1_textbox_children(n_intervals):
        if not page_handler.is_recipe_current(1):
             raise PreventUpdate
        
        return updata_textbox_children(reci1_textbox_indicators)
    
    @app.callback(
        [Output(item['id'], 'children') for item in reci2_textbox_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_reci2_textbox_children(n_intervals):
        if not page_handler.is_recipe_current(2):
             raise PreventUpdate
        
        return updata_textbox_children(reci2_textbox_indicators)
    
    @app.callback(
        [Output(item['id'], 'children') for item in reci3_textbox_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_reci3_textbox_children(n_intervals):
        if not page_handler.is_recipe_current(3):
             raise PreventUpdate
        
        return updata_textbox_children(reci3_textbox_indicators)
    
    @app.callback(
        [Output(item['id'], 'children') for item in reci4_textbox_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_reci4_textbox_children(n_intervals):
        if not page_handler.is_recipe_current(4):
             raise PreventUpdate
        
        return updata_textbox_children(reci4_textbox_indicators)
    
    # すべてのステップコンポーネントのIDをリストアップ
    # 例: ['reci_num1_1_step', 'reci_num1_2_step', ..., 'reci_num6_34_step', ...]
    output1_ids = []
    for step_item_list in reci1_step_data: # step_data はリストのリスト
        for item in step_item_list:
            output1_ids.append(Output(item['id'], 'children'))

    @app.callback(
        output=output1_ids,
        inputs=Input('dummy-button-reci1', 'children'), # ダミーOutputがトリガー
        prevent_initial_call=True
    )
    def update_recipe1_steps(dummy_trigger):
        if not dummy_trigger:
            raise PreventUpdate

        # 最新のレシピデータを取得
        csv_recipe_data = recipe_handler.get_recipe_data()
        
        # 【共通関数を呼び出し、更新する値のリストを生成】
        updated_children = generate_recipe_display_values(
            csv_recipe_data, 
            reci1_step_data, 
            reci1_textbox_data
        )

        return updated_children
    
    output2_ids = []
    for step_item_list in reci2_step_data: # step_data はリストのリスト
        for item in step_item_list:
            output2_ids.append(Output(item['id'], 'children'))

    @app.callback(
        output=output2_ids,
        inputs=Input('dummy-button-reci2', 'children'), # ダミーOutputがトリガー
        prevent_initial_call=True
    )
    def update_recipe2_steps(dummy_trigger):
        if not dummy_trigger:
            raise PreventUpdate

        # 最新のレシピデータを取得
        csv_recipe_data = recipe_handler.get_recipe_data()
        
        # 【共通関数を呼び出し、更新する値のリストを生成】
        updated_children = generate_recipe_display_values(
            csv_recipe_data, 
            reci2_step_data, 
            reci2_textbox_data
        )

        return updated_children
    
    output3_ids = []
    for step_item_list in reci3_step_data: # step_data はリストのリスト
        for item in step_item_list:
            output3_ids.append(Output(item['id'], 'children'))

    @app.callback(
        output=output3_ids,
        inputs=Input('dummy-button-reci3', 'children'), # ダミーOutputがトリガー
        prevent_initial_call=True
    )
    def update_recipe3_steps(dummy_trigger):
        if not dummy_trigger:
            raise PreventUpdate

        # 最新のレシピデータを取得
        csv_recipe_data = recipe_handler.get_recipe_data()
        
        # 【共通関数を呼び出し、更新する値のリストを生成】
        updated_children = generate_recipe_display_values(
            csv_recipe_data, 
            reci3_step_data, 
            reci3_textbox_data
        )

        return updated_children
    
    output4_ids = []
    for step_item_list in reci4_step_data: # step_data はリストのリスト
        for item in step_item_list:
            output4_ids.append(Output(item['id'], 'children'))

    @app.callback(
        output=output4_ids,
        inputs=Input('dummy-button-reci4', 'children'), # ダミーOutputがトリガー
        prevent_initial_call=True
    )
    def update_recipe4_steps(dummy_trigger):
        if not dummy_trigger:
            raise PreventUpdate

        # 最新のレシピデータを取得
        csv_recipe_data = recipe_handler.get_recipe_data()
        
        # 【共通関数を呼び出し、更新する値のリストを生成】
        updated_children = generate_recipe_display_values(
            csv_recipe_data, 
            reci4_step_data, 
            reci4_textbox_data
        )

        return updated_children
    
    # レシピデータをPLCに送信するコールバック
    @app.callback(
        # 何も更新しないダミーOutput、または画面遷移後のURL
        output=Output('dummy-div-for-plc-write', 'children'), # レイアウトにダミーDivを追加してください
        inputs=[
            Input('recipe-to-plc-button', 'n_clicks'), # ユーザーがレイアウトに追加するボタンID
        ],
        prevent_initial_call=True
    )
    def recipe_to_plc(n_clicks):
        if not n_clicks or n_clicks == 0:
            raise PreventUpdate
        
        _prepare_recipe_data_for_plc()
            
        print("レシピデータの送信リクエストが完了しました...")
            
        return no_update # 画面上のコンポーネントは更新しない
    
    # レシピデータを保存するコールバック
    @app.callback(
        # 何も更新しないダミーOutput、または画面遷移後のURL
        output=Output('dummy-div-for-plc-write', 'children', allow_duplicate=True), # ダミーDivのidが重複するので、「allow_duplicate=True」を追加する
        inputs=[
            Input('recipe-save-button', 'n_clicks'), # ユーザーがレイアウトに追加するボタンID
        ],
        prevent_initial_call=True
    )
    def recipe_save(n_clicks):
        if not n_clicks or n_clicks == 0:
            raise PreventUpdate
        
        # 【変更箇所: PLC送信の代わりにファイル保存を呼び出す】
        # 将来的に動的なファイルパス管理が実装されるまで、初期化時のパスを使用
        file_path_to_save = recipe_handler.get_recipe_file()
        
        recipe_handler.save_current_recipe_to_file(file_path_to_save)
            
        print(f"レシピデータのファイル保存リクエストが完了しました。保存先: {file_path_to_save}")
            
        return no_update # 画面上のコンポーネントは更新しない
    
    # レシピの編集＆切替をするコールバック
    @app.callback(
        Output('recipe-sel-store', 'data'),
        Input('file-tree', 'selected'),
        State('recipe-sel-store', 'data'),
        prevent_initial_call=True
    )
    def change_selected_recipe(selected_values, data):
    # 状態の更新
        data['selected_values'] = selected_values
        return data
    
    # DUMMY_OUTPUT_ID = 'dummy-button-reci1'
    # @app.callback(
    #     Output(DUMMY_OUTPUT_ID, 'children'),
    #     Input('recipe-edit-button', 'n_clicks'),
    #     State('recipe-sel-store', 'data'),
    #     prevent_initial_call=True
    # )
    @app.callback(
        Output(reci1_name, 'children'),
        Input('recipe-edit-button', 'n_clicks'),
        State('recipe-sel-store', 'data'),
        prevent_initial_call=True
    )
    def update_selected_recipe(n_clicks, data):
        if not n_clicks or n_clicks == 0:
            raise PreventUpdate

        selected_values = data.get('selected_values')

        if not selected_values:
            # レシピが選択されていない場合は何もしない
            print("レシピが選択されていません。")
            raise PreventUpdate

        # 1. 選択されたレシピのファイル名（value）を取得
        # dmc.Treeはリストを返すため、最初の要素を取得
        selected_value = selected_values[0] 
        
        # 2. valueからレシピ番号を抽出
        # 例: 'reci_sel_file1' -> 1
        # ※ `recipe_manager_layout.py` で 'reci_sel_file{number}' の形式で設定されている前提
        try:
            recipe_num_str = selected_value.replace('reci_sel_file', '')
            # レシピ番号は1から始まるため、インデックスは (番号 - 1)
            # ただし、`recipe_handler`の初期化ではレシピ0がデバッグ用のため、
            # ファイルから読み込むレシピはインデックス1からとなり、`recipe_num`をそのまま使うのが適切かもしれません
            # ここではファイル名をキーとして設定リストからインデックスを探索する、より安全な方法を検討
            
            # 簡易的な実装: ファイル番号をそのままレシピ番号として使用 (0番はデバッグ用と仮定)
            new_recipe_num = int(recipe_num_str) 
            
        except ValueError:
            print(f"レシピ選択値の解析エラー: {selected_value}")
            raise PreventUpdate

        # 3. recipe_handler の更新 (編集対象のレシピを切り替え)
        if recipe_handler.edit_recipe_num != new_recipe_num:
            recipe_handler.edit_recipe_num = new_recipe_num
            print(f"編集対象のレシピを Recipe_{new_recipe_num} に切り替えました。")
            
            # オフセットも初期化
            # recipe_handler.update_edit_step_offset(0)

            # 4. 新しいレシピデータを読み込む（`get_recipe_data` の呼び出しをトリガーする）
            # ダミーの値を返すことで、recipe_callbacks.pyの `update_recipe1_steps` などをトリガーします
            # ここでは単なる時間ベースの文字列を返し、強制的に更新させる
            import datetime
            return str(datetime.datetime.now())
        else:
            # 選択中のレシピと同じ場合は更新しない
            raise PreventUpdate
        
    # 信号（style）を更新
    @app.callback(
        [Output(item['id'], 'style') for item in recipe_manager_sig_list],
        Input('interval-component', 'n_intervals'),
    )
    def update_chamber_style(n_intervals):
        if not page_handler.is_recipe_mode():
             raise PreventUpdate
        
        new_styles = []     # コールバック用のstyleリスト、または空のリスト
        new_styles = update_sensor_style3400(recipe_manager_sig_list)

        return new_styles