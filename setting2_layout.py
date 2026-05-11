from dash import html
from constans import FormatSpecifier

from common_modal_layout import create_setting_modal

# --------------------------------------------------------
# テキストとアドレスのリスト
# --------------------------------------------------------
# 改行文字コード（自由に変更可）
NEWLINE = '<br>'
label_text_data = [
    # 左の列
    {'left': '36px', 'top': '100px', 'text': '真空排気開始'},
    {'left': '36px', 'top': '100px', 'text': '粗びき'},
    {'left': '36px', 'top': '100px', 'text': 'チャンバー'+NEWLINE+'真空引き'},
    {'left': '36px', 'top': '100px', 'text': 'TMP起動'},
    {'left': '36px', 'top': '100px', 'text': 'チャンバー'+NEWLINE+'高真空引き'},
    {'left': '36px', 'top': '100px', 'text': 'チャンバー'+NEWLINE+'再排気'},
    {'left': '36px', 'top': '100px', 'text': '昇温'},
    {'left': '36px', 'top': '100px', 'text': '再排気回数超過'},
    {'left': '36px', 'top': '100px', 'text': 'VPP'+NEWLINE+'異常電圧'},
    {'left': '36px', 'top': '100px', 'text': 'テンション'+NEWLINE+'正常範囲'},
]
unit_text_data = [
    # 左の列
    {'left': '256px', 'top': '100px', 'text': 'タイムアウト'+NEWLINE+'(sec)'},
    {'left': '256px', 'top': '100px', 'text': 'タイムアウト'+NEWLINE+'(sec)'},
    {'left': '256px', 'top': '100px', 'text': 'タイムアウト'+NEWLINE+'(sec)'},
    {'left': '256px', 'top': '100px', 'text': 'タイムアウト'+NEWLINE+'(sec)'},
    {'left': '256px', 'top': '100px', 'text': 'タイムアウト'+NEWLINE+'(min)'},
    {'left': '256px', 'top': '100px', 'text': 'タイムアウト'+NEWLINE+'(sec)'},
    {'left': '256px', 'top': '100px', 'text': 'タイムアウト'+NEWLINE+'(min)'},
    {'left': '256px', 'top': '100px', 'text': '回数'+NEWLINE+'(回)'},
    {'left': '256px', 'top': '100px', 'text': '電圧'+NEWLINE+'(V)'},
    {'left': '256px', 'top': '100px', 'text': '角度'+NEWLINE+'(°)'},
]
limit_text_data = [
    {'left': '376px', 'top': '8px', 'text': '上限'},
    {'left': '508px', 'top': '8px', 'text': '下限'},
]
# --------------------------------------------------------
# モニターと設定の入力ボックスのリスト
# コールバックで'children'を変更します
# --------------------------------------------------------
BASE_INDEX = 120 # D4200のインデックスは120番目と想定
setting_upper_data = [
    # 左の列
    {'id': 'set2_auto_to1', 'left': '356px','top': '8px', 'address': 4218, 'data_index': BASE_INDEX + 18, 'gain':10,
        'format': FormatSpecifier.D, 'trigger_id': 'set2_auto_to1_trigger',
        'name': '真空排気開始 タイムアウト', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set2_auto_to2', 'left': '356px','top': '80px', 'address': 4219, 'data_index': BASE_INDEX + 19, 'gain':10,
        'format': FormatSpecifier.D, 'trigger_id': 'set2_auto_to2_trigger',
        'name': '粗びき タイムアウト', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set2_auto_to3', 'left': '356px','top': '152px', 'address': 4220, 'data_index': BASE_INDEX + 20, 'gain':10,
        'format': FormatSpecifier.D, 'trigger_id': 'set2_auto_to3_trigger',
        'name': 'チャンバー真空引き タイムアウト', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set2_auto_to4', 'left': '356px','top': '224px', 'address': 4221, 'data_index': BASE_INDEX + 21, 'gain':10,
        'format': FormatSpecifier.D, 'trigger_id': 'set2_auto_to4_trigger',
        'name': 'TMP起動 タイムアウト', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set2_auto_to5', 'left': '356px','top': '296px', 'address': 4222, 'data_index': BASE_INDEX + 22, 'gain':1,
        'format': FormatSpecifier.D, 'trigger_id': 'set2_auto_to5_trigger',
        'name': 'チャンバー高真空引き タイムアウト', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set2_auto_to6', 'left': '356px','top': '368px', 'address': 4223, 'data_index': BASE_INDEX + 23, 'gain':10,
        'format': FormatSpecifier.D, 'trigger_id': 'set2_auto_to6_trigger',
        'name': 'チャンバー再排気 タイムアウト', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set2_auto_to7', 'left': '356px','top': '368px', 'address': 4225, 'data_index': BASE_INDEX + 25, 'gain':1,
        'format': FormatSpecifier.D, 'trigger_id': 'set2_auto_to7_trigger',
        'name': '昇温 タイムアウト', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set2_auto_to8', 'left': '356px','top': '368px', 'address': 4224, 'data_index': BASE_INDEX + 24, 'gain':1,
        'format': FormatSpecifier.D, 'trigger_id': 'set2_auto_to8_trigger',
        'name': '再排気回数', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set2_RF1_1_vpp', 'left': '356px','top': '368px', 'address': 4240, 'data_index': BASE_INDEX + 40, 'gain':1,
        'format': FormatSpecifier.D, 'trigger_id': 'set2_RF1_vpp_1_trigger',
        'name': 'VPP異常電圧 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set2_tension_1', 'left': '356px','top': '368px', 'address': 4244, 'data_index': BASE_INDEX + 42, 'gain':1,
        'format': FormatSpecifier.F3_2, 'trigger_id': 'set2_tension_1_trigger',
        'name': 'テンション正常範囲 上限', 'min_value': 0.0, 'max_value': 500.0},
]
setting_low_data = [
    {'id': 'set2_RF1_2_vpp', 'left': '508px','top': '616px', 'address': 4242, 'data_index': BASE_INDEX + 41, 'gain':1,
        'format': FormatSpecifier.D, 'trigger_id': 'set2_RF1_vpp_2_trigger',
        'name': 'VPP異常電圧 下限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set2_tension_2', 'left': '508px','top': '688px', 'address': 4246, 'data_index': BASE_INDEX + 43, 'gain':1,
        'format': FormatSpecifier.F3_2, 'trigger_id': 'set2_tension_2_trigger',
        'name': 'テンション正常範囲 下限', 'min_value': 0.0, 'max_value': 500.0},
]

