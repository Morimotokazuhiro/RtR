import dash
from dash import dcc, html, ctx
from dash.exceptions import PreventUpdate

from dash.dependencies import Input, Output
import random
from dash import no_update # no_updateを明示的にインポート
# C#通信用
from tcp_client import tcp_client_handler

# 必要なデータをインポート
from auto_chamber_layout import (
    chamber_src_indicators, 
    chamber_ids_children, 
    chamber_style_indicators,
    chamber_monitor_indicators
)
from auto_pipe_layout import(
    monitor_data as pipe_src_indicators,
    sensor_list as pipe_sensor_list
) 
from auto_water_layout import (
    water_style_indicators
)
from auto_recipe_layout import(
    recipe_handler, recipe_data_ids
)
from auto_alarm_layout import (
    autobutton_src_indicators, 
    lamp_button_data as auto_lamp_button_data
)
from auto_graph_layout import AutoGraphLayout
# PLC通信用
# from pipe_connect import DeviceEnum, plc_handler, DEVICE_DATA_EXTENDED
# C#通信用
from constans import DeviceEnum, DEVICE_DATA_EXTENDED, BASE_STYLES_MAP
from constans_graph import GRAPH_DATA_LIST
from data_queue import data_queue_handler
from auto_graph_layout import AutoGraphLayout
# 異常監視用
from alarm_monitoring import alm_handler
# 操作ログ用
from act_log_task import act_log_handler
# 画面管理用
from page_manager import page_handler

from dash import no_update
import datetime

DEBUG_MODE = False  # テスト中は True、本番リリース時は False に手動で変更

# オート画面用のグラフハンドラ
auto_graph_handler = AutoGraphLayout(max_points=150, title="グラフ", series_names=['データ'])

def check_and_reset(handler, selector_id):
    if ctx.triggered_id == selector_id:
        handler.data_queues = [[] for _ in handler.series_names]

# ボタンの画像を変える
# これは個別にアドレスを取得します。連続アドレスの取得はmanualのコールバックを参照してください
def update_button_image_src(image_list):
    # これは簡易版です
    updated_values = []
    
    for item in image_list:
        address = item['address']
        plc_value = False
        
        plc_value = data_queue_handler.get_bit_device(address)

        if plc_value ^ item['reverse']: # ^演算子：XOR、つまりreverseがONのときは信号が反転する
            updated_values.append('/assets/images/PlasticSquare_SB.png') # ONの青ボタン点灯
        else:
            updated_values.append('/assets/images/PlasticSquare_G.png')  # ONのグレー消灯

    return updated_values

# センサー、またIO信号の「Lime」「Red」の色を変更します。(M600～番地に対応。X0～にも対応)
def update_sensor_style(draw_list):
    # ユーティリティ関数で安全にデータ取得
    M600_list, offset = data_queue_handler.safe_plc_data_access(
        DeviceEnum.BITS_M600, 
        len(draw_list)
    )
    # ユーティリティ関数で安全にデータ取得
    X0_list, offsetX = data_queue_handler.safe_plc_data_access(
        DeviceEnum.BITS_X0, 
        len(draw_list)
    )
    
    # データが未準備の場合（deviceがNoneの場合）は no_update のリストをそのまま返す
    if offset is None:
        return M600_list # [no_update, no_update, ...] のリスト

    new_styles = []
    plc_value = False

    for item in draw_list:
        original_address = item['address']
        address = original_address - offset

        if original_address < offset:
            # X0～ のデバイス
            try:
                reverse = item.get('reverse', False)
                plc_value = X0_list[original_address] ^ reverse
            except IndexError:
                # リストが空ではないが、インデックスがオーバーした場合（データ定義ミスなどの場合）
                print(f'警告: X0_list の長さ {len(X0_list)} に対して、要求アドレス {original_address} が範囲外です。')
                plc_value = False # 安全策として False (OFF) に設定
        else:
            # M600～ のデバイス
            try:
                reverse = item.get('reverse', False)
                plc_value = M600_list[address] ^ reverse
            except IndexError:
                # リストが空ではないが、インデックスがオーバーした場合（データ定義ミスなどの場合）
                print(f'警告: M600_list の長さ {len(M600_list)} に対して、要求アドレス {original_address} (-{offset})が範囲外です。')
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
            base_style['backgroundColor'] = 'red'
            base_style['boxShadow'] = 'none' #'0 0 5px lime'
            
        new_styles.append(base_style)
        
    return new_styles

