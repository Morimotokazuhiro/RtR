from dash import Input, Output, no_update
from dash.exceptions import PreventUpdate

from auto_callbacks import get_convert_index

from setting1_layout import (
    setting_data as set1textbox_children_indicators
)
from setting2_layout import (
    setting_data as set2textbox_children_indicators
)
from setting3_layout import (
    setting_data as set3textbox_children_indicators
)
from error_log import error_log_handler
# C#通信用
from constans import DeviceEnum, FormatSpecifier
from data_queue import data_queue_handler
# 画面管理用
from page_manager import page_handler

def updata_textbox_children(textbox_children_indicators):
    # D4000のデータ取得と安全チェック
    D4000_list, offset = data_queue_handler.safe_plc_data_access(DeviceEnum.MIX_D4000, len(textbox_children_indicators))

    # どちらか一方でも no_update が返された場合（データリストではなく no_update のリストが返される）
    # D4000_list の最初の要素が no_update なら、未準備と判断できる
    if D4000_list and D4000_list[0] == no_update:
        return D4000_list
    
    updated_values = []
    max_offset = 10000   # アドレスの最大値を想定

    # PLCデータを使うロジック
    for data in textbox_children_indicators:
        address = data['address']
        format_specifier = data['format']
        gain = data.get('gain', 1)

        address_index = 0
        device_value = 0.0
        value_str = ''

        try:
            # D4000～
            address_index = get_convert_index(data, DeviceEnum.MIX_D4000.value)
            device_value = float(D4000_list[address_index]) / float(gain)

            # FormatSpecifierからPLC用の書式文字列を取得して使用
            format_str = format_specifier.value
            if format_specifier == FormatSpecifier.D:
                value = int(device_value)
            else:
                value = device_value
            value_str = f'{value:{format_str}}'
        except IndexError as e:
            # 範囲外エラーが発生した場合
            value_str = 'ERR'
            error_log_handler.print_log("WARNING", f"警告: データアクセスエラー (アドレス: {address}, エラー: {e})")
        updated_values.append(value_str)
    return updated_values

# コールバックを登録する関数
def register_setting_callbacks(app):
    # --------------------------------------------------------
    # モニター値の更新
    # --------------------------------------------------------
    @app.callback(
        [Output(item['id'], 'children') for item in set1textbox_children_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_set1_textbox_children(n_intervals):
        if not page_handler.is_setting_current(1):
            raise PreventUpdate
        
        return updata_textbox_children(set1textbox_children_indicators)
    
    @app.callback(
        [Output(item['id'], 'children') for item in set2textbox_children_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_set2_textbox_children(n_intervals):
        if not page_handler.is_setting_current(2):
            raise PreventUpdate
        
        return updata_textbox_children(set2textbox_children_indicators)
    
    @app.callback(
        [Output(item['id'], 'children') for item in set3textbox_children_indicators],
        Input('interval-component', 'n_intervals'),
    )
    def update_set3_textbox_children(n_intervals):
        if not page_handler.is_setting_current(3):
            raise PreventUpdate
        
        return updata_textbox_children(set3textbox_children_indicators)