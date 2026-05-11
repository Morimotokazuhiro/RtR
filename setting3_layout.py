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
    {'left': '36px', 'top': '100px', 'text': 'SVM3'+NEWLINE+'A室テンション制御'},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': 'SVM4'+NEWLINE+'B室テンション制御'},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
    # 右の列
    {'left': '36px', 'top': '100px', 'text': 'SVM2'+NEWLINE+'圧力制御弁PID'},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '36px', 'top': '100px', 'text': ''},
]
unit_text_data = [
    # 左の列
    {'left': '256px', 'top': '100px', 'text': 'サンプリング周期'+NEWLINE+'(ms)'},
    {'left': '256px', 'top': '100px', 'text': '入力フィルタ定数'+NEWLINE+'(%)'},
    {'left': '256px', 'top': '100px', 'text': '比例ゲイン'+NEWLINE+'(%)'},
    {'left': '256px', 'top': '100px', 'text': '積分時間'+NEWLINE+'(*100ms)'},
    {'left': '256px', 'top': '100px', 'text': '微分ゲイン'+NEWLINE+'(%)'},
    {'left': '256px', 'top': '100px', 'text': '微分時間'+NEWLINE+'(*10ms)'},
    {'left': '36px', 'top': '100px', 'text': ''},
    {'left': '256px', 'top': '100px', 'text': 'サンプリング周期'+NEWLINE+'(ms)'},
    {'left': '256px', 'top': '100px', 'text': '入力フィルタ定数'+NEWLINE+'(%)'},
    {'left': '256px', 'top': '100px', 'text': '比例ゲイン'+NEWLINE+'(%)'},
    {'left': '256px', 'top': '100px', 'text': '積分時間'+NEWLINE+'(*100ms)'},
    {'left': '256px', 'top': '100px', 'text': '微分ゲイン'+NEWLINE+'(%)'},
    {'left': '256px', 'top': '100px', 'text': '微分時間'+NEWLINE+'(*10ms)'},
    # 右の列
    {'left': '256px', 'top': '100px', 'text': 'サンプリング周期'+NEWLINE+'(ms)'},
    {'left': '256px', 'top': '100px', 'text': '入力フィルタ定数'+NEWLINE+'(%)'},
    {'left': '256px', 'top': '100px', 'text': '比例ゲイン'+NEWLINE+'(%)'},
    {'left': '256px', 'top': '100px', 'text': '積分時間'+NEWLINE+'(*100ms)'},
    {'left': '256px', 'top': '100px', 'text': '微分ゲイン'+NEWLINE+'(%)'},
    {'left': '256px', 'top': '100px', 'text': '微分時間'+NEWLINE+'(*10ms)'},
]
# limit_text_data = [
#     {'left': '376px', 'top': '8px', 'text': '上限'},
#     {'left': '1040px', 'top': '8px', 'text': '上限'},
# ]
# --------------------------------------------------------
# モニターと設定の入力ボックスのリスト
# コールバックで'children'を変更します
# --------------------------------------------------------
BASE_INDEX = 120 # D4200のインデックスは120番目と想定
setting_para_data = [
    # 左の列
    {'id': 'set3_SVM3_sam', 'left': '356px','top': '8px', 'address': 4200, 'data_index': BASE_INDEX + 0,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM3_sam_trigger',
        'name': 'SVM3 サンプリング周期', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM3_inp', 'left': '356px','top': '80px', 'address': 4201, 'data_index': BASE_INDEX + 1,
        'format': FormatSpecifier.F3_2, 'trigger_id': 'set3_SVM3_inp_trigger',
        'name': 'SVM3 入力フィルタ定数', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM3_hirei', 'left': '356px','top': '152px', 'address': 4202, 'data_index': BASE_INDEX + 2,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM3_hirei_trigger',
        'name': 'SVM3 比例ゲイン', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM3_sekibun', 'left': '356px','top': '224px', 'address': 4203, 'data_index': BASE_INDEX + 3,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM3_sekibun_trigger',
        'name': 'SVM3 積分時間', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM3_bibunG', 'left': '356px','top': '296px', 'address': 4204, 'data_index': BASE_INDEX + 4,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM3_bibunG_trigger',
        'name': 'SVM3 微分ゲイン', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM3_bibunT', 'left': '356px','top': '368px', 'address': 4205, 'data_index': BASE_INDEX + 5,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM3_bibunT_trigger',
        'name': 'SVM3 微分時間', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_N/A'},
    {'id': 'set3_SVM4_sam', 'left': '356px','top': '8px', 'address': 4206, 'data_index': BASE_INDEX + 6,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM4_sam_trigger',
        'name': 'SVM4 サンプリング周期', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM4_inp', 'left': '356px','top': '80px', 'address': 4207, 'data_index': BASE_INDEX + 7,
        'format': FormatSpecifier.F3_2, 'trigger_id': 'set3_SVM4_inp_trigger',
        'name': 'SVM4 入力フィルタ定数', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM4_hirei', 'left': '356px','top': '152px', 'address': 4208, 'data_index': BASE_INDEX + 8,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM4_hirei_trigger',
        'name': 'SVM4 比例ゲイン', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM4_sekibun', 'left': '356px','top': '224px', 'address': 4209, 'data_index': BASE_INDEX + 9,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM4_sekibun_trigger',
        'name': 'SVM4 積分時間', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM4_bibunG', 'left': '356px','top': '296px', 'address': 4210, 'data_index': BASE_INDEX + 10,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM4_bibunG_trigger',
        'name': 'SVM4 微分ゲイン', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM4_bibunT', 'left': '356px','top': '368px', 'address': 4211, 'data_index': BASE_INDEX + 11,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM4_bibunT_trigger',
        'name': 'SVM4 微分時間', 'min_value': 0.0, 'max_value': 500.0},
    # 右の列
    {'id': 'set3_SVM2_sam', 'left': '356px','top': '8px', 'address': 4212, 'data_index': BASE_INDEX + 12,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM2_sam_trigger',
        'name': 'SVM2 サンプリング周期', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM2_inp', 'left': '356px','top': '80px', 'address': 4213, 'data_index': BASE_INDEX + 13,
        'format': FormatSpecifier.F3_2, 'trigger_id': 'set3_SVM2_inp_trigger',
        'name': 'SVM2 入力フィルタ定数', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM2_hirei', 'left': '356px','top': '152px', 'address': 4214, 'data_index': BASE_INDEX + 14,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM2_hirei_trigger',
        'name': 'SVM2 比例ゲイン', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM2_sekibun', 'left': '356px','top': '224px', 'address': 4215, 'data_index': BASE_INDEX + 15,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM2_sekibun_trigger',
        'name': 'SVM2 積分時間', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM2_bibunG', 'left': '356px','top': '296px', 'address': 4216, 'data_index': BASE_INDEX + 16,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM2_bibunG_trigger',
        'name': 'SVM2 微分ゲイン', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set3_SVM2_bibunT', 'left': '356px','top': '368px', 'address': 4217, 'data_index': BASE_INDEX + 17,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set3_SVM2_bibunT_trigger',
        'name': 'SVM2 微分時間', 'min_value': 0.0, 'max_value': 500.0},
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
for i, item in enumerate(setting_para_data):
    x_index =  i // ROW_COUNT
    y_index = i % ROW_COUNT
    item['left'] = f'{BASE_UPPER_LEFT + x_index*664}px'
    item['top'] = f'{BASE_TOP + y_index*72}px'

# N/Aを除いたリストで結合する
setting_data = [data for data in setting_para_data if data.get('id') != 'set3_N/A']

def create_setting3_layout():
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

    # 5. ダミーコンポーネント (テキストボックスのOutコールバック用)
    layout.append(
        html.Div(id='dummy-button-set3', style={'display': 'none'})
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
    create_setting_modal(layout, '-set3')

    return layout