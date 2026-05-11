from dash import html, dcc
from enum import Enum
from constans import FormatSpecifier

from common_modal_layout import create_setting_modal

# --------------------------------------------------------
# テキストとアドレスのリスト
# --------------------------------------------------------
# 改行文字コード（自由に変更可）
NEWLINE = '<br>'
text_data = [
    # 左の列
    {'left': '36px', 'top': '100px', 'text': 'RF1'+NEWLINE+'RF電源'},
    {'left': '36px', 'top': '100px', 'text': 'H1'+NEWLINE+'ヒーター'},
    {'left': '36px', 'top': '100px', 'text': 'H2'+NEWLINE+'ヒーター'},
    {'left': '36px', 'top': '100px', 'text': 'CHL1'+NEWLINE+'チラー'},
    {'left': '36px', 'top': '100px', 'text': 'SVM1'+NEWLINE+'サーボオン'},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': 'SVM1'+NEWLINE+'メンテナンス'},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': '----'+NEWLINE+'メンテ旋回ブレーキ'},
    {'left': '36px', 'top': '100px', 'text': ''},
    # 左の列設定
    {'left': '464px', 'top': '100px', 'text': '出力'+NEWLINE+'(W)'},
    {'left': '464px', 'top': '100px', 'text': '温度'+NEWLINE+'(℃)'},
    {'left': '464px', 'top': '100px', 'text': '温度'+NEWLINE+'(℃)'},
    {'left': '464px', 'top': '100px', 'text': ''},
    {'left': '464px', 'top': '100px', 'text': ''},
    {'left': '464px', 'top': '100px', 'text': ''},
    {'left': '464px', 'top': '100px', 'text': '位置'+NEWLINE+'(mm)'},
    {'left': '464px', 'top': '100px', 'text': '速度'+NEWLINE+'(mm/s)'},
    {'left': '464px', 'top': '100px', 'text': ''},
    {'left': '464px', 'top': '100px', 'text': ''},
    # 右の列設定
    {'left': '848px', 'top': '100px', 'text': ''},
    {'left': '848px', 'top': '100px', 'text': '加熱ステップ数'+NEWLINE+'(ステップ)'},
    {'left': '848px', 'top': '100px', 'text': '加熱ステップ数'+NEWLINE+'(ステップ)'},
]
BASE_TOP = 8
# ラベルのy座標の再割り当て
for i, item in enumerate(text_data):
    index = i % 10
    item['top'] = f'{index*72+BASE_TOP}px'

# --------------------------------------------------------
# ボタンのリスト
# コールバックで'src'を変更し、押下時のアドレス参照にも使います
# --------------------------------------------------------
lp_button_data = [
    # 左の列
    {'id': 'op2_RF1_1', 'img_id': 'op2_RF1_img1', 'left': '204px','top': '8px', 'sw_address': 3063, 'address': 863, 'type':'ON', 'name':'ON', 'reverse': False},
    {'id': 'op2_RF1_2', 'img_id': 'op2_RF1_img2', 'left': '336px','top': '8px', 'sw_address': 3263, 'address': 863, 'type':'OFF', 'name':'OFF', 'reverse': True},

    {'id': 'op2_H1_1', 'img_id': 'op2_H1_img1','left': '204px','top': '80px', 'sw_address': 3065, 'address': 865, 'type':'ON', 'name':'ON', 'reverse': False},
    {'id': 'op2_H1_2', 'img_id': 'op2_H1_img2','left': '336px','top': '80px', 'sw_address': 3265, 'address': 865, 'type':'OFF', 'name':'OFF', 'reverse': True},

    {'id': 'op2_H2_1', 'img_id': 'op2_H2_img1','left': '204px','top': '152px', 'sw_address': 3066, 'address': 866, 'type':'ON', 'name':'ON', 'reverse': False},
    {'id': 'op2_H2_2', 'img_id': 'op2_H2_img2','left': '336px','top': '152px', 'sw_address': 3266, 'address': 866, 'type':'OFF', 'name':'OFF', 'reverse': True},

    {'id': 'op2_CHL1_1', 'img_id': 'op2_CHL1_img1','left': '204px','top': '224px', 'sw_address': 3064, 'address': 864, 'type':'ON', 'name':'起動', 'reverse': False},
    {'id': 'op2_CHL1_2', 'img_id': 'op2_CHL1_img2','left': '336px','top': '224px', 'sw_address': 3264, 'address': 864, 'type':'OFF', 'name':'停止', 'reverse': True},

    {'id': 'op2_SVM1_1', 'img_id': 'op2_SVM1_img1','left': '204px','top': '296px', 'sw_address': 3096, 'address': 896, 'type':'ON', 'name':'ON', 'reverse': False},
    {'id': 'op2_SVM1_2', 'img_id': 'op2_SVM1_img2','left': '336px','top': '296px', 'sw_address': 3296, 'address': 896, 'type':'OFF', 'name':'OFF', 'reverse': True},

    {'id': 'op2_mnt_lock_1', 'img_id': 'op2_mnt_lock_img1','left': '204px','top': '584px', 'sw_address': 3060, 'address': 860, 'type':'ON', 'name':'解除', 'reverse': False},
    {'id': 'op2_mnt_lock_2', 'img_id': 'op2_mnt_lock_img2','left': '336px','top': '584px', 'sw_address': 3260, 'address': 860, 'type':'OFF', 'name':'ロック', 'reverse': True},
]
button_data = [
    {'id': 'op2_SVM1_mnt_1', 'img_id': 'op2_SVM1_mnt_img1','left': '204px','top': '440px', 'sw_address': 3092, 'name':'移動'},
    {'id': 'op2_SVM1_mnt_2', 'img_id': 'op2_SVM1_mnt_img2','left': '336px','top': '440px', 'sw_address': 3292, 'name':'停止'},
    {'id': 'op2_SVM1_mnt_3', 'img_id': 'op2_SVM1_mnt_img3','left': '204px','top': '512px', 'sw_address': 3091, 'name':'原点復帰'},
]
ope2button_click_indicators = lp_button_data + button_data

