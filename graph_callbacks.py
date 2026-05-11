from dash import Input, Output, no_update, ctx
from dash.exceptions import PreventUpdate
from constans import DeviceEnum, DEVICE_DATA_EXTENDED
from constans_graph import GRAPH_DATA_LIST
from data_queue import data_queue_handler
from auto_graph_layout import AutoGraphLayout
# 画面管理用
from page_manager import page_handler

trend_graph1_handler = AutoGraphLayout(max_points=150, title="グラフ1", series_names=['データ'])
trend_graph2_handler = AutoGraphLayout(max_points=150, title="グラフ2", series_names=['データ'])
trend_graph3_handler = AutoGraphLayout(max_points=150, title="グラフ3", series_names=['データ'])

# ドロップダウン変更時にデータをリセットする
def check_and_reset(handler, selector_id):
    if ctx.triggered_id == selector_id:
        handler.data_queues = [[] for _ in handler.series_names]

# コールバックを登録する関数
def register_graph_callbacks(app):
    # アドレスから名称を取得するヘルパー関数
    name_map = {item['address']: item['name'] for item in GRAPH_DATA_LIST}

    @app.callback(
        Output('graph-graph1', 'figure'),
        Input('interval-component', 'n_intervals'),
        Input('graph-selector-1', 'value'),
    )
    def update_trend_graph1(n_intervals, selected_address):
        if not page_handler.is_graph_mode():
            raise PreventUpdate
        
        # リセット処理
        check_and_reset(trend_graph1_handler, 'graph-selector-1')

        device_name = DEVICE_DATA_EXTENDED[DeviceEnum.REAL_D6000.value]['device']
        trend_data_list = data_queue_handler.get_device_data(device_name)
        
        if trend_data_list and selected_address:
            # 選択されたアドレスからインデックスを動的に計算
            index = (selected_address - 6000) // 2
            new_data_point = trend_data_list[index]
            
            # タイトルと系列名を更新（AutoGraphLayoutの仕様に合わせて調整してください）
            label = name_map.get(selected_address, "不明")
            trend_graph1_handler.title = label
            trend_graph1_handler.series_names = [label]
            
            return trend_graph1_handler.update_and_create_figure([new_data_point])
            
        return no_update
    
    @app.callback(
        Output('graph-graph2', 'figure'),
        Input('interval-component', 'n_intervals'),
        Input('graph-selector-2', 'value'), # ドロップダウンをInputに追加
    )
    def update_trend_graph2(n_intervals, selected_address):
        if not page_handler.is_graph_mode():
            raise PreventUpdate
        
        # リセット処理
        check_and_reset(trend_graph2_handler, 'graph-selector-2')

        device_name = DEVICE_DATA_EXTENDED[DeviceEnum.REAL_D6000.value]['device']
        trend_data_list = data_queue_handler.get_device_data(device_name)
        
        if trend_data_list and selected_address:
            index = (selected_address - 6000) // 2
            new_data_point = trend_data_list[index]
            
            label = name_map.get(selected_address, "不明")
            trend_graph2_handler.title = label
            trend_graph2_handler.series_names = [label]
            
            return trend_graph2_handler.update_and_create_figure([new_data_point])
            
        return no_update
    
    @app.callback(
        Output('graph-graph3', 'figure'),
        Input('interval-component', 'n_intervals'),
        Input('graph-selector-3', 'value'), # ドロップダウンをInputに追加
    )
    def update_trend_graph3(n_intervals, selected_address):
        if not page_handler.is_graph_mode():
            raise PreventUpdate
        
        # リセット処理
        check_and_reset(trend_graph3_handler, 'graph-selector-3')

        device_name = DEVICE_DATA_EXTENDED[DeviceEnum.REAL_D6000.value]['device']
        trend_data_list = data_queue_handler.get_device_data(device_name)
        
        if trend_data_list and selected_address:
            index = (selected_address - 6000) // 2
            new_data_point = trend_data_list[index]
            
            label = name_map.get(selected_address, "不明")
            trend_graph3_handler.title = label
            trend_graph3_handler.series_names = [label]
            
            return trend_graph3_handler.update_and_create_figure([new_data_point])
            
        return no_update