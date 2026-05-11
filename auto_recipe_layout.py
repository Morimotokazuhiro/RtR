from dash import html, dcc

from data_queue import data_queue_handler

# レシピデータを定義します。
recipe_name_data = {'id': 'recipe_name','left': '8px','top': '16px','width': '504px'}
recipe_bar_data = {'id': 'recipe_bar','left': '32px','top': '56px','width': '457px'}
recipe_step_data = {'id': 'recipe_step','left': '112px','top': '128px','width': '300px'}

# 機器名、現在値、設定値のデータを定義します。
# addressが一定間隔の割り当てでない為、個別に割り当てていく。
# 画面の表示される行数は、ここで指定する。コールバックの数に影響するので、「DEVICE_SIZE」を必ず参照すること。

recipe_dev_data = [
    {'id': 'recipe1', 'left': '8px', 'top': '200px', 'text': 'RFセットパワー'},
    {'id': 'recipe2', 'left': '8px', 'top': '200px', 'text': '温度設定'},
    {'id': 'recipe3', 'left': '8px', 'top': '200px', 'text': '温度設定'},
    {'id': 'recipe4', 'left': '8px', 'top': '200px', 'text': 'H2 マスフロー'},
    {'id': 'recipe5', 'left': '8px', 'top': '200px', 'text': 'CH4 マスフロー'},
    {'id': 'recipe6', 'left': '8px', 'top': '200px', 'text': 'O2 マスフロー'},
    {'id': 'recipe7', 'left': '8px', 'top': '200px', 'text': 'Ar マスフロー'},
    {'id': 'recipe8', 'left': '8px', 'top': '200px', 'text': 'N2 マスフロー'},
    {'id': 'recipe9', 'left': '8px', 'top': '200px', 'text': 'H2 マスフロー'},
    {'id': 'recipe10', 'left': '8px', 'top': '200px', 'text': 'Ar マスフロー'},
    {'id': 'recipe11', 'left': '8px', 'top': '200px', 'text': 'A室角度'},
    {'id': 'recipe12', 'left': '8px', 'top': '200px', 'text': 'B室角度'},
    {'id': 'recipe13', 'left': '8px', 'top': '200px', 'text': '開度調整'},
    {'id': 'recipe14', 'left': '8px', 'top': '200px', 'text': '圧力調整'},
    {'id': 'recipe15', 'left': '8px', 'top': '200px', 'text': 'フォイル搬送速度'},
    {'id': 'recipe16', 'left': '8px', 'top': '200px', 'text': 'テンション制御速度上限'},
    {'id': 'recipe17', 'left': '8px', 'top': '200px', 'text': 'テンション制御速度下限'},
    {'id': 'recipe18', 'left': '8px', 'top': '200px', 'text': 'フォイル搬送速度'},
    {'id': 'recipe19', 'left': '8px', 'top': '200px', 'text': 'テンション制御速度上限'},
    {'id': 'recipe20', 'left': '8px', 'top': '200px', 'text': 'テンション制御速度下限'},
    {'id': 'recipe21', 'left': '8px', 'top': '200px', 'text': '時間'},
    {'id': 'recipe22', 'left': '8px', 'top': '200px', 'text': '排気ステップ圧力'},
    {'id': 'recipe23', 'left': '8px', 'top': '200px', 'text': '排気・ステップ制御選択'},
    {'id': 'recipe24', 'left': '8px', 'top': '200px', 'text': 'A室回転方向'},
    {'id': 'recipe25', 'left': '8px', 'top': '200px', 'text': 'B室回転方向'},
    {'id': 'recipe26', 'left': '8px', 'top': '200px', 'text': 'A室テンションコントロール監視先'},
    {'id': 'recipe27', 'left': '8px', 'top': '200px', 'text': 'B室テンションコントロール監視先'},
    {'id': 'recipe28', 'left': '8px', 'top': '200px', 'text': '巻径演算'},
    {'id': 'recipe29', 'left': '8px', 'top': '200px', 'text': 'PGAS1 使用'},
    {'id': 'recipe30', 'left': '8px', 'top': '200px', 'text': 'PGAS2 使用'},
    {'id': 'recipe31', 'left': '8px', 'top': '200px', 'text': 'PGAS3 使用'},
    {'id': 'recipe32', 'left': '8px', 'top': '200px', 'text': 'PGAS4 使用'}
]
# TODO: アドレス0は仮です
recipe_cur_data = [
    {'id': 'recipe1', 'left': '240px', 'top': '200px', 'address': 6004},
    {'id': 'recipe2', 'left': '240px', 'top': '200px', 'address': 6020},
    {'id': 'recipe3', 'left': '240px', 'top': '200px', 'address': 6022},
    {'id': 'recipe4', 'left': '240px', 'top': '200px', 'address': 6034},
    {'id': 'recipe5', 'left': '240px', 'top': '200px', 'address': 6036},
    {'id': 'recipe6', 'left': '240px', 'top': '200px', 'address': 6038},
    {'id': 'recipe7', 'left': '240px', 'top': '200px', 'address': 6040},
    {'id': 'recipe8', 'left': '240px', 'top': '200px', 'address': 6042},
    {'id': 'recipe9', 'left': '240px', 'top': '200px', 'address': 6044},
    {'id': 'recipe10', 'left': '240px', 'top': '200px', 'address': 6046},
    {'id': 'recipe11', 'left': '240px', 'top': '200px', 'address': 6026},
    {'id': 'recipe12', 'left': '240px', 'top': '200px', 'address': 6028},
    {'id': 'recipe13', 'left': '240px', 'top': '200px', 'address': 6094},
    {'id': 'recipe14', 'left': '240px', 'top': '200px', 'address': 6002},
    {'id': 'recipe15', 'left': '240px', 'top': '200px', 'address': 6096},
    {'id': 'recipe16', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe17', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe18', 'left': '240px', 'top': '200px', 'address': 6104},
    {'id': 'recipe19', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe20', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe21', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe22', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe23', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe24', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe25', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe26', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe27', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe28', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe29', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe30', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe31', 'left': '240px', 'top': '200px', 'address': 0},
    {'id': 'recipe32', 'left': '240px', 'top': '200px', 'address': 0},
]

