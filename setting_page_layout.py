from dash import html, dcc

# 各コンテンツのレイアウトファイルをインポート
from setting1_layout import create_setting1_layout
from setting2_layout import create_setting2_layout
from setting3_layout import create_setting3_layout

def create_setting_layout(page_number):

    setting_layout = []

    setting_children = []
    if page_number == 1:
        setting_children = create_setting1_layout()
    if page_number == 2:
        setting_children = create_setting2_layout()
    if page_number == 3:
        setting_children = create_setting3_layout()

    setting_layout = html.Div(className='setting-container', id='setting-container', children=[
        # 状態を保持するためのdcc.Store
        #dcc.Store(id='setting-mode-store', data={'current_mode': 1, 'max_mode': len(MODE_CONFIG_MAP)}),

        html.Div(className='setting-main-content', children=[
            # # content-1: スイッチ (固定)
            # html.Div(className='setting-content-item content-1', style={'position': 'relative'}, children=button_layout_list),
            # content-2: 切り替え用コンテナ
            html.Div(
                id='setting-content-2-container',
                className='setting-content-item content-2',
                style={'position': 'relative'},
                children=setting_children # 初期表示はモード1
            )
        ])
    ])
    
    return setting_layout