BASE_LABEL_LEFT = 36
BASE_TOP = 40
ROW_COUNT = 13
# ラベルの座標の再割り当て
for i, item in enumerate(label_text_data):
    x_index =  i // ROW_COUNT
    y_index = i % ROW_COUNT
    item['left'] = f'{BASE_LABEL_LEFT + x_index*664}px'
    item['top'] = f'{BASE_TOP + y_index*72}px'

BASE_UNIT_LEFT = 216
for i, item in enumerate(unit_text_data):
    x_index =  i // ROW_COUNT
    y_index = i % ROW_COUNT
    item['left'] = f'{BASE_UNIT_LEFT + x_index*664}px'
    item['top'] = f'{BASE_TOP + y_index*72}px'

BASE_UPPER_LEFT = 376
for i, item in enumerate(setting_upper_data):
    x_index =  i // ROW_COUNT
    y_index = i % ROW_COUNT
    item['left'] = f'{BASE_UPPER_LEFT + x_index*664}px'
    item['top'] = f'{BASE_TOP + y_index*72}px'

# N/Aを除いたリストで結合する
setting_para_data = setting_upper_data + setting_low_data
setting_data = [data for data in setting_para_data if data.get('id') != 'N/A']

def create_setting2_layout():
    layout = []
    text_data = label_text_data + unit_text_data

    # 1. テキスト (z-index: 5)
    for data in text_data:
        # # 'left'と'top'の値からpxを除去し、オフセットを適用
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
            'color': 'black',
            'fontFamily': 'Meiryo UI',
            'zIndex': 5,
        }
        layout.append(html.P(children=children, style=style))

    # 2. テキスト (z-index: 5)
    for data in limit_text_data:
        # # 'left'と'top'の値からpxを除去し、オフセットを適用
        left_val = int(data['left'].replace('px', ''))
        top_val = int(data['top'].replace('px', '')) - 12
        children = data['text']
        
        style={
            'position': 'absolute',
            'left': f'{left_val}px',
            'top': f'{top_val}px',
            'width': f'128px',
            'textAlign': 'center',
            'fontSize': '20px',
            'color': 'black',
            'fontFamily': 'Meiryo UI',
            'zIndex': 5,
        }
        layout.append(html.P(children=children, style=style))

    # 5. ダミーコンポーネント (テキストボックスのOutコールバック用)
    layout.append(
        html.Div(id='dummy-button-set2', style={'display': 'none'})
    )

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
    create_setting_modal(layout, '-set2')

    return layout