recipe_set_data = [
    # ここから2ワード
    {'id': 'recipe1', 'left': '380px', 'top': '200px', 'address': 5000,'data_index': 0},
    {'id': 'recipe2', 'left': '380px', 'top': '200px', 'address': 5002,'data_index': 1},
    {'id': 'recipe3', 'left': '380px', 'top': '200px', 'address': 5004,'data_index': 2},
    {'id': 'recipe4', 'left': '380px', 'top': '200px', 'address': 5006,'data_index': 3},
    {'id': 'recipe5', 'left': '380px', 'top': '200px', 'address': 5008,'data_index': 4},
    {'id': 'recipe6', 'left': '380px', 'top': '200px', 'address': 5010,'data_index': 5},
    {'id': 'recipe7', 'left': '380px', 'top': '200px', 'address': 5012,'data_index': 6},
    {'id': 'recipe8', 'left': '380px', 'top': '200px', 'address': 5014,'data_index': 7},
    {'id': 'recipe9', 'left': '380px', 'top': '200px', 'address': 5016,'data_index': 8},
    {'id': 'recipe10', 'left': '380px', 'top': '200px', 'address': 5018,'data_index': 9},
    {'id': 'recipe11', 'left': '380px', 'top': '200px', 'address': 5020,'data_index': 10},
    {'id': 'recipe12', 'left': '380px', 'top': '200px', 'address': 5022,'data_index': 11},
    {'id': 'recipe13', 'left': '380px', 'top': '200px', 'address': 5028,'data_index': 14},
    {'id': 'recipe14', 'left': '380px', 'top': '200px', 'address': 5030,'data_index': 15},
    {'id': 'recipe15', 'left': '380px', 'top': '200px', 'address': 5032,'data_index': 16},
    {'id': 'recipe16', 'left': '380px', 'top': '200px', 'address': 5038,'data_index': 19},
    {'id': 'recipe17', 'left': '380px', 'top': '200px', 'address': 5040,'data_index': 20},
    {'id': 'recipe18', 'left': '380px', 'top': '200px', 'address': 5042,'data_index': 21},
    {'id': 'recipe19', 'left': '380px', 'top': '200px', 'address': 5044,'data_index': 22},
    {'id': 'recipe20', 'left': '380px', 'top': '200px', 'address': 5046,'data_index': 23},
    {'id': 'recipe21', 'left': '380px', 'top': '200px', 'address': 5052,'data_index': 26},
    {'id': 'recipe22', 'left': '380px', 'top': '200px', 'address': 5054,'data_index': 27},
    # ここから1ワード
    {'id': 'recipe23', 'left': '380px', 'top': '200px', 'address': 5060,'data_index': 30},
    {'id': 'recipe24', 'left': '380px', 'top': '200px', 'address': 5061,'data_index': 31},
    {'id': 'recipe25', 'left': '380px', 'top': '200px', 'address': 5062,'data_index': 32},
    {'id': 'recipe26', 'left': '380px', 'top': '200px', 'address': 5063,'data_index': 33},
    {'id': 'recipe27', 'left': '380px', 'top': '200px', 'address': 5064,'data_index': 34},
    {'id': 'recipe28', 'left': '380px', 'top': '200px', 'address': 5065,'data_index': 35},
    {'id': 'recipe29', 'left': '380px', 'top': '200px', 'address': 5066,'data_index': 36},
    {'id': 'recipe30', 'left': '380px', 'top': '200px', 'address': 5067,'data_index': 37},
    {'id': 'recipe31', 'left': '380px', 'top': '200px', 'address': 5068,'data_index': 38},
    {'id': 'recipe32', 'left': '380px', 'top': '200px', 'address': 5069,'data_index': 39},
]

