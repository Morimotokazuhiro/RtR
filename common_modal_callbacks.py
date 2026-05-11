import time

from dash import Dash, callback, Input, Output, State, no_update, ctx
from dash import html
from dash.exceptions import PreventUpdate
from typing import List, Dict, Any

from common_modal_layout import MODAL_STYLE
from manual_operation1_layout import setting_data as ope1_setting_data
from manual_operation2_layout import setting_data as ope2_setting_data
from manual_operation3_layout import setting_data as ope3_setting_data
from manual_operation5_layout import setting_data as ope5_setting_data
from setting1_layout import setting_data as set1_setting_data
from setting2_layout import setting_data as set2_setting_data
from setting3_layout import setting_data as set3_setting_data
from recipe_edit1_layout import (
    textbox_data as reci1_textbox_data,
    step_data as reci1_step_data
)
from recipe_edit2_layout import (
    textbox_data as reci2_textbox_data,
    step_data as reci2_step_data
)
from recipe_edit3_layout import (
    textbox_data as reci3_textbox_data,
    step_data as reci3_step_data
)
from recipe_edit4_layout import (
    textbox_data as reci4_textbox_data,
    step_data as reci4_step_data
) 
# 通信用
from tcp_client import tcp_client_handler
# レシピ用
from recipe_manager import recipe_handler
# formatの型
from constans import FormatSpecifier
# 操作ログ用
from act_log_task import act_log_handler
# エラーログ用
from error_log import error_log_handler

# 共通ロジック（前回の回答で抽象化したもの）
def display_view_modal(button_id, current_value, setting_datas, setting_ids):
    # ここでは、ope1/ope2に依存しない共通の処理を記述
    try:
        clicked_index = setting_ids.index(button_id)
    except ValueError:
        raise PreventUpdate

    modal_style = MODAL_STYLE.copy()
    modal_style['display'] = 'flex'

    # 選択された設定データの詳細情報を取得
    selected_setting = setting_datas[clicked_index]
    str_format_FS:FormatSpecifier = selected_setting.get('format', FormatSpecifier.D)
    str_format = str_format_FS.value
    
    store_data = {
        'id': button_id, 
        'address': setting_datas[clicked_index]['address'],
        'format': str_format,
        'value': current_value,
        'min_value': selected_setting.get('min_value', None),
        'max_value': selected_setting.get('max_value', None),
        'file': selected_setting.get('file', False),
        'step': selected_setting.get('step', 0),
        'item_id': selected_setting.get('item_id', 0),
        'gain': selected_setting.get('gain', 1),
    }

    act_log_handler.logging_trigger(f"入力ボックス選択: id_{store_data['id']}/address_{store_data['address']}")

    # モーダルに表示する新しい内容
    # 現在値、デバイス名、上限値、下限値を含める
    name = selected_setting.get('name', 'N/A')
    min_val = selected_setting.get('min_value', 'N/A')
    max_val = selected_setting.get('max_value', 'N/A')
    
    # html.Divを使って複数行の表示を作成
    modal_children = []
    modal_children.append(html.Div([
        html.H5(f'{name} の設定', style={'fontWeight': 'bold', 'margin': '0 0 5px 0'}),  # デバイス名
        html.P(f'現在値: {current_value}', style={'margin': '0'}),
        html.P(f'範囲: {min_val} 〜 {max_val}', style={'margin': '0'}),
    ]))
    
    # 戻り値を modal_children に変更
    return modal_style, store_data, modal_children

def create_modal_callback(
    app, 
    setting_datas: List[Dict[str, Any]],
    modal_id_suffix: str # 例: '-op1', '-op2'
):
    """
    指定された設定データとモーダルIDサフィックスに基づいて、
    固有のDashコールバックを生成・登録する。
    """
    setting_ids = [item['id'] for item in setting_datas]
    
    # ----------------------------------------------------------------------
    # クロージャとしてコールバック関数を定義
    # ----------------------------------------------------------------------
    @app.callback(
        Output(f'setting-modal{modal_id_suffix}', 'style'),
        Output(f'modal-data-store{modal_id_suffix}', 'data'),
        Output(f'modal-current-display{modal_id_suffix}', 'children'),
        [Input(id, 'n_clicks') for id in setting_ids],
        [State(id, 'children') for id in setting_ids]
    )
    def display_modal_for_screen(*args):
        #ctx = callback.context
        if not ctx.triggered:
            raise PreventUpdate
        
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        # argsの分割
        num_inputs = len(setting_ids)
        n_clicks_list = args[:num_inputs]
        children_list = args[num_inputs:]

        clicked_index_in_list = setting_ids.index(button_id)
        current_value = children_list[clicked_index_in_list]

        if n_clicks_list[clicked_index_in_list] is not None and n_clicks_list[clicked_index_in_list] > 0:
            # 共通ロジックを呼び出し
            return display_view_modal(
                button_id=button_id,
                current_value=current_value,
                setting_datas=setting_datas, # クロージャがキャプチャした引数
                setting_ids=setting_ids      # クロージャがキャプチャした引数
            )
        
        raise PreventUpdate
    
