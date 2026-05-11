from dash import html, dcc

# 各コンテンツのレイアウトファイルをインポート
from manual_diagram1_layout import create_diagram1_layout
from manual_diagram2_layout import create_diagram2_layout
from manual_diagram3_layout import create_diagram3_layout

# 同様に、content-3 用のレイアウトファイルもインポート
from manual_operation1_layout import create_operation1_layout
from manual_operation2_layout import create_operation2_layout
from manual_operation3_layout import create_operation3_layout
from manual_operation4_layout import create_operation4_layout
from manual_operation5_layout import create_operation5_layout

# アラームリスト
from manual_alarm_layout import create_manual_alerm_layout

def create_manual_layout(page_number):

    manual_children1 = []
    if (page_number == 1) or (page_number == 2):
        manual_children1 = create_diagram1_layout()
    if page_number == 3:
        manual_children1 = create_diagram2_layout()
    if (page_number == 4) or (page_number == 5):
        manual_children1 = create_diagram3_layout()

    manual_children3 = []
    if page_number == 1:
        manual_children3 = create_operation1_layout()
    if page_number == 2:
        manual_children3 = create_operation2_layout()
    if page_number == 3:
        manual_children3 = create_operation3_layout()
    if page_number == 4:
        manual_children3 = create_operation4_layout()
    if page_number == 5:
        manual_children3 = create_operation5_layout()

    manual_layout = html.Div(className='manual-container', id='manual-container', children=[
        html.Div(className='manual-main-content', children=[
            # content-1: 切り替え用コンテナ
            html.Div(
                id='manual-content-1-container',
                className='manual-content-item content-1',
                style={'position': 'relative'},
                children=manual_children1
            ),
            
            # content-2: スイッチとアラーム情報 (固定)
            html.Div(className='manual-content-item content-2', style={'position': 'relative'}, children=[
                *create_manual_alerm_layout()
            ]),
            
            # content-3: 切り替え用コンテナ (高さは残りのスペースを自動で占める)
            html.Div(
                id='manual-content-3-container',
                className='manual-content-item content-3',
                style={'position': 'relative'},
                children=manual_children3
            )
        ])
    ])
    
    return manual_layout