# DEVICE_SIZEは、各辞書のサイズ以下に設定して下さい。
DEVICE_SIZE = 32 # 仕様書や画面の表示領域を確認すること。
# y座標の再割り当て
TOP_BASE = 228
for i in range(DEVICE_SIZE):
    recipe_dev_data[i]['top'] = f'{i*36+TOP_BASE}px'
    recipe_cur_data[i]['top'] = f'{i*36+TOP_BASE}px'
    recipe_set_data[i]['top'] = f'{i*36+TOP_BASE}px'
    recipe_dev_data[i]['id'] = f'recipe_dev{i+1}'
    recipe_cur_data[i]['id'] = f'recipe_cur{i+1}'
    recipe_set_data[i]['id'] = f'recipe_set{i+1}'

recipe_data_ids = [recipe_name_data['id'], recipe_bar_data['id'], recipe_step_data['id']]
for data in recipe_dev_data[:DEVICE_SIZE]:
    recipe_data_ids.append(data['id'])
for data in recipe_cur_data[:DEVICE_SIZE]: # DEVICE_SIZEでスライス
    recipe_data_ids.append(data['id'])
for data in recipe_set_data[:DEVICE_SIZE]: # DEVICE_SIZEでスライス
    recipe_data_ids.append(data['id'])

base_style = {
        'font-family': 'Meiryo UI',
        'font-size': '18px',
        'position': 'absolute',
    }

# レイアウトを生成する関数
def create_recipe_layout():

    layout = []

    # 1. レシピ名
    layout.append(html.Div('レシピ名(仮)', id=recipe_name_data['id'], style={
        **base_style, 'left': recipe_name_data['left'], 'top': recipe_name_data['top'], 'width': recipe_name_data['width'],
        'text-align': 'center', 'font-weight': 'bold'
    }))

    # 2. 実行表示のバー
    # childrenプロパティが更新されるため、初期childrenはNoneにします
    layout.append(html.Div(id=recipe_bar_data['id'], style={
        **base_style, 'left': recipe_bar_data['left'], 'top': recipe_bar_data['top'], 'width': recipe_bar_data['width'],
        'height': '33px', 'border': '1px solid black'
    })),

    # 3. ステップ番号
    layout.append(html.Div('ステップ番号(仮)', id=recipe_step_data['id'], style={
        **base_style, 'left': recipe_step_data['left'], 'top': recipe_step_data['top'], 'width': recipe_step_data['width'],
        'text-align': 'center'
    })),

    # 4. ステップ切替スイッチ
    # 左矢印ボタン
    layout.append(html.Button(
        id='recipe_switch1',
        children=html.Div('＜', className='recipe-switch-button-icon'),
        n_clicks=0,
        className='recipe-switch-button',
        style={
            'position': 'absolute',
            'left': '16px',
            'top': '108px',
            'display': 'none'
        }
    ))
    # 右矢印ボタン
    layout.append(html.Button(
        id='recipe_switch2',
        children=html.Div('＞', className='recipe-switch-button-icon'),
        n_clicks=0,
        className='recipe-switch-button',
        style={
            'position': 'absolute',
            'left': '440px',
            'top': '108px',
            'display': 'none'
        }
    ))

    # 5. 機器名（項目）
    layout.append(html.Div('機器名称', id='device_item', style={
        **base_style, 'left': '8px', 'top': '188px', 'width': '210px', 'text-align': 'left',
        'font-weight': 'bold'}
    ))

    # 6. 現在値（項目）
    layout.append(html.Div('現在値', id='cur_item', style={
        **base_style, 'left': '240px', 'top': '188px', 'width': '126px', 'text-align': 'right',
        'font-weight': 'bold'}
    ))

    # 7. 設定値（項目）
    layout.append(html.Div('設定値', id='set_item', style={
        **base_style, 'left': '380px', 'top': '188px', 'width': '126px', 'text-align': 'right',
        'font-weight': 'bold'}
    ))

    # 8.機器名
    for data in recipe_dev_data[:DEVICE_SIZE]:
        style={
            **base_style, 'left': data['left'], 'top': data['top'], 'width': '240px',
            'text-align': 'left', 'color': '#000000'}
        layout.append(html.Div(data['id'], id=data['id'],style=style))
        
    # 9.現在値
    for data in recipe_cur_data[:DEVICE_SIZE]:
        style={
            **base_style, 'left': data['left'], 'top': data['top'], 'width': '126px',
            'text-align': 'right', 'color': 'orangered'}
        layout.append(html.Div(data['id'], id=data['id'],style=style))
        
    # 10.設定値
    for data in recipe_set_data[:DEVICE_SIZE]:
        style={
            **base_style, 'left': data['left'], 'top': data['top'], 'width': '126px',
            'text-align': 'right', 'color': 'deepskyblue'}
        layout.append(html.Div(data['id'], id=data['id'],style=style))
        
        # 11.グレーの線
    for i in range(DEVICE_SIZE):
        layout.append(html.Div(id=f'bar{i+1}',style={
            'position': 'absolute', 'left': '8px', 'top': f'{i*36 + 256}px', # 線の位置を調整
            'width': '501px', 'height': '1px', 'background-color': '#999999',
        }))

    return layout


