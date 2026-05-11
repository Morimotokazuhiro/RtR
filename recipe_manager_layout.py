from dash import html
import dash_mantine_components as dmc
# レシピ用
from recipe_manager import recipe_handler
from constans import BASE_STYLES_MAP

recipe_data = [
    # テンプレ
    {"label": "レシピ1", "value": "reci_sel_file1"},
    {"label": "レシピ2", "value": "reci_sel_file2"},
    # childrenがないため、すべてのノードが単一のアイテムとして表示されます
]
# レシピ送信完了信号
sig_list = [
    {'id': 'reci_mana_fin', 'left': '200px', 'top': '48px', 'address': 3611, 'style_type': 'BASE_24px', 'name': '送信完了'},
]

def _add_device_name(layout, item_list, offset_x: int, offset_y: int, width: str, color: str, z_index: int):
    """
    機器名を描画するヘルパー関数。
    - offset_x/offset_y: 元の left/top からのオフセット (px)
    - width: テキストボックスの幅 (px, 'auto'など)
    """
    for item in item_list:
        # 'left'と'top'の値からpxを除去し、オフセットを適用
        left_val = int(item['left'].replace('px', '')) + offset_x
        top_val = int(item['top'].replace('px', '')) + offset_y
        
        layout.append(html.Div(
            item['name'],
            style={
                'position': 'absolute',
                'left': f'{left_val}px',
                'top': f'{top_val}px',
                'textAlign': 'left',
                'width': width,
                'fontSize': '24px',
                'fontWeight': 'bold',
                'color': item.get('name_color', color), # name_colorが定義されていればそれを使用、なければcolor
                'fontFamily': 'Meiryo UI',
                'zIndex': z_index,
            }
        ))

def create_recipe_manager_layout():
    layout = []

    # テスト用レシピ送信ボタン
    layout.append(html.Button(
        id='recipe-to-plc-button',
        children=html.Div('送信', className='recipe-switch-button-icon'),
        n_clicks=0,
        className='recipe-switch-button',
        style={
            'position': 'absolute',
            'left': '16px',
            'top': '32px',
        }
    ))

    # レシピ保存ボタン
    layout.append(html.Button(
        id='recipe-save-button',
        children=html.Div('保存', className='recipe-switch-button-icon'),
        n_clicks=0,
        className='recipe-switch-button',
        style={
            'position': 'absolute',
            'left': '96px',
            'top': '32px',
        }
    ))

    _add_device_name(layout, sig_list, offset_x=32, offset_y=-6, width='400px', color='black', z_index=8)

    # センサー、ポンプ等のマークの生成 
    for item in sig_list:        
        # 1. ベーススタイルを取得
        base_style = BASE_STYLES_MAP[item['style_type']].copy()
        
        # 2. 座標情報で上書き
        base_style['left'] = item['left']
        base_style['top'] = item['top']
        
        # 3. 初期色を設定 (例: 初期状態は灰色)
        base_style['backgroundColor'] = 'gray'
        
        # コンポーネントの初期スタイルとして設定
        layout.append(html.Div(id=item['id'], style=base_style))

    # # レシピ編集ボタン
    # layout.append(html.Button(
    #     id='recipe-edit-button',
    #     children=html.Div('編集＆読込', className='recipe-switch-button-icon'),
    #     n_clicks=0,
    #     className='recipe-switch-button',
    #     style={
    #         'position': 'absolute',
    #         'left': '176px',
    #         'top': '32px',
    #     }
    # ))

    # ダミーコンポーネント (操作ボタンのOutコールバック用)
    layout.append(
        html.Div(id='dummy-div-for-plc-write', style={'display': 'none'})
    )

    # # ini設定の内容を受け取る
    # setting, setting_list = recipe_handler.get_recipe_setting()
    # my_data = []

    # recipe_max = setting['recipemax']
    # if recipe_max >= 1:
    # # レシピリストデータを作成する
    #     for i in range(recipe_max):
    #         number = i + 1
    #         name = setting_list[i]['name']
    #         my_data.append({"label": name, "value": f'reci_sel_file{number}'})

    # recipe_data = my_data
    
    # layout.append(dmc.Container(
    # # コンテナ全体の幅を広げます
    # size="xl",
    # style={
    #     'position': 'absolute',  # 絶対位置指定を有効にする
    #     'left': '340px',         # 左端から340pxの位置
    #     'top': '32px',         # 上端から100pxの位置
    #     'width': '1048px',
    #     'backgroundColor': '#f0f0f0', # 視認性向上のため背景色を指定
    #     'padding': '10px',
    #     'border': '1px solid #ccc'
    # },
    # children=[
    #     # html.H1("dmc.Tree (ファイルリスト選択)", style={'marginBottom': '20px'}),
    #     #dmc.Divider(), # 横線

    #     # ----------------- 3. 2列表示レイアウト (dmc.Grid) -----------------
    #     dmc.Grid(
    #         #style={'marginTop': '0px'},
    #         gutter="xs",
    #         #mt="xs",


    #         children=[
    #             # ----------------- 左カラム: Treeview (ファイルリスト) -----------------
    #             dmc.GridCol(
    #                 span=4,  # グリッドシステムで全体の12分の4を使用 (約3分の1)
    #                 children=[
    #                     dmc.Card(
    #                         shadow="sm", padding="xs", radius="md", withBorder=True,
    #                         children=[
    #                             dmc.CardSection(
    #                                 dmc.Text("レシピ名", size="lg", style={'paddingY': '4px'}),#'padding': '10px'}),
    #                                 withBorder=True,
    #                                 inheritPadding=True,
    #                             ),
    #                             # **文字サイズを大きくする** (styleプロパティを使用)
    #                             dmc.Tree(
    #                                 id="file-tree",
    #                                 data=recipe_data,
    #                                 selectOnClick=True,  # ノードを選択可能にする
    #                                 expandOnClick=False, # ノードを選択しても自動展開しない
    #                                 style={
    #                                     'fontSize': '20px',  # 文字サイズを大きくする
    #                                     'padding': '10px'
    #                                 }
    #                             ),
    #                         ]
    #                     )
    #                 ]
    #             ),

    #             # ----------------- 右カラム: 選択された情報表示 -----------------
    #             dmc.GridCol(
    #                 span=8,  # グリッドシステムで全体の12分の8を使用 (約3分の2)
    #                 children=[
    #                     dmc.Card(
    #                         shadow="sm",
    #                         padding="xs",
    #                         radius="md",
    #                         withBorder=True,
    #                         children=[
    #                             dmc.CardSection(
    #                                 dmc.Text("information", size="lg", style={'paddingY': '4px'}),
    #                                 withBorder=True,
    #                                 inheritPadding=True,
    #                             ),
    #                             html.Div([
    #                                 dmc.Text("ファイル名:", size="md",),
    #                                 dmc.Text(id="selected-node-id", children="（何も選択されていません）", size="lg", c="blue"),
    #                                 dmc.Space(h=20),
    #                                 dmc.Text("💡 dmc.Treeのデータには、ファイルリストのパスやURLなどの情報を埋め込むことができます。", size="sm", c="dimmed")
    #                             ], style={'padding': '10px'})
    #                         ]
    #                     )
    #                 ]
    #             )
    #         ]
    #     )
    # ]))

    return layout