# --------------------------------------------------------
# モニターと設定の入力ボックスのリスト
# コールバックで'children'を変更します
# --------------------------------------------------------
setting_data = [
    {'id': 'op2_RF1_SV', 'left': '564px','top': '8px', 'address': 4000, 'data_index': 0,
        'format': FormatSpecifier.F4_1, 'trigger_id': 'op2_RF1_trigger',
        'name': 'RF1 パワー', 'min_value': 0.0, 'max_value': 1000.0},
    {'id': 'op2_H1_SV', 'left': '564px','top': '80px', 'address': 4002, 'data_index': 1,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op2_H1_trigger',
        'name': 'H1 温度', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op2_H2_SV', 'left': '564px','top': '152px', 'address': 4004, 'data_index': 2,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op2_H2_trigger',
        'name': 'H2 温度', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op2_SVM1_pos_SV', 'left': '564px','top': '440px', 'address': 4024, 'data_index': 12,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op2_SVM1_pos_trigger',
        'name': 'SVM1 位置', 'min_value': 0.0, 'max_value': 100.0},
    {'id': 'op2_SVM1_spd_SV', 'left': '564px','top': '512px', 'address': 4026, 'data_index': 13,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op2_SVM1_spd_trigger',
        'name': 'SVM1 速度', 'min_value': 0.0, 'max_value': 100.0},

    {'id': 'op2_H1_step_SV', 'left': '996px','top': '80px', 'address': 4060, 'data_index': 30,
        'format': FormatSpecifier.D, 'trigger_id': 'op2_H1_trigger',
        'name': 'H1 加熱ステップ数', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op2_H2_step_SV', 'left': '996px','top': '152px', 'address': 4061, 'data_index': 31,
        'format': FormatSpecifier.D, 'trigger_id': 'op2_H2_trigger',
        'name': 'H2 加熱ステップ数', 'min_value': 0.0, 'max_value': 500.0},
]
monitor_data = [
    {'id': 'op2_H1_PV', 'left': '696px','top': '80px', 'address': 6020, 'format': FormatSpecifier.F3_1},
    {'id': 'op2_H2_PV', 'left': '696px','top': '152px', 'address': 6022, 'format': FormatSpecifier.F3_1},
]
ope2textbox_children_indicators = (
    monitor_data +
    setting_data
)

