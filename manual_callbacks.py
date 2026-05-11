from dash import Input, Output, no_update, ctx
from dash.exceptions import PreventUpdate

from auto_callbacks import get_component_id, get_convert_index, update_sensor_style, update_valve_image_src
from manual_diagram1_layout import (
    diagram1_valve_indicators,
    diagram1_ids_children,
    diagram1_style_indicators,
    monitor_list as dg1_monitor_data
)
from manual_diagram2_layout import (
    diagram2_ids_children,
    mode_list as diagram2_mode_style_indicators,
    monitor_list as dg2_monitor_data,
    BASE_20px_CIRCLE
)
from manual_diagram3_layout import (
    diagram3_valve_indicators,
    diagram3_ids_children,
    monitor_list as dg3_monitor_data,
    sensor_list as dg3_sensor_list,
)
from manual_operation1_layout import (
    ope1button_src_indicators,
    log_button_data as ope1button_log,
    ope1_buttons,
    ope1lamp_src_indicators,
    setting_data as ope1textbox_children_indicators
)

from manual_operation2_layout import (
    lp_button_data as ope2button_src_indicators,
    ope2button_click_indicators,
    ope2textbox_children_indicators,
    lamp_data as ope2lamp_src_indicators
)
from manual_operation3_layout import (
    lp_button_data as ope3button_src_indicators,
    setting_data as ope3textbox_children_indicators
)
from manual_operation4_layout import (
    button_data as ope4button_src_indicators,
    lamp_data as ope4lamp_src_indicators
)
from manual_operation5_layout import (
    ope5textbox_children_indicators
)
from manual_alarm_layout import (
    mnabutton_src_indicators,
    auto_button_data as autobutton_src_indicators,
    lamp_data as mnalamp_src_indicators,
)
from error_log import error_log_handler
# 操作ログ用
from act_log_task import act_log_handler
# C#通信用
from constans import DeviceEnum
from tcp_client import tcp_client_handler
from data_queue import data_queue_handler
# 異常監視用
from alarm_monitoring import alm_handler
# 画面管理用
from page_manager import page_handler

import datetime

# ボタンの画像を変える
def update_button_image_src(image_list):
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

            if item['type'] == 'ON':
                if plc_value ^ item['reverse']: # ^演算子：XOR、つまりreverseがONのときは信号が反転する
                    updated_values.append('/assets/images/PlasticSquare_SB.png') # ONの青ボタン点灯
                else:
                    updated_values.append('/assets/images/PlasticSquare_G.png')  # ONのグレー消灯
            elif item['type'] == 'OFF':
                if plc_value ^ item['reverse']:
                    updated_values.append('/assets/images/PlasticSquare_R.png') # OFFの赤ボタン点灯
                else:
                    updated_values.append('/assets/images/PlasticSquare_G.png')  # OFFのグレー消灯
            # 特別なボタン
            elif item['type'] == 'SVM2_CL':
                if plc_value:
                    updated_values.append('/assets/images/PlasticSquare_R.png')
                else:
                    updated_values.append('/assets/images/PlasticSquare_G.png')
            elif item['type'] == 'AUTO_bt':
                if plc_value:
                    updated_values.append('/assets/images/PlasticSquare_Y.png')
                else:
                    updated_values.append('/assets/images/PlasticSquare_G.png')

        return updated_values

def update3400_button_image_src(image_list):
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

# モード設定の「Lime」の色を変更します。
def update_mode_style(draw_list):
    # ユーティリティ関数で安全にデータ取得
    M600_list, offset = data_queue_handler.safe_plc_data_access(
        DeviceEnum.BITS_M600, 
        len(draw_list)
    )
    
    # データが未準備の場合（deviceがNoneの場合）は no_update のリストをそのまま返す
    if offset is None:
        return M600_list # [no_update, no_update, ...] のリスト

    new_styles = []
    plc_value = False

    for item in draw_list:
        address_index = get_convert_index(item, DeviceEnum.BITS_M600.value)
        # 取得したリストの長さチェックと try-except で安全性を高める
        try:
            reverse = item.get('reverse', False)
            plc_value = M600_list[address_index] ^ reverse
        except IndexError:
            # リストが空ではないが、インデックスがオーバーした場合（データ定義ミスなどの場合）
            error_log_handler.print_log("WARNING", f'警告: D5000_list の長さ {len(M600_list)} に対して、インデックス {address_index} が参照されました。')
            plc_value = False # 安全策として False (OFF) に設定

        # 1. レイアウト生成時と同じように、ベーススタイルと座標から完全なスタイルを再構成
        base_style = BASE_20px_CIRCLE.copy()
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