class RecipeManager:
    # 現在ステップアドレス (自動画面レシピモニター用)
    STEP_ADDRESS = 4098

    def __init__(self):
        # インスタンス変数として定義し直す
        self.recipe_name = 'レシピ名'    # レシピ名
        self.recipe_bar = 0             # 実行状態表示のバー
        self.max_step = 20              # 最大のステップ番号
        self.running = False            # 運転中
        self.checking = False           # ステップ確認状態
        self.current_step = 1           # 実行中のステップ番号
        self.view_step = 1              # 表示中のステップ番号

    # 通常のインスタンスメソッドに戻す（@classmethodは不要）
    def update_view_step(self, countup):
        self.checking = True

        # あらかじめ、加算（減算）した結果を確認し、修正後に代入する
        new_step = self.view_step + countup
        
        if new_step < 1:
            new_step = 1
        elif new_step > self.max_step:
            new_step = self.max_step
        
        self.view_step = new_step

    # パラメータのアップデート
    def update_parameter(self):
        # 仮の内容です
        # 運転中の立ち上がり/立ち下がり時は、ステップ確認状態をリセット
        new_running = True # 仮
        if (new_running and (not self.running)) or ((not new_running) and self.running):
             self.checking = False
        self.running = new_running

        # 実行中のステップ番号
        self.current_step = data_queue_handler.get_word_device(self.STEP_ADDRESS)
        
        # ステップ確認状態でないなら、表示中のステップ番号は実行中のステップ番号に追従する
        if not self.checking:
            self.view_step = self.current_step

        # 実行状態表示のバーの更新
        if not self.running:
            self.recipe_bar = 0
        elif self.view_step == self.current_step:
            self.recipe_bar = 1
        elif self.view_step > self.current_step:
            self.recipe_bar = 2
        elif self.view_step < self.current_step:
            self.recipe_bar = 3

        # レシピ名の更新 (仮)
        self.recipe_name = 'レシピ名'    # レシピ名
    # 実行表示バー    
    def get_bar_style(self):
        if self.recipe_bar == 0:
            return {'background': 'linear-gradient(to right, transparent 0%, transparent 100%)'}
        elif self.recipe_bar == 1:
            return {'background': 'linear-gradient(to right, limegreen 0%, limegreen 100%)'}
        elif self.recipe_bar == 2:
            return {'background': 'linear-gradient(to right, limegreen, transparent)'}
        else:
            return {'background': 'linear-gradient(to right, transparent, limegreen)'}
    # ステップ番号
    def get_step_number(self):
        return f'ステップ:{self.current_step}/{self.max_step}'
        #return f'ステップ:{self.current_step}/{self.max_step} (表示中:{self.view_step})'

    def reset_status(self):
        # インスタンス変数をリセット
        self.checking = False
        self.current_step = 1
        self.view_step = 1
        print("RecipeManagerのステータスをリセットしました。")

    @property
    def device_size(self):
        return DEVICE_SIZE
    
    @property
    def device_datas(self):
        return recipe_dev_data
    
    @property
    def current_datas(self):
        return recipe_cur_data
    
    @property
    def setting_datas(self):
        return recipe_set_data

# 💡 このファイル内でインスタンス（共有オブジェクト）を生成
# これが「唯一の」共有されるハンドラとなる
recipe_handler = RecipeManager()