def update_valve_image_src(image_list):
    # ★ 修正: ユーティリティ関数で安全にデータ取得
        M600_list, offset = data_queue_handler.safe_plc_data_access(
            DeviceEnum.BITS_M600, 
            len(image_list)
        )
        # データが未準備の場合（deviceがNoneの場合）は no_update のリストをそのまま返す
        if offset is None:
            return M600_list # [no_update, no_update, ...] のリスト

        updated_values = []
        plc_value = False
        
        for item in image_list:
            address = item['address'] - offset
            plc_value = False
            
            try:
                plc_value = M600_list[address] 
            except IndexError:
                plc_value = False

            if item['muki']: # 縦向き
                if plc_value:
                    updated_values.append('/assets/images/valve_on_tate.png')
                else:
                    updated_values.append('/assets/images/valve_off_tate.png') 
            else:
                if plc_value:
                    updated_values.append('/assets/images/valve_on.png')
                else:
                    updated_values.append('/assets/images/valve_off.png') 

        return updated_values

# コールバックされたコンポーネントのIDを取得
def get_component_id(ctx):
    """
    コールバックされたコンポーネントのIDを取得する。
    Args:
        ctx: dash.callback_context オブジェクト。
    Returns:
        トリガーとなったコンポーネントのID (文字列)。
    """
    ctx = dash.callback_context
    if not ctx.triggered:
        return no_update # トリガーがない場合は更新しない
    else:
        return ctx.triggered[0]['prop_id'].split('.')[0]

# 参照先のアドレスを変換してインデックスを返す
def get_convert_index(data, device_enum_index):
    # 入力の引数は、各デバイス情報の辞書
    address = data['address']
    # 通信データの辞書
    device_info = DEVICE_DATA_EXTENDED[device_enum_index]
    offset = device_info['offset']
    device_type = device_info['data_type']

    if device_type == 'MIX':
        data_index = data.get('data_index')

        if device_type is None:
            print(f"警告: 「data_index」がありません。(アドレス: {address})")
            return 0
        
        else:
            # Mixは個別に記述されたインデックスを返す
            return data_index
        
    offset_address = address - offset

    if offset_address < 0:
        print(f"警告: 「address」の割り当てが間違っています。(アドレス: {address}, オフセット： {offset})")
        return 0

    if (device_type == 'REAL') or (device_type == 'DINT'):
        # ダブルワードはアドレスを半分にして返す
        return offset_address // 2
    else:
        # 1ワードとビット型はそのまま返す
        return offset_address

def get_plc_D5000D6000_datas(datas, read_size):
    # 入力datasのaddressから、PLCデータを取得します。フォーマットを適用し、リストを返します。
    updated_values = []

    # D5000のデータ取得と安全チェック
    D5000_list, offset5 = data_queue_handler.safe_plc_data_access(DeviceEnum.MIX_D5000, len(chamber_ids_children))
    # D6000のデータ取得と安全チェック
    D6000_list, offset6 = data_queue_handler.safe_plc_data_access(DeviceEnum.REAL_D6000, len(chamber_ids_children))

    # どちらか一方でも no_update が返された場合（データリストではなく no_update のリストが返される）
    # D5000_list の最初の要素が no_update なら、未準備と判断できる
    if D5000_list and D5000_list[0] == no_update:
        # 準備が出来ていない場合は、エラーが出ないように「no_update」（更新しない）をread_sizeの数だけ返す。
        return [no_update] * read_size
    
    # D6000_list の最初の要素が no_update なら、未準備と判断できる
    if D6000_list and D6000_list[0] == no_update:
        # 準備が出来ていない場合は、エラーが出ないように「no_update」（更新しない）をread_sizeの数だけ返す。
        return [no_update] * read_size
    
    max_offset = 10000   # アドレスの最大値を想定

    # PLCデータを使うロジック
    for i in range(read_size):
        data = datas[i]
        address = data['address']
        format_specifier = data.get('format')
        format_str = ''

        address_index = 0
        device_value = 0
        value_str = ''

        try:
            if address == 0:
                # レシピ等でアドレスが設定されていないとき
                device_value = 0
            elif (address >= offset5) and (address < offset6):
                # D5000～
                address_index = get_convert_index(data, DeviceEnum.MIX_D5000.value)
                # if address_index is None:
                #     print(f"(アドレスインデックス: {address}, {i}, {address_index})")
                device_value = D5000_list[address_index]
            elif (address >= offset6) and (address < max_offset):
                # D6000～
                address_index = get_convert_index(data, DeviceEnum.REAL_D6000.value)
                device_value = D6000_list[address_index]

            # 個別にフォントを設定するなら、ここでformat_strを作る
            if format_specifier is None:
                format_str = '.1f'
            else:
                format_str = format_specifier.value
            value_str = f'{device_value:{format_str}}'

            # デバッグ用
            # if address_index == 0:
            #     print(f"value: id:{address_index}, value {device_value})")
                
        except IndexError as e:
            # 範囲外エラーが発生した場合
            value_str = 'ERR'
            print(f"警告: データアクセスエラー (アドレス: {address}, エラー: {e})")

        updated_values.append(value_str)
    return updated_values

# コールバックを登録するための関数
def register_auto_callbacks(app):
    # 冷却水モニター値を更新するコールバック関数
    @app.callback(
        [Output(item['id'], 'style') for item in water_style_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_water_style(n_intervals):
        if not page_handler.is_auto_mode():
             raise PreventUpdate
        
        new_styles = []     # コールバック用のstyleリスト、または空のリスト
        new_styles = update_sensor_style(water_style_indicators)
        
        return new_styles
    
    name_map = {item['address']: item['name'] for item in GRAPH_DATA_LIST}

    @app.callback(
        Output('auto-graph', 'figure'),
        Input('interval-component', 'n_intervals'),
        Input('auto-graph-selector', 'value'),  # ドロップダウンを追加
    )
    def update_auto_graph(n_intervals, selected_address):
        # グラフ画面用ID（例: 'auto'）に合わせて判定
        if not page_handler.is_auto_mode():
             raise PreventUpdate

        # リセット処理
        check_and_reset(auto_graph_handler, 'auto-graph-selector')

        device_name = DEVICE_DATA_EXTENDED[DeviceEnum.REAL_D6000.value]['device']
        trend_data_list = data_queue_handler.get_device_data(device_name)
        
        if trend_data_list and selected_address:
            index = (selected_address - 6000) // 2
            new_data_point = trend_data_list[index]
            
            label = name_map.get(selected_address, "不明")
            auto_graph_handler.title = label
            auto_graph_handler.series_names = [label]
            
            return auto_graph_handler.update_and_create_figure([new_data_point])
            
        return no_update
        
    # レシピのコールバック関数
    @app.callback(
        [Output(id, 'children') for id in recipe_data_ids],
        Input('interval-component', 'n_intervals'),
        Input('recipe_switch1', 'n_clicks'),
        Input('recipe_switch2', 'n_clicks'),
    )
    def update_recipe_data(n_intervals, n1, n2):
        if not page_handler.is_auto_mode():
             raise PreventUpdate
        
        countup = 0
        com_id = get_component_id(dash.callback_context)

        if com_id == 'recipe_switch1':
            countup = -1
            # 💡 インスタンスに対してメソッドを呼び出す（ self は自動で渡される）
            recipe_handler.update_view_step(countup)
        elif com_id == 'recipe_switch2':
            countup = 1
            recipe_handler.update_view_step(countup)
        
        recipe_handler.update_parameter()
        # リセットが必要な場合は
        # recipe_handler.reset_status()

        # Out用のリスト（recipe_data_idsの順番に従うこと）
        updated_values = []
        # レシピ番号
        updated_values.append(recipe_handler.recipe_name)
        # 実行表示バー
        style = recipe_handler.get_bar_style()
        updated_values.append(html.Div(style={'height': '100%', 'width': '100%', **style}))
        # ステップ番号
        updated_values.append(recipe_handler.get_step_number())

        size = recipe_handler.device_size
        # 機器名 (仮)
        for i in range(size):
            devace_name = recipe_handler.device_datas[i]['text']
            updated_values.append(f'{devace_name}')

        # 現在値
        current_plc_datas = get_plc_D5000D6000_datas(recipe_handler.current_datas, size)
        updated_values.extend(current_plc_datas)
        # 設定値
        setting_plc_datas = get_plc_D5000D6000_datas(recipe_handler.setting_datas, size)
        updated_values.extend(setting_plc_datas)
        
        return updated_values

    #
    # バルブモニターに関するコールバック関数
    #
    # 画像（src）を更新
    @app.callback(
        [Output(item['id'], 'src') for item in pipe_src_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_pipe_monitor(n_intervals):
        if not page_handler.is_auto_mode():
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_valve_image_src(pipe_src_indicators)

        return updated_values
    # 信号（style）を更新
    @app.callback(
        [Output(item['id'], 'style') for item in pipe_sensor_list],
        Input('interval-component', 'n_intervals'),
    )
    def update_pipe_style(n_intervals):
        if not page_handler.is_auto_mode():
             raise PreventUpdate
        
        new_styles = []     # コールバック用のstyleリスト、または空のリスト
        new_styles = update_sensor_style(pipe_sensor_list)
        
        return new_styles
    
    #
    # チャンバーに関するコールバック関数
    #
    # 画像（src）を更新
    @app.callback(
        [Output(item['id'], 'src') for item in chamber_src_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_chamber_src(n_intervals):
        if not page_handler.is_auto_mode():
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_valve_image_src(chamber_src_indicators)

        return updated_values
    # 信号（style）を更新
    @app.callback(
        [Output(item['id'], 'style') for item in chamber_style_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_chamber_style(n_intervals):
        if not page_handler.is_auto_mode():
             raise PreventUpdate
        
        new_styles = []     # コールバック用のstyleリスト、または空のリスト
        new_styles = update_sensor_style(chamber_style_indicators)
        
        return new_styles
    # 数値表示（children）を更新
    @app.callback(
        [Output(item['id'], 'children') for item in chamber_monitor_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_chamber_monitor(n_intervals):
        if not page_handler.is_auto_mode():
             raise PreventUpdate
               
        # D5000のデータ取得と安全チェック
        D5000_list, offset5 = data_queue_handler.safe_plc_data_access(DeviceEnum.MIX_D5000, len(chamber_monitor_indicators))
        # D6000のデータ取得と安全チェック
        D6000_list, offset6 = data_queue_handler.safe_plc_data_access(DeviceEnum.REAL_D6000, len(chamber_monitor_indicators))

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
        for data in chamber_monitor_indicators:
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
                if format_specifier == 'date':
                    # 時間の場合はfloat型（秒）から変換する
                    value = int(device_value)
                    time_delta = datetime.timedelta(seconds=value)
                    # オブジェクトを文字列に変換
                    value_str = str(time_delta)
                else:
                    format_str = format_specifier.value
                    value_str = f'{device_value:{format_str}}'

            except IndexError as e:
                # 範囲外エラーが発生した場合
                value_str = 'ERR'
                print(f"警告: データアクセスエラー (アドレス: {address}, エラー: {e})")
            updated_values.append(value_str)
        return updated_values
    
    #
    # アラームリストのコールバック関数
    #
    @app.callback(
        Output('auto-alarm-table', 'data'),
        Input('interval-component', 'n_intervals'),
        prevent_initial_call=True 
    )
    def update_alarm_table(n_intervals):
        if not page_handler.is_auto_mode():
             raise PreventUpdate
        
        return alm_handler.Check_Alarm()
    
    @app.callback(
        [Output(item['img_id'], 'src') for item in auto_lamp_button_data],
        Input('interval-component', 'n_intervals'),
    )
    def update_alarm_button_src(n_intervals):
        if not page_handler.is_auto_mode():
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_button_image_src(auto_lamp_button_data)

        return updated_values
    
    @app.callback(
        Output('dummy-button-autoreset', 'children'), 
        [Input(item['id'], 'n_clicks') for item in autobutton_src_indicators],
        prevent_initial_call=True # 初期実行を防止
    )
    def click_autoreset_button(*n_clicks_list):
        if not page_handler.is_auto_mode():
             raise PreventUpdate
        
        # 1. クリックされたボタンを特定
        button_id = get_component_id(ctx)
        #if not ctx.triggered:
        if button_id == no_update:
            return no_update
        
        # IDに対応するボタンデータを operation3_src_indicators から検索
        clicked_button_data = next(
            (item for item in autobutton_src_indicators if item['id'] == button_id),
            None
        )

        if clicked_button_data is None:
            return no_update # データが見つからない場合は何もしない

        # 3. PLCに書き込み
        print(f"操作ボタンクリック: {clicked_button_data['sw_address']} に を書き込みます。")
        act_log_handler.logging_trigger(f"ボタンクリック: id_{clicked_button_data['id']}/address_{clicked_button_data['sw_address']}")
        # plc_handlerは mx_connect.py で定義されているグローバルインスタンス
        tcp_client_handler.write_device_bit(clicked_button_data)
        
        # 4. 処理完了: Output (ダミーコンポーネント) は更新しない
        return no_update
    