# ランプの画像を変える
def update_lamp_image_src(image_list):
    # ★ 修正: ユーティリティ関数で安全にデータ取得
        M3400_list, offset = data_queue_handler.safe_plc_data_access(
            DeviceEnum.BITS_M3400, 
            len(image_list)
        )
        # データが未準備の場合（deviceがNoneの場合）は no_update のリストをそのまま返す
        if offset is None:
            return M3400_list # [no_update, no_update, ...] のリスト

        updated_values = []
        plc_value = False
        
        for item in image_list:
            address = item['address'] - offset
            plc_value = False
            
            try:
                plc_value = M3400_list[address] 
            except IndexError:
                plc_value = False

            if plc_value:
                updated_values.append('/assets/images/RealCircle2_G.png') # 緑ランプ点灯
            else:
                updated_values.append('/assets/images/RealCircle2_R.png') # 赤ランプ点灯

        return updated_values

def updata_textbox_children(textbox_children_indicators):
    # D4000のデータ取得と安全チェック
    D4000_list, offset4 = data_queue_handler.safe_plc_data_access(DeviceEnum.MIX_D4000, len(textbox_children_indicators))
    # D6000のデータ取得と安全チェック
    D6000_list, offset6 = data_queue_handler.safe_plc_data_access(DeviceEnum.REAL_D6000, len(textbox_children_indicators))

    # どちらか一方でも no_update が返された場合（データリストではなく no_update のリストが返される）
    # D4000_list の最初の要素が no_update なら、未準備と判断できる
    if D4000_list and D4000_list[0] == no_update:
        return D4000_list 
    
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
            if (address >= offset4) and (address < offset6):
                # D4000～
                address_index = get_convert_index(data, DeviceEnum.MIX_D4000.value)
                device_value = D4000_list[address_index]
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



