from dash import dash_table
from dash import html

# --------------------------------------------------------
# テキストとアドレスのリスト
# --------------------------------------------------------
# 改行文字コード（自由に変更可）
NEWLINE = '<br>'
text_data1 = [
    {'left': '956px', 'top': '54px', 'text': '自動'+NEWLINE+'真空引き粗びき'},
    {'left': '956px', 'top': '122px', 'text': '自動'+NEWLINE+'高真空真空引き'},
    {'left': '956px', 'top': '194px', 'text': '自動 チャンバー'+NEWLINE+'N2パージ'},
]
text_data2 = [
    {'left': '1100px', 'top': '0px', 'text': 'サイクル運転'},
]
# 自動運転ボタン
auto_button_data = [
    # ONボタン
    {'id': 'mna_auto1_bt1', 'img_id': 'mna_auto1_bt_img1', 'left': '1124px','top': '54px', 'sw_address': 3097, 'address': 908, 'type':'AUTO_bt', 'name':'ON', 'reverse': False,
     'src': '/assets/images/PlasticSquare_G.png'},
    {'id': 'mna_auto2_bt1', 'img_id': 'mna_auto2_bt_img1', 'left': '1124px','top': '126px', 'sw_address': 3098, 'address': 909, 'type':'AUTO_bt', 'name':'ON', 'reverse': False,
     'src': '/assets/images/PlasticSquare_G.png'},
    {'id': 'mna_auto3_bt1', 'img_id': 'mna_auto3_bt_img1', 'left': '1124px','top': '198px', 'sw_address': 3099, 'address': 910, 'type':'AUTO_bt', 'name':'ON', 'reverse': False,
     'src': '/assets/images/PlasticSquare_G.png'},

    # OFFボタン
    {'id': 'mna_auto1_bt2', 'img_id': 'mna_auto1_bt_img2', 'left': '1256px','top': '54px', 'sw_address': 3297, 'address': 897, 'type':'OFF', 'name':'OFF', 'reverse': True,
     'src': '/assets/images/PlasticSquare_G.png'},
    {'id': 'mna_auto2_bt2', 'img_id': 'mna_auto2_bt_img2', 'left': '1256px','top': '126px', 'sw_address': 3298, 'address': 898, 'type':'OFF', 'name':'OFF', 'reverse': True,
     'src': '/assets/images/PlasticSquare_G.png'},
    {'id': 'mna_auto3_bt2', 'img_id': 'mna_auto3_bt_img2', 'left': '1256px','top': '198px', 'sw_address': 3299, 'address': 899, 'type':'OFF', 'name':'OFF', 'reverse': True,
     'src': '/assets/images/PlasticSquare_G.png'},
]

reset_button_data = [
    {'id': 'btn-manual-al-reset', 'left': '816px', 'top': '140px', 'sw_address': 502, 'name': 'リセット'},
    {'id': 'btn-manual-bz-stop', 'left': '816px', 'top': '212px', 'sw_address': 503, 'name': 'ブザー停止'},
]
mnabutton_src_indicators = reset_button_data + auto_button_data

# インターロックランプ
lamp_data = [
    {'id': 'mna_auto1LP_1', 'img_id': 'mna_auto1LP_img1','left': '1096px','top': '54px', 'address': 3497},
    {'id': 'mna_auto2LP_1', 'img_id': 'mna_auto2LP_img1','left': '1096px','top': '126px', 'address': 3498},
    {'id': 'mna_auto3LP_1', 'img_id': 'mna_auto3LP_img1','left': '1096px','top': '198px', 'address': 3499},
]


ALARM_COLUMN_DEFS = [
    {'name': '時刻', 'id': 'time'},
    {'name': '重要度', 'id': 'level'},
    {'name': '種類', 'id': 'type'},
    {'name': 'メッセージ', 'id': 'message'},
]
# アラームテーブルの列IDをリストで抽出（style_cell_conditionalなどで利用するため）
ALARM_COLUMN_IDS = [col['id'] for col in ALARM_COLUMN_DEFS]

# 四角い線を定義する関数
def _add_rectangle(layout, left, top, width, height, color, z_index=1):
    style = {
        'position': 'absolute',
        'left': f'{left}px',
        'top': f'{top}px',
        'width': f'{width}px',
        'height': f'{height}px',
        'border': f'1px solid {color}',
        'z-index': z_index
    }
    layout.append(html.Div(style=style))

