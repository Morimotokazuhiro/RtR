from dash import html
from constans import FormatSpecifier

from common_modal_layout import create_setting_modal

# --------------------------------------------------------
# テキストとアドレスのリスト
# --------------------------------------------------------
# 改行文字コード（自由に変更可）
NEWLINE = '<br>'
text_data = [
    # 左の列
    {'left': '36px', 'top': '8px', 'text': 'MFCG1'+NEWLINE+'H2 マスフロー'},
    {'left': '36px', 'top': '80px', 'text': 'MFCG2'+NEWLINE+'CH4 マスフロー'},
    {'left': '36px', 'top': '152px', 'text': 'MFCG3'+NEWLINE+'O2 マスフロー'},
    {'left': '36px', 'top': '224px', 'text': 'MFCG4'+NEWLINE+'Ar マスフロー'},
    {'left': '36px', 'top': '296px', 'text': 'MFCG5'+NEWLINE+'N2 マスフロー'},
    {'left': '36px', 'top': '368px', 'text': 'MFCG6'+NEWLINE+'H2 マスフロー'},
    {'left': '36px', 'top': '440px', 'text': 'MFCG7'+NEWLINE+'Ar マスフロー'},
    # 左の列設定
    {'left': '256px', 'top': '8px', 'text': '流量'+NEWLINE+'(sccm)'},
    {'left': '256px', 'top': '80px', 'text': '流量'+NEWLINE+'(sccm)'},
    {'left': '256px', 'top': '152px', 'text': '流量'+NEWLINE+'(sccm)'},
    {'left': '256px', 'top': '224px', 'text': '流量'+NEWLINE+'(sccm)'},
    {'left': '256px', 'top': '296px', 'text': '流量'+NEWLINE+'(sccm)'},
    {'left': '256px', 'top': '368px', 'text': '流量'+NEWLINE+'(sccm)'},
    {'left': '256px', 'top': '440px', 'text': '流量'+NEWLINE+'(sccm)'},
]
# --------------------------------------------------------
# モニターと設定の入力ボックスのリスト
# コールバックで'children'を変更します
# --------------------------------------------------------
setting_data = [
    {'id': 'op5_MFCG1_SV', 'left': '356px','top': '8px', 'address': 4006, 'data_index': 3,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op5_MFCG1_trigger',
        'name': 'MFCG1 H2', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op5_MFCG2_SV', 'left': '356px','top': '80px', 'address': 4008, 'data_index': 4,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op5_MFCG2_trigger',
        'name': 'MFCG2 CH4', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op5_MFCG3_SV', 'left': '356px','top': '152px', 'address': 4010, 'data_index': 5,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op5_MFCG3_trigger',
        'name': 'MFCG3 O2', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op5_MFCG4_SV', 'left': '356px','top': '224px', 'address': 4012, 'data_index': 6,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op5_MFCG4_trigger',
        'name': 'MFCG4 Ar', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op5_MFCG5_SV', 'left': '356px','top': '296px', 'address': 4014, 'data_index': 7,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op5_MFCG5_trigger',
        'name': 'MFCG5 N2', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op5_MFCG6_SV', 'left': '356px','top': '368px', 'address': 4016, 'data_index': 8,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op5_MFCG6_trigger',
        'name': 'MFCG6 H2', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op5_MFCG7_SV', 'left': '356px','top': '440px', 'address': 4018, 'data_index': 9,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op5_MFCG7_trigger',
        'name': 'MFCG7 Ar', 'min_value': 0.0, 'max_value': 500.0},
]
monitor_data = [
    {'id': 'op5_MFCG1_PV', 'left': '488px','top': '8px', 'address': 6034, 'format': FormatSpecifier.F3_1},
    {'id': 'op5_MFCG2_PV', 'left': '488px','top': '80px', 'address': 6036, 'format': FormatSpecifier.F3_1},
    {'id': 'op5_MFCG3_PV', 'left': '488px','top': '152px', 'address': 6038, 'format': FormatSpecifier.F3_1},
    {'id': 'op5_MFCG4_PV', 'left': '488px','top': '224px', 'address': 6040, 'format': FormatSpecifier.F3_1},
    {'id': 'op5_MFCG5_PV', 'left': '488px','top': '296px', 'address': 6042, 'format': FormatSpecifier.F3_1},
    {'id': 'op5_MFCG6_PV', 'left': '488px','top': '368px', 'address': 6044, 'format': FormatSpecifier.F3_1},
    {'id': 'op5_MFCG7_PV', 'left': '488px','top': '440px', 'address': 6046, 'format': FormatSpecifier.F3_1},
]
ope5textbox_children_indicators = (
    monitor_data +
    setting_data
)

# マスフロー
def create_operation5_layout():
    """
    手動運転画面のモード5 (操作ボタンエリア) のレイアウト
    """
    layout = []

    # 1. テキスト (z-index: 5)
    for i,data in enumerate(text_data):
        # # 'left'と'top'の値からpxを除去し、オフセットを適用
        id = f'op5_text{i}'
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

    # 5. ダミーコンポーネント (テキストボックスのOutコールバック用)
    layout.append(
        html.Div(id='dummy-button-op5', style={'display': 'none'})
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
    create_setting_modal(layout, '-op5')
    
    return layout