def register_manual_callbacks(app):
    # バルブ画像（src）を更新
    @app.callback(
        [Output(item['id'], 'src') for item in diagram1_valve_indicators],
        Input('interval-component', 'n_intervals'), 
    )
    def update_dg1_src(n_intervals):
        if not page_handler.is_manual_diagram(1):
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_valve_image_src(diagram1_valve_indicators)

        return updated_values
    
    @app.callback(
        [Output(item['id'], 'src') for item in diagram3_valve_indicators],
        Input('interval-component', 'n_intervals'),  
    )
    def update_dg3_src(n_intervals):
        if not page_handler.is_manual_diagram(3):
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_valve_image_src(diagram3_valve_indicators)

        return updated_values
    
    # 信号（style）を更新
    @app.callback(
        [Output(item['id'], 'style') for item in diagram1_style_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_dg1_style(n_intervals):
        if not page_handler.is_manual_diagram(1):
             raise PreventUpdate
        
        new_styles = []     # コールバック用のstyleリスト、または空のリスト
        new_styles = update_sensor_style(diagram1_style_indicators)
        
        return new_styles
    
    @app.callback(
        [Output(item['id'], 'style') for item in diagram2_mode_style_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_dg2_mode_style(n_intervals):
        if not page_handler.is_manual_diagram(2):
             raise PreventUpdate
        
        new_styles = []     # コールバック用のstyleリスト、または空のリスト
        new_styles = update_mode_style(diagram2_mode_style_indicators)
        
        return new_styles    
    
    @app.callback(
        [Output(item['id'], 'style') for item in dg3_sensor_list],
        Input('interval-component', 'n_intervals'),
    )
    def update_dg3_style(n_intervals):
        if not page_handler.is_manual_diagram(3):
             raise PreventUpdate
        
        new_styles = []     # コールバック用のstyleリスト、または空のリスト
        new_styles = update_sensor_style(dg3_sensor_list)
        
        return new_styles
    
    # インターロックランプ (画像) の更新
    @app.callback(
        [Output(item['img_id'], 'src') for item in mnalamp_src_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_mna_lamp_src(n_intervals):
        if not page_handler.is_manual_mode():
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_lamp_image_src(mnalamp_src_indicators)

        return updated_values
    
    @app.callback(
        [Output(item['img_id'], 'src') for item in ope1lamp_src_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_ope1_lamp_src(n_intervals):
        if not page_handler.is_manual_operation(1):
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_lamp_image_src(ope1lamp_src_indicators)

        return updated_values
    
    @app.callback(
        [Output(item['img_id'], 'src') for item in ope2lamp_src_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_ope2_lamp_src(n_intervals):
        if not page_handler.is_manual_operation(2):
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_lamp_image_src(ope2lamp_src_indicators)

        return updated_values
    
    @app.callback(
        [Output(item['img_id'], 'src') for item in ope4lamp_src_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_ope4_lamp_src(n_intervals):
        if not page_handler.is_manual_operation(4):
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_lamp_image_src(ope4lamp_src_indicators)

        return updated_values
    
    # ボタン画像（src）の更新
    @app.callback(
        [Output(item['img_id'], 'src') for item in autobutton_src_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_mna_button_src(n_intervals):
        if not page_handler.is_manual_mode():
             raise PreventUpdate
        #print("update_mna_button_src")
        updated_values = []
        updated_values = update_button_image_src(autobutton_src_indicators)

        return updated_values
    @app.callback(
        Output(ope1button_log[0]['img_id'], 'src'),
        Input('interval-component', 'n_intervals'),
    )
    def update_ope1_log_button_src(n_intervals):
        if not page_handler.is_manual_operation(1):
             raise PreventUpdate
        
        updated_values = update3400_button_image_src(ope1button_log)
        return updated_values[0] if updated_values else no_update
    
    @app.callback(
        [Output(item['img_id'], 'src') for item in ope1button_src_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_ope1_button_src(n_intervals):
        if not page_handler.is_manual_operation(1):
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_button_image_src(ope1button_src_indicators)

        return updated_values    
    
    @app.callback(
        [Output(item['img_id'], 'src') for item in ope2button_src_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_ope2_button_src(n_intervals):
        if not page_handler.is_manual_operation(2):
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_button_image_src(ope2button_src_indicators)

        return updated_values
    
    @app.callback(
        [Output(item['img_id'], 'src') for item in ope3button_src_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_ope3_button_src(n_intervals):
        if not page_handler.is_manual_operation(3):
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_button_image_src(ope3button_src_indicators)

        return updated_values
    
    @app.callback(
        [Output(item['img_id'], 'src') for item in ope4button_src_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_ope4_button_src(n_intervals):
        if not page_handler.is_manual_operation(4):
             raise PreventUpdate
        
        updated_values = []
        updated_values = update_button_image_src(ope4button_src_indicators)

        return updated_values
    
    # 入力テキストボックスの更新
    @app.callback(
        [Output(item['id'], 'children') for item in ope1textbox_children_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_ope1_textbox_children(n_intervals):
        if not page_handler.is_manual_operation(1):
             raise PreventUpdate
        return updata_textbox_children(ope1textbox_children_indicators)
    
    @app.callback(
        [Output(item['id'], 'children') for item in ope2textbox_children_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_ope2_textbox_children(n_intervals):
        if not page_handler.is_manual_operation(2):
            raise PreventUpdate        
        return updata_textbox_children(ope2textbox_children_indicators)
    
    @app.callback(
        [Output(item['id'], 'children') for item in ope3textbox_children_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_ope3_textbox_children(n_intervals):
        if not page_handler.is_manual_operation(3):
            raise PreventUpdate
        return updata_textbox_children(ope3textbox_children_indicators)
    
    @app.callback(
        # ope5textbox_children_indicators に含まれるすべての html.Div の 'children' を出力
        [Output(item['id'], 'children') for item in ope5textbox_children_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_ope5_textbox_children(n_intervals):
        if not page_handler.is_manual_operation(5):
            raise PreventUpdate
        return updata_textbox_children(ope5textbox_children_indicators)
    
    # 模式図モニター値を更新
    @app.callback(
        [Output(id, 'children') for id in diagram1_ids_children],
        Input('interval-component', 'n_intervals'),
    )
    def update_dg1_monitor(n_intervals):
        if not page_handler.is_manual_diagram(1):
             raise PreventUpdate
        
        # D4000のデータ取得と安全チェック
        D4000_list, offset4 = data_queue_handler.safe_plc_data_access(DeviceEnum.MIX_D4000, len(diagram1_ids_children))
        # D6000のデータ取得と安全チェック
        D6000_list, offset6 = data_queue_handler.safe_plc_data_access(DeviceEnum.REAL_D6000, len(diagram1_ids_children))

        # どちらか一方でも no_update が返された場合（データリストではなく no_update のリストが返される）
        # D4000_list の最初の要素が no_update なら、未準備と判断できる
        if D4000_list and D4000_list[0] == no_update:
            return D4000_list 
        
        # D6000_list の最初の要素が no_update なら、未準備と判断できる
        if D6000_list and D6000_list[0] == no_update:
            return D6000_list 
        
        updated_values = []
        max_offset = 10000   # アドレスの最大値を想定

        # PLCデータを使うロジック
        for data in dg1_monitor_data:
            address = data['address']
            format_specifier = data['format']

            address_index = 0
            device_value = 0
            value_str = ''

            try:
                if (address >= offset4) and (address < offset6):
                    # D4000～
                    address_index = get_convert_index(data, DeviceEnum.MIX_D4000.value)
                    device_value = D4000_list[address_index]
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
                error_log_handler.print_log("WARNING", f"警告: データアクセスエラー (アドレス: {address}, エラー: {e})")
            updated_values.append(value_str)
        return updated_values
    
    @app.callback(
        [Output(id, 'children') for id in diagram2_ids_children],
        Input('interval-component', 'n_intervals'),
    )
    def update_dg2_monitor(n_intervals):
        if not page_handler.is_manual_diagram(2):
             raise PreventUpdate
        
        # D4000のデータ取得と安全チェック
        D4000_list, offset4 = data_queue_handler.safe_plc_data_access(DeviceEnum.MIX_D4000, len(diagram2_ids_children))
        # D6000のデータ取得と安全チェック
        D6000_list, offset6 = data_queue_handler.safe_plc_data_access(DeviceEnum.REAL_D6000, len(diagram2_ids_children))

        # どちらか一方でも no_update が返された場合（データリストではなく no_update のリストが返される）
        # D4000_list の最初の要素が no_update なら、未準備と判断できる
        if D4000_list and D4000_list[0] == no_update:
            return D4000_list 
        
        # D6000_list の最初の要素が no_update なら、未準備と判断できる
        if D6000_list and D6000_list[0] == no_update:
            return D6000_list 
        
        updated_values = []
        max_offset = 10000   # アドレスの最大値を想定

        # PLCデータを使うロジック
        for data in dg2_monitor_data:
            address = data['address']
            format_specifier = data['format']

            address_index = 0
            device_value = 0
            value_str = ''

            try:
                if (address >= offset4) and (address < offset6):
                    # D4000～
                    address_index = get_convert_index(data, DeviceEnum.MIX_D4000.value)
                    device_value = D4000_list[address_index]
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
    
    @app.callback(
        [Output(id, 'children') for id in diagram3_ids_children],
        Input('interval-component', 'n_intervals'),
    )
    def update_dg3_monitor(n_intervals):
        if not page_handler.is_manual_diagram(3):
             raise PreventUpdate

        # D6000のデータ取得と安全チェック
        D6000_list, offset6 = data_queue_handler.safe_plc_data_access(DeviceEnum.REAL_D6000, len(dg3_monitor_data))
        
        # D6000_list の最初の要素が no_update なら、未準備と判断できる
        if D6000_list and D6000_list[0] == no_update:
            return D6000_list 
        
        updated_values = []

        # PLCデータを使うロジック
        for data in dg3_monitor_data:
            address = data['address']
            format_specifier = data['format']

            address_index = 0
            device_value = 0
            value_str = ''

            try:
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
    #
    # ボタン押下トリガー
    #
    @app.callback(
        Output('dummy-button-op1', 'children'), 
        [Input(item['id'], 'n_clicks') for item in ope1_buttons],
        prevent_initial_call=True # 初期実行を防止
    )
    def click_ope1_button(*n_clicks_list):
        if not page_handler.is_manual_operation(1):
             raise PreventUpdate
        
        # 1. クリックされたボタンを特定
        button_id = get_component_id(ctx)

        if button_id == no_update:
            return no_update
        
        # IDに対応するボタンデータを operation3_src_indicators から検索
        clicked_button_data = next(
            (item for item in ope1_buttons if item['id'] == button_id),
            None
        )

        if clicked_button_data is None:
            return no_update # データが見つからない場合は何もしない

        # 3. PLCに書き込み
        print(f"操作ボタンクリック: {clicked_button_data['sw_address']} に を書き込みます。")
        act_log_handler.logging_trigger(f"ボタンクリック: id_{clicked_button_data['id']}/address_{clicked_button_data['sw_address']}")
        # plc_handlerは mx_connect.py で定義されているグローバルインスタンス
        tcp_client_handler.write_device_bit(clicked_button_data)
        
        # 5. 処理完了: Output (ダミーコンポーネント) は更新しない
        return no_update
    
    @app.callback(
        Output('dummy-button-op2', 'children'), 
        [Input(item['id'], 'n_clicks') for item in ope2button_click_indicators],
        prevent_initial_call=True # 初期実行を防止
    )
    def click_ope2_button(*n_clicks_list):
        if not page_handler.is_manual_operation(2):
             raise PreventUpdate
        
        # 1. クリックされたボタンを特定
        button_id = get_component_id(ctx)
        #if not ctx.triggered:
        if button_id == no_update:
            return no_update
        
        # IDに対応するボタンデータを operation3_src_indicators から検索
        clicked_button_data = next(
            (item for item in ope2button_click_indicators if item['id'] == button_id),
            None
        )

        if clicked_button_data is None:
            return no_update # データが見つからない場合は何もしない

        # 3. PLCに書き込み
        print(f"操作ボタンクリック: {clicked_button_data['sw_address']} に を書き込みます。")
        act_log_handler.logging_trigger(f"ボタンクリック: id_{clicked_button_data['id']}/address_{clicked_button_data['sw_address']}")
        # plc_handlerは mx_connect.py で定義されているグローバルインスタンス
        tcp_client_handler.write_device_bit(clicked_button_data)
        
        # 5. 処理完了: Output (ダミーコンポーネント) は更新しない
        return no_update
    
    @app.callback(
        # OutputにダミーID 'dummy_button-op3' を指定し、childrenを no_update で返す
        Output('dummy-button-op3', 'children'), 
        [Input(item['id'], 'n_clicks') for item in ope3button_src_indicators],
        prevent_initial_call=True # 初期実行を防止
    )
    def click_ope3_button(*n_clicks_list):
        if not page_handler.is_manual_operation(3):
             raise PreventUpdate
        
        # 1. クリックされたボタンを特定
        button_id = get_component_id(ctx)
        #if not ctx.triggered:
        if button_id == no_update:
            return no_update
        
        # IDに対応するボタンデータを operation3_src_indicators から検索
        clicked_button_data = next(
            (item for item in ope3button_src_indicators if item['id'] == button_id),
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
    
    @app.callback(
        # OutputにダミーID 'dummy_button-op4' を指定し、childrenを no_update で返す
        Output('dummy-button-op4', 'children'), 
        [Input(item['id'], 'n_clicks') for item in ope4button_src_indicators],
        prevent_initial_call=True # 初期実行を防止
    )
    def click_ope4_button(*n_clicks_list):
        if not page_handler.is_manual_operation(4):
             raise PreventUpdate
        
        # 1. クリックされたボタンを特定
        button_id = get_component_id(ctx)
        #if not ctx.triggered:
        if button_id == no_update:
            return no_update
        
        # IDに対応するボタンデータを operation3_src_indicators から検索
        clicked_button_data = next(
            (item for item in ope4button_src_indicators if item['id'] == button_id),
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
    
    @app.callback(
        # OutputにダミーID 'dummy_button-op4' を指定し、childrenを no_update で返す
        Output('dummy-button-manualreset', 'children'), 
        [Input(item['id'], 'n_clicks') for item in mnabutton_src_indicators],
        prevent_initial_call=True # 初期実行を防止
    )
    def click_manualreset_button(*n_clicks_list):
        if not page_handler.is_manual_mode():
             raise PreventUpdate
        
        # 1. クリックされたボタンを特定
        button_id = get_component_id(ctx)
        #if not ctx.triggered:
        if button_id == no_update:
            return no_update
        
        # IDに対応するボタンデータを operation3_src_indicators から検索
        clicked_button_data = next(
            (item for item in mnabutton_src_indicators if item['id'] == button_id),
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
    
    #
    # アラームリストのコールバック関数
    #
    @app.callback(
        Output('alarm-table', 'data'),
        Input('interval-component', 'n_intervals'),
        prevent_initial_call=True 
    )
    def update_alarm_table(n_intervals):
        if not page_handler.is_manual_mode():
            raise PreventUpdate
        
        return alm_handler.Check_Alarm()
    


    