def _add_lamp(layout, data):
    children=[
        # 1. 画像 (背景または状態表示)
        html.Img(
            id=data['img_id'], # Img ID をコールバックの Output に使う
            src='/assets/images/RealCircle2_R.png',
            style={'width': '100%', 'height': '100%',
                    'position': 'absolute', # ボタン内に配置
                    'left': '0', 'top': '0',
                    'zIndex': 1 # テキストより下
                }
        ),
    ]
    style={
        'position': 'absolute',
        'left': data['left'], 'top': data['top'],
        'width': '24px', 'height': '24px',
        'zIndex': 5,
        'padding': '0', # Paddingを除去して画像を表示
        'border': 'none', # ボーダーを除去
        'background': 'none',# 背景を除去
    }
    
    layout.append(html.Div(id=data['id'], children=children, style=style))

def _add_text(layout, label_list):
    for i,data in enumerate(label_list):
        # # 'left'と'top'の値からpxを除去し、オフセットを適用
        id = f'mna_text{i}'
        left_val = data['left']
        top_val = data['top']
        children = data['text']
        
        style={
            'position': 'absolute',
            'left': left_val,
            'top': top_val,
            'fontSize': '20px',
            'color': 'black',
            'fontFamily': 'Meiryo UI',
            'zIndex': 5,
        }
        layout.append(html.P(id=id, children=children, style=style))
    

# テーブルの行数
ALM_NUM_ROWS = 8    # アラーム行数
MES_NUM_ROWS = 10   # メッセージ行数

def create_manual_alerm_layout():
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
        id='alarm-table',
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
            id='manual-alarm-container',
            children=[alarm_table],
            style={
                'position': 'absolute',
                'left': '12px', 'top': '8px',
                'width': '785px', 'height': '270px',
                # 2. 座標/配置の定義（中央揃えの例）
                'marginLeft': 'auto',     # 左マージンを自動に
                'marginRight': 'auto',    # 右マージンを自動に
                'padding': '0px',        # 内側の余白
                'border': '1px solid #ccc' # 境界線
            }
        ))
    
    # 3.リセットボタン
    for data in reset_button_data:
        children=[
            # 1. 画像 (背景または状態表示)
            html.Img(
                src='/assets/images/PlasticRect_Y.png',
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
        layout.append(html.Button(id=data['id'], n_clicks=0,children=children, style=style))

    # 四角の線 (z-index: 1)
    _add_rectangle(layout, left=950, top=50, width=447, height=216, color='#999999', z_index=1)

    _add_text(layout, text_data2)

    for i,data in enumerate(text_data1):
        # # 'left'と'top'の値からpxを除去し、オフセットを適用
        id = f'mna_text{i}'
        left_val = int(data['left'].replace('px', '')) + 16
        top_val = int(data['top'].replace('px', '')) - 16
        parts = data['text'].split(NEWLINE)
        if len(parts) >= 2:
            # 改行で2段に分ける（3段表示は考慮しない）
            children = [
                html.Span(parts[0]),
                html.Br(),
                html.Span(parts[1])
            ]
        else:
            children = data['text']
        
        style={
            'position': 'absolute',
            'left': f'{left_val}px',
            'top': f'{top_val}px',
            'fontSize': '20px',
            #'fontWeight': 'bold',
            'color': 'black',
            'fontFamily': 'Meiryo UI',
            'zIndex': 5,
        }
        layout.append(html.P(id=id, children=children, style=style))

    # 3.リセットボタン
    for data in auto_button_data:
        _src = data['src']
        children=[
            # 1. 画像 (背景または状態表示)
            html.Img(
                id=data['img_id'], # Img ID をコールバックの Output に使う
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
        # ダミーは表示しない
        # if data['id'] == 'reset_dummy':
        #     style['display'] = 'none'

        layout.append(html.Button(id=data['id'], n_clicks=0,children=children, style=style))

    # 4. インターロックランプの追加
    for data in lamp_data:
        _add_lamp(layout, data)
    # 4. ダミーコンポーネント (操作ボタンのOutコールバック用)
    layout.append(
        html.Div(id='dummy-button-manualreset', style={'display': 'none'})
    )
    
    return layout