def create_ok_callback(
    app: Dash, 
    modal_id_suffix: str # 例: '-op1', '-op2'
):
    """
    OKボタンの処理コールバックを生成・登録する。
    """
    modal_id = f'setting-modal{modal_id_suffix}'
    input_id = f'modal-input{modal_id_suffix}'
    store_id = f'modal-data-store{modal_id_suffix}'
    ok_button_id = f'modal-ok-button{modal_id_suffix}'
    dummy_output_id = f'dummy-button{modal_id_suffix}'

    # 2. OKボタンでPLCに値を送信し、モーダルを閉じる
    @app.callback(
        # モーダル本体のスタイルを変更
        Output(modal_id, 'style', allow_duplicate=True),
        # ダミーOutput。allow_duplicate=Trueにするために必要
        Output(dummy_output_id, 'children', allow_duplicate=True), 
        Input(ok_button_id, 'n_clicks'),
        State(input_id, 'value'),
        State(store_id, 'data'), # Storeに保存されたclicked_data全体
        State(modal_id, 'style'),
        prevent_initial_call=True
    )
    def send_textbox_value(n_clicks, input_value_str, store_data, modal_style):
        #ctx = callback.context
        if n_clicks is None or n_clicks == 0:
            raise PreventUpdate # no_update より推奨
        
        act_log_handler.logging_trigger(f"入力ボックスOK: id_{store_data['id']}/address_{store_data['address']}")
            
        str_id = store_data['id']
        gain = store_data['gain']
        print(f"id '{str_id}' が選択されました")
        # 1. 入力値のバリデーション
        try:
            str_format = store_data['format']
            if (str_format == '^d') or (str_format == 'd'):
                input_data = int(input_value_str) * int(gain)                
            else:
                input_data = float(input_value_str) * float(gain)
        except (ValueError, TypeError):
            # 警告ログを出力
            error_log_handler.print_log("WARNING", f"警告: 入力値 '{input_value_str}' は数値として無効です。")
            # モーダルは閉じない
            return no_update, no_update
        
        if store_data['file']:
            # R番地への書き込み

            # 2. PLCに書き込み if文にstore_data.get('item_id')を追加すると「0」のときにはじかれるので、チェックしない
            if store_data:
                item_id = store_data['item_id']
                value = input_data
                
                # PLCに書き込む場合
                # print(f"モーダル入力 (OK): R{address} に {value} を書き込みます。")
                # tcp_client_handler.write_Rdevice_word(address, value) 
                # レシピに書き込む場合
                step = store_data['step']
                recipe_handler.write_recipe_device(step, item_id, value)
            else:
                print("警告: Storeデータに 'item_id' がありません。書き込みをスキップします。")
                return no_update, no_update
            
                # 3. モーダルを非表示にする
            new_style = modal_style.copy()
            new_style['display'] = 'none'

            # 画面更新用に、ダミーOutputに、更新が成功したことを示す値（例: 現在時刻の文字列）を返す
            update_trigger_value = f"Update:{time.time()}" 

            # new_style (モーダルを閉じる), update_trigger_value (ダミーOutputに値を設定)
            return new_style, update_trigger_value
        else:
            # 通常のD番地への書き込み

            # 2. PLCに書き込み
            if store_data and store_data.get('address'):
                address = store_data['address']
                value = input_data
                
                print(f"モーダル入力 (OK): D{address} に {value} を書き込みます。")
                
                # TODO: ここで tcp_client_handler.write_device_word(address, value) を呼び出す
                tcp_client_handler.write_device_word(address, value) 
            else:
                print("警告: Storeデータに 'address' がありません。書き込みをスキップします。")
                return no_update, no_update
            
            # 3. モーダルを非表示にする
            new_style = modal_style.copy()
            new_style['display'] = 'none'

            # new_style (モーダルを閉じる), no_update (ダミーOutput)
            return new_style, no_update
        
def create_cancel_callback(
    app: Dash, 
    modal_id_suffix: str # 例: '-op1', '-op2'
):
    """
    キャンセルボタンの処理コールバックを生成・登録する。
    """
    modal_id = f'setting-modal{modal_id_suffix}'
    cancel_button_id = f'modal-cancel-button{modal_id_suffix}'

    # 3. キャンセルボタンでモーダルを閉じる
    @app.callback(
        Output(modal_id, 'style', allow_duplicate=True),
        Input(cancel_button_id, 'n_clicks'),
        State(modal_id, 'style'),
        prevent_initial_call=True
    )
    def cancel_textbox_input(n_clicks, modal_style):
        #ctx = callback.context #

        if n_clicks is None or n_clicks == 0:
            raise PreventUpdate
            
        # モーダルを非表示にする
        new_style = modal_style.copy()
        new_style['display'] = 'none'

        return new_style