# インターロックランプ
lamp_data = [
    # 左の列 ランプ
    {'id': 'op2_RF1LP_1', 'img_id': 'op2_RF1LP_img1', 'left': '176px','top': '12px', 'address': 3463},
    {'id': 'op2_H1LP_1', 'img_id': 'op2_H1LP_img1','left': '176px','top': '84px', 'address': 3465},
    {'id': 'op2_H2LP_1', 'img_id': 'op2_H2LP_img1','left': '176px','top': '156px', 'address': 3466},
    #{'id': 'op2_SVM1LP_1', 'img_id': 'op2_SVM1LP_img1','left': '176px','top': '228px', 'address': 3467},
    #{'id': 'op2_SVM1LP_2', 'img_id': 'op2_SVM1LP_img2','left': '176px','top': '256px', 'address': 3490},
    {'id': 'op2_CHL1LP_1', 'img_id': 'op2_CHL1LP_img1','left': '176px','top': '228px', 'address': 3464},
    {'id': 'op2_SVM1_SV_1', 'img_id': 'op2_SVM1_SV_img1','left': '176px','top': '300px', 'address': 3496},
    {'id': 'op2_SVM1_mnt1_LP_1', 'img_id': 'op2_SVM1_mnt1_LP_img1','left': '176px','top': '444px', 'address': 3492},
    {'id': 'op2_SVM1_mnt3_LP_1', 'img_id': 'op2_SVM1_mnt3_LP_img1','left': '176px','top': '516px', 'address': 3491},
    {'id': 'op2_mnt_lock_LP_1', 'img_id': 'op2_mnt_lock_LP_img1','left': '176px','top': '588px', 'address': 3460},
]

def _add_lp_button(layout, button_list):
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
            'padding': '0', # Paddingを除去して画像を表示
            'border': 'none', # ボーダーを除去
            'background': 'none',# 背景を除去
        }
        layout.append(html.Button(id=data['id'], n_clicks=0, children=children, style=style))

def _add_button(layout, data, _src):
    font_size = '20px'
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
        'padding': '0', # Paddingを除去して画像を表示
        'border': 'none', # ボーダーを除去
        'background': 'none',# 背景を除去
    }
    layout.append(html.Button(id=data['id'], n_clicks=0, children=children, style=style))

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

def create_operation2_layout():
    """
    手動運転画面のモード2 (操作ボタンエリア) のレイアウト
    """
    layout = []

    # 1. テキスト (z-index: 5)
    for i,data in enumerate(text_data):
        # # 'left'と'top'の値からpxを除去し、オフセットを適用
        id = f'op2_text{i}'
        left_val = int(data['left'].replace('px', '')) + 16
        top_val = int(data['top'].replace('px', '')) - 12
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

    # 3. 操作ボタン (z-index: 5)
    _add_lp_button(layout, lp_button_data)
    # 3.通常の操作ボタン
    _add_button(layout, button_data[0], '/assets/images/PlasticRect_G.png')
    _add_button(layout, button_data[1], '/assets/images/PlasticRect_R.png')
    _add_button(layout, button_data[2], '/assets/images/PlasticRect_G.png')
    
    # 4. インターロックランプの追加
    for data in lamp_data:
        _add_lamp(layout, data)

    # 5. ダミーコンポーネント (操作ボタンのOutコールバック用)
    layout.append(
        html.Div(id='dummy-button-op2', style={'display': 'none'})
    )

    # 6. モニター値 (z-index: 5)
    for data in monitor_data:
        # 'top'の文字列から数値を取り出し、計算する
        top_value = int(data['top'].replace('px', '')) + 4
        className='operation_monitor-style' # CSSクラスを適用
        style = {
            'position': 'absolute',
            'left': data['left'],
            'top': f'{top_value}px',
            'zIndex': 5,
        }
        layout.append(html.Div(data['id'], id=data['id'], className=className, style=style))

    # 7. 設定値 (z-index: 5)
    for data in setting_data:
        top_value = int(data['top'].replace('px', '')) + 4
        className='operation_setting-style clickable-setting' # 新しいCSSクラスを追加
        style = {
            'position': 'absolute',
            'left': data['left'],
            'top': f'{top_value}px',
            'zIndex': 5,
        }
        # この html.Div がクリックされたら、隠された dcc.Store を更新する
        layout.append(html.Div(
            data['id'], 
            id=data['id'], 
            n_clicks=0, # クリックを監視
            className=className, 
            style=style
        ))

    # 8. ポップアップ用のレイアウト
    create_setting_modal(layout, '-op2')

    return layout