from dash import dcc, html
from constans_graph import GRAPH_DATA_LIST
from auto_pipe_layout import create_pipe_layout
from auto_chamber_layout import create_chamber_layout
from auto_water_layout import create_water_layout
from auto_recipe_layout import create_recipe_layout
from auto_alarm_layout import create_auto_alerm_layout

def create_auto_layout():
    # ドロップダウン用の選択肢を作成
    options = [{'label': item['name'], 'value': item['address']} for item in GRAPH_DATA_LIST]

    layout = html.Div(className='container', children=[
    #layout_template = html.Div(className='container', children=[
        
        # --- グラフとメッセージオーバーレイ ---
        # 💡 修正: CSSの .graph-content を利用し、position: relative で絶対配置の基準とする
        html.Div(className='graph-content', style={'position': 'relative'}, children=[
            
            # グラフ表示領域
            html.Div(className='auto-graph-section', children=[
                html.Div([
                    dcc.Dropdown(
                        id='auto-graph-selector',
                        options=options,
                        value=6002,  # デフォルト値
                        clearable=False,
                        style={'width': '300px', 'marginBottom': '10px'}
                    ),
                    html.Div(id='auto-graph-container', children=[
                        dcc.Graph(id='auto-graph', style={'width': '100%', 'height': '500px'})
                    ])
                ])
            ]),

            # --- メッセージオーバーレイ (グラフの上に重ねる) ---
            # html.Div(
            #     id='status-message-overlay', # 識別用ID (グラフ全体を覆う)
            #     className='message-overlay',
            #     children=[
            #         html.Div(id='status-message-text', children=[
                        
            #             ],
            #             style={ # スタイルは、グラフ領域に位置合わせ
            #                 # 💡 修正: メッセージ装飾（半透明の背景と影）
            #                 'position': 'absolute', 
            #                 'top': '25%',
            #                 'left': '25%',
            #                 'padding': '30px', 
            #                 'borderRadius': '15px', 
            #                 'boxShadow': '0 6px 12px rgba(0,0,0,0.5)', 
            #                 'backgroundColor': 'rgba(255, 255, 255, 0.85)', # 白の半透明背景 (透過度85%)
            #                 'textAlign': 'center',
            #                 'maxWidth': '800px',
            #                 'minWidth': '400px',
            #             } 
            #         )
            #     ],
            #     style={ # このDiv (オーバーレイ) はグラフ領域全体を覆い、子要素を中央に配置する役割
            #         'position': 'relative'
            #     } 
            # ),
        ]), # graph-content 終了


        html.Div(className='middle-section', children=[
            html.Aside(className='left-column', children=[
                html.Div(className='content-item recipe-1', style={'position': 'relative'}, children=[
                    *create_recipe_layout()
                ])
            ]),
            
            html.Div(className='right-column', children=[
                html.Div(className='content-item content-1', style={'position': 'relative'}, children=[
                    *create_chamber_layout()
                ]),
                html.Div(className='content-item content-2', style={'position': 'relative'}, children=[
                    *create_pipe_layout()
                ]),
                html.Div(className='content-item content-3', style={'position': 'relative'}, children=[
                    *create_water_layout()
                ]),
                html.Div(className='content-item content-4', style={'position': 'relative'}, children=[
                    *create_auto_alerm_layout()
                ])
            ])
        ]),

        # 3. ダミーコンポーネント (操作ボタンのOutコールバック用)
        #html.Div(id='dummy_div', children=[], style={'display': 'none'}) ,

        

        html.Footer(children=[
            
        ]),
    ])

    return layout
