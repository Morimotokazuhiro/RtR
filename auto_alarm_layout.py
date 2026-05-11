from dash import dash_table
from dash import html

ALARM_COLUMN_DEFS = [
    {'name': '時刻', 'id': 'time'},
    {'name': '重要度', 'id': 'level'},
    {'name': '種類', 'id': 'type'},
    {'name': 'メッセージ', 'id': 'message'},
]
# アラームテーブルの列IDをリストで抽出（style_cell_conditionalなどで利用するため）
ALARM_COLUMN_IDS = [col['id'] for col in ALARM_COLUMN_DEFS]

# 照光ボタン
lamp_button_data = [
    {'id': 'btn-auto-start', 'img_id': 'btn-auto-start_img1', 'left': '780px','top': '170px', 'sw_address': 3100, 'address': 900, 'type':'ON', 'name':'起動', 'reverse': False,
     'src': '/assets/images/PlasticSquare_G.png'},
    #{'id': 'btn-auto-log', 'img_id': 'btn-auto-log_img1', 'left': '780px','top': '260px', 'sw_address': 3600, 'address': 3601, 'type':'ON', 'name':'ロギング', 'reverse': False,
    # 'src': '/assets/images/PlasticSquare_G.png'},
]
# プッシュボタン
push_button_data = [
    {'id': 'btn-auto-reset', 'left': '780px', 'top': '8px', 'sw_address': 502, 'name': 'リセット',
     'src': '/assets/images/PlasticRect_Y.png'},
    {'id': 'btn-auto-bz-stop', 'left': '780px', 'top': '80px', 'sw_address': 503, 'name': 'ブザー停止',
     'src': '/assets/images/PlasticRect_Y.png'},
    {'id': 'btn-auto-stop', 'left': '780px', 'top': '242px', 'sw_address': 3300, 'name': '停止',
     'src': '/assets/images/PlasticRect_R.png'},
]
autobutton_src_indicators = lamp_button_data + push_button_data

def _add_button(layout, button_list):
    font_size = '20px'
    for data in button_list:
        _src = data['src']
        children=[
            # 1. 画像 (背景または状態表示)
            html.Img(
                src=_src,
                style={'width': '100%', 'height': '100%',
                        'position': 'absolute', # ボタン内に配置
                        'left': '0', 'top': '0',
                        'zIndex': 1 # テキストより下
                    }
            ),
            # 2. テキスト (「ON」または「OFF」の文字)
            html.Div(
                data['name'],
                style={
                    'position': 'absolute',
                    # ボタンの中央に配置
                    'top': '50%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)', # CSSで完全な中央揃え
                    'fontSize': '20px',
                    'fontFamily': 'Meiryo UI',
                    'fontWeight': 'bold',
                    'whiteSpace': 'nowrap', 
                    'color': 'black', # 文字色
                    'zIndex': 2 # 画像より上
                }
            )
        ]
        style={
            'position': 'absolute',
            'left': data['left'], 'top': data['top'],
            'width': '128px', 'height': '64px',
            'fontSize': '18px',
            'zIndex': 5,
            
            'padding': '0', # Paddingを除去して画像を表示
            'border': 'none', # ボーダーを除去
            'background': 'none',# 背景を除去
            'overflow': 'hidden' # 子要素がはみ出さないように
        }
    
        layout.append(html.Button(id=data['id'], n_clicks=0, children=children, style=style))

def _add_lamp_button(layout, button_list):
    font_size = '20px'
    for data in button_list:
        children=[
            # 1. 画像 (背景または状態表示)
            html.Img(
                id=data['img_id'], # Img ID をコールバックの Output に使う
                src='/assets/images/PlasticSquare_G.png',
                style={'width': '100%', 'height': '100%',
                        'position': 'absolute', # ボタン内に配置
                        'left': '0', 'top': '0',
                        'zIndex': 1 # テキストより下
                    }
            ),
            # 2. テキスト (「ON」または「OFF」の文字)
            html.Div(
                data['name'],
                style={
                    'position': 'absolute',
                    # ボタンの中央に配置
                    'top': '50%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)', # CSSで完全な中央揃え
                    'fontSize': f'{font_size}',
                    'whiteSpace': 'nowrap',  # 折り返しを無効にする
                    'fontFamily': 'Meiryo UI',
                    'fontWeight': 'bold',
                    'color': 'black', # 文字色
                    'zIndex': 2 # 画像より上
                }
            )
        ]
        style={
            'position': 'absolute',
            'left': data['left'], 'top': data['top'],
            'width': '128px', 'height': '64px',
            'zIndex': 5,
            # children の absolute 配置を基準にするため、position: relative は必須
            #'position': 'relative', 
            'padding': '0', # Paddingを除去して画像を表示
            'border': 'none', # ボーダーを除去
            'background': 'none',# 背景を除去
            #'overflow': 'hidden' # 子要素がはみ出さないように
        }
    
        layout.append(html.Button(id=data['id'], n_clicks=0, children=children, style=style))

