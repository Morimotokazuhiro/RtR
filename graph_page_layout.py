from dash import html, dcc
from constans_graph import GRAPH_DATA_LIST

def create_graph_layout():
    # ドロップダウン用の選択肢を作成
    options = [{'label': item['name'], 'value': item['address']} for item in GRAPH_DATA_LIST]

    graph_layout = html.Div(className='graph-container', style={'position': 'relative'}, children=[
        # グラフ1用のコントロール
        html.Div([
            dcc.Dropdown(
                id='graph-selector-1',
                options=options,
                value=6004,  # デフォルト値: RF伝送出力
                clearable=False,
                style={'width': '300px', 'marginBottom': '10px'}
            ),
            dcc.Graph(id='graph-graph1', style={'width': '100%', 'height': '400px'}),
        ], className='graph-content-item'),

        # グラフ2用のコントロール
        html.Div([
            dcc.Dropdown(
                id='graph-selector-2',
                options=options,
                value=6006,  # デフォルト値: RF反射出力
                clearable=False,
                style={'width': '300px', 'marginBottom': '10px'}
            ),
            dcc.Graph(id='graph-graph2', style={'width': '100%', 'height': '400px'}),
        ], className='graph-content-item'),

        # html.Div(
        #     #'グラフ3',
        #     className='graph-content-item',
        #     children=[
        #         dcc.Graph(
        #             id='graph-graph3',
        #             style={'width': '100%', 'height': '100%'}
        #         ),
        #     ]),

        # グラフ3用のコントロール
        html.Div([
            dcc.Dropdown(
                id='graph-selector-3',
                options=options,
                value=6000,  # デフォルト値: チャンバー内圧
                clearable=False,
                style={'width': '300px', 'marginBottom': '10px'}
            ),
            dcc.Graph(id='graph-graph3', style={'width': '100%', 'height': '400px'}),
        ], className='graph-content-item'),
    ])
    
    return graph_layout