def register_modal_callbacks(app: Dash):
    """
    設定値入力モーダルに関連する共通コールバックをDashアプリに登録します。
    """
    # 1. ope1 用コールバックの登録
    create_modal_callback(
        app,
        setting_datas=ope1_setting_data,
        modal_id_suffix='-op1' # operation1のModal IDに対応
    )

    # 2. ope2 用コールバックの登録
    create_modal_callback(
        app,
        setting_datas=ope2_setting_data,
        modal_id_suffix='-op2' # operation2のModal IDに対応
    )

    # 3. ope3 用コールバックの登録
    create_modal_callback(
        app,
        setting_datas=ope3_setting_data,
        modal_id_suffix='-op3' # operation3のModal IDに対応
    )

    # 4. ope5 用コールバックの登録
    create_modal_callback(
        app,
        setting_datas=ope5_setting_data,
        modal_id_suffix='-op5' # operation5のModal IDに対応
    )
    # 5. set1 用コールバックの登録
    create_modal_callback(
        app,
        setting_datas=set1_setting_data,
        modal_id_suffix='-set1' # setting1のModal IDに対応
    )
    # 6. set2 用コールバックの登録
    create_modal_callback(
        app,
        setting_datas=set2_setting_data,
        modal_id_suffix='-set2' # setting2のModal IDに対応
    )
    create_modal_callback(
        app,
        setting_datas=set3_setting_data,
        modal_id_suffix='-set3' # setting2のModal IDに対応
    )
    # 7. recipe edit 用コールバックの登録
    recipe1_steps = []
    for steps in reci1_step_data:
        recipe1_steps.extend(steps)

    create_modal_callback(
        app,
        setting_datas=reci1_textbox_data + recipe1_steps,
        modal_id_suffix='-reci1' # recipe editのModal IDに対応
    )

    recipe2_steps = []
    for steps in reci2_step_data:
        recipe2_steps.extend(steps)

    create_modal_callback(
        app,
        setting_datas=reci2_textbox_data + recipe2_steps,
        modal_id_suffix='-reci2' # recipe editのModal IDに対応
    )

    recipe3_steps = []
    for steps in reci3_step_data:
        recipe3_steps.extend(steps)

    create_modal_callback(
        app,
        setting_datas=reci3_textbox_data + recipe3_steps,
        modal_id_suffix='-reci3' # recipe editのModal IDに対応
    )

    recipe4_steps = []
    for steps in reci4_step_data:
        recipe4_steps.extend(steps)

    create_modal_callback(
        app,
        setting_datas=reci4_textbox_data + recipe4_steps,
        modal_id_suffix='-reci4' # recipe editのModal IDに対応
    )

    # 1. ope1 の OK/Cancel ボタンコールバック登録
    create_ok_callback(app, modal_id_suffix='-op1')
    create_cancel_callback(app, modal_id_suffix='-op1')

    # 2. ope2 の OK/Cancel ボタンコールバック登録
    create_ok_callback(app, modal_id_suffix='-op2')
    create_cancel_callback(app, modal_id_suffix='-op2')

    # 3. ope3 の OK/Cancel ボタンコールバック登録
    create_ok_callback(app, modal_id_suffix='-op3')
    create_cancel_callback(app, modal_id_suffix='-op3')

    # 4. ope5 の OK/Cancel ボタンコールバック登録
    create_ok_callback(app, modal_id_suffix='-op5')
    create_cancel_callback(app, modal_id_suffix='-op5')

    # 5. set1 の OK/Cancel ボタンコールバック登録
    create_ok_callback(app, modal_id_suffix='-set1')
    create_cancel_callback(app, modal_id_suffix='-set1')

    # 6. set2 の OK/Cancel ボタンコールバック登録
    create_ok_callback(app, modal_id_suffix='-set2')
    create_cancel_callback(app, modal_id_suffix='-set2')

    # 6. set3 の OK/Cancel ボタンコールバック登録
    create_ok_callback(app, modal_id_suffix='-set3')
    create_cancel_callback(app, modal_id_suffix='-set3')

    # 7. reci の OK/Cancel ボタンコールバック登録
    create_ok_callback(app, modal_id_suffix='-reci1')
    create_cancel_callback(app, modal_id_suffix='-reci1')

    create_ok_callback(app, modal_id_suffix='-reci2')
    create_cancel_callback(app, modal_id_suffix='-reci2')

    create_ok_callback(app, modal_id_suffix='-reci3')
    create_cancel_callback(app, modal_id_suffix='-reci3')

    create_ok_callback(app, modal_id_suffix='-reci4')
    create_cancel_callback(app, modal_id_suffix='-reci4')