# テーブルの行数
ALM_NUM_ROWS = 15    # アラーム行数

def create_auto_alerm_layout():
    layout = []    
    sample_alarm = [
        # {ALARM_COLUMN_IDS[0]: '12:00:00', ALARM_COLUMN_IDS[1]: 'CRITICAL', ALARM_COLUMN_IDS[2]: 'システム', ALARM_COLUMN_IDS[3]: 'エラーのメッセージ'},
        # {ALARM_COLUMN_IDS[0]: '11:00:00', ALARM_COLUMN_IDS[1]: 'WARNING', ALARM_COLUMN_IDS[2]: 'センサー', ALARM_COLUMN_IDS[3]: '警告のメッセージ'},
        # {ALARM_COLUMN_IDS[0]: '10:00:00', ALARM_COLUMN_IDS[1]: 'INFO', ALARM_COLUMN_IDS[2]: '圧力',  ALARM_COLUMN_IDS[3]: ''},
    ]
    empty_row_dict = {col_id: '' for col_id in ALARM_COLUMN_IDS}
    alarm_list = sample_alarm + [empty_row_dict] * (ALM_NUM_ROWS - len(sample_alarm))

    # ... DataTableの定義（前の回答の例を使用） ...
    alarm_table = dash_table.DataTable(
        id='auto-alarm-table',
        columns=ALARM_COLUMN_DEFS,
        data=alarm_list,
        style_table={
            'table-layout': 'fixed'
        },
        style_cell_conditional=[
            {'if': {'column_id': ALARM_COLUMN_IDS[0]},
            'width': '120px'},
            {'if': {'column_id': ALARM_COLUMN_IDS[1]},
            'width': '120px'},
            {'if': {'column_id': ALARM_COLUMN_IDS[2]},
            'width': '120px'}
        ],
        style_cell={
            'fontSize': '18px',
            'textAlign': 'left',
            'fontFamily': 'Meiryo UI',
        },
        style_header={
            'fontSize': '20px',
            'fontWeight': 'bold',
            'fontFamily': 'Meiryo UI',
        },
        style_data_conditional=[
            {
                # CRITICALな行を赤くハイライト
                'if': {'filter_query': '{level} = "CRITICAL"'},
                'backgroundColor': "#FF847D",
                #'color': 'white',
                'fontWeight': 'bold'
            },
            {
                # WARNINGのテキストをオレンジ色に
                'if': {'filter_query': '{level} = "WARNING"'},
                'backgroundColor': "#FFE77D",
                'fontWeight': 'bold'
            }
        ]
    )

    # ★ ここがDataTableの座標と大きさを制御する
    layout.append(html.Div(
            id='auto-alarm-container',
            children=[alarm_table],
            style={
                'position': 'absolute',
                'left': '12px', 'top': '8px',
                'width': '760px', 'height': '333px',
                # 2. 座標/配置の定義（中央揃えの例）
                'marginLeft': 'auto',     # 左マージンを自動に
                'marginRight': 'auto',    # 右マージンを自動に
                'padding': '0px',        # 内側の余白
                'border': '1px solid #ccc' # 境界線
            }
        ))
    
    
    
    # 3. 操作ボタン (z-index: 5)
    _add_button(layout, push_button_data)
    _add_lamp_button(layout, lamp_button_data)

    # 4. ダミーコンポーネント (操作ボタンのOutコールバック用)
    layout.append(
        html.Div(id='dummy-button-autoreset', style={'display': 'none'})
    )
    
    return layout