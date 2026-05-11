from dash import html, dcc

# 各コンテンツのレイアウトファイルをインポート
from recipe_edit1_layout import create_recipe_edit1_layout
from recipe_edit2_layout import create_recipe_edit2_layout
from recipe_edit3_layout import create_recipe_edit3_layout
from recipe_edit4_layout import create_recipe_edit4_layout
from recipe_manager_layout import create_recipe_manager_layout

def create_recipe_layout(page_number):

    recipe_children = []
    if page_number == 1:
        recipe_children = create_recipe_edit1_layout()
    if page_number == 2:
        recipe_children = create_recipe_edit2_layout()
    if page_number == 3:
        recipe_children = create_recipe_edit3_layout()
    if page_number == 4:
        recipe_children = create_recipe_edit4_layout()



    layout = html.Div(className='recipe-container', id='recipe-container', children=[
        dcc.Store(id='recipe-sel-store', data={'selected_values': ''}),


        html.Div(className='recipe-main-content', children=[
            # content-1: 切り替え用コンテナ
            html.Div(
                id='recipe-content-1-container',
                className='recipe-content-item content-1',
                style={'position': 'relative'},
                children=recipe_children
            ),
            
            # content-2: レシピファイルの編集
            html.Div(className='recipe-content-item content-2', style={'position': 'relative'}, children=[
                *create_recipe_manager_layout()
            ])
        ])


    ])

    
    
    return layout