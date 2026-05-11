import copy

from dash import html
from recipe_constans import (
    edit_step_num_format_data,
    edit_dev_format_data,
    edit_monitor_format_data,
    edit_textbox_format_data
)

from common_modal_layout import create_setting_modal
from recipe_manager import recipe_handler, generate_recipe_display_values
from tcp_client import tcp_client_handler

recipe_name_data = {
    'id': 'recipe_name1', 'left': '620px', 'top': '8px', 'text': 'レシピ名',
}

step_data = []
# フォーマットからコピーする (辞書のコピーはディープコピーが必要)
step_num_data = copy.deepcopy(edit_step_num_format_data)
recipe_dev_data = copy.deepcopy(edit_dev_format_data)
monitor_data = copy.deepcopy(edit_monitor_format_data)
textbox_data = copy.deepcopy(edit_textbox_format_data)

BASE_DEV_LEFT = 36
BASE_DEV_TOP = 120
# ラベルの座標の再割り当て
for i, item in enumerate(recipe_dev_data):
    item['id'] = f'reci4_num{i+1}_dev'
    item['left'] = f'{BASE_DEV_LEFT}px'
    item['top'] = f'{BASE_DEV_TOP + i*56}px'

BASE_PV_LEFT = 340
BASE_PV_TOP = 120
# ラベルの座標の再割り当て
for i, item in enumerate(monitor_data):
    item['id'] = f'reci4_num{i+1}_PV'
    item['left'] = f'{BASE_PV_LEFT}px'
    item['top'] = f'{BASE_PV_TOP + i*56}px'

BASE_SV_LEFT = 472
# ラベルの座標の再割り当て
for i, item in enumerate(textbox_data):
    item['id'] = f'reci4_num{i+1}_SV'
    item['trigger_id'] = f'reci4_num{i+1}_trigger'
    item['left'] = f'{BASE_SV_LEFT}px'
    item['top'] = f'{BASE_PV_TOP + i*56}px'

reci4_textbox_indicators = monitor_data + textbox_data

# さらに2ステップ分の辞書を作成
for i in range(2):
    # シャローコピーではなく、ディープコピーが必要
    step_data.append(copy.deepcopy(textbox_data))

BASE_STEP_LEFT = 620
RECIPE_DEV_SET_POINT = 1800
RECIPE_DEV_OFFSET = 100
# ラベルの座標の再割り当て
for k in range(len(step_data)):
    item_list = step_data[k]
    for i, item in enumerate(item_list):
        item['id'] = f'reci4_num{k+1}_{i+1}_step'
        item['trigger_id'] = f'reci4_num{k+1}_{i+1}_trigger'
        item['left'] = f'{BASE_STEP_LEFT + k*132}px'
        item['top'] = f'{BASE_PV_TOP + i*56}px'
        index = textbox_data[i]['address'] - 5000
        item['address'] = RECIPE_DEV_SET_POINT + (RECIPE_DEV_OFFSET * k) + index
        item['file'] = True # ファイルレジスタ
        item['step'] = k+18
        item['item_id'] = i

BASE_STEP_TOP = 80
step_num_data[:] = step_num_data[:2]
for i, item in enumerate(step_num_data):
    item['id'] = f'reci4_step_num{i+1}'
    item['left'] = f'{BASE_STEP_LEFT + i*132}px'
    item['top'] = f'{BASE_STEP_TOP}px'
    item['text'] = str(i+19)

BASE_NEXT_BUTTON_STYLE = {
    'position': 'absolute',
    'width': '64px', 'height': '64px',
    'padding': '0', 'border': 'none',
    'background': 'none', 'cursor': 'pointer',
    'zIndex': 5, 'display': 'inline-block'
}

NEWLINE = '<br>'
# DEFAULT_RECIPE_NUM = 0
def create_recipe_edit4_layout():
    layout = []

    # レシピのオフセットの更新
    recipe_handler.update_edit_step_offset(offset=18)

    # 1. レシピデータを取得
    # recipe_handler.edit_recipe_num = DEFAULT_RECIPE_NUM
    csv_recipe_data = recipe_handler.get_recipe_data()
    
    # 【共通関数を呼び出し、表示値を生成】
    display_values_list = generate_recipe_display_values(
        csv_recipe_data, 
        step_data, 
        textbox_data
    )
    
    # 2. 表示するDivコンポーネントを生成
    # display_values_list のインデックスを追跡するためのカウンター
    value_index = 0 
    
    for k in range(len(step_data)):
        item_list = step_data[k]
        
        for i, data in enumerate(item_list):
            
            # 共通関数で生成された表示値を取得
            if value_index < len(display_values_list):
                display_value = display_values_list[value_index]
            else:
                display_value = "ERROR" # 万が一のフォールバック
            
            value_index += 1 # 次の値へ

            # data はここで内側の辞書（例: item1_step1）となる
            top_value = int(data['top'].replace('px', '')) + 4
            className='recipe_setting-style clickable-setting'
            style = {
                'position': 'absolute',
                'left': data['left'],
                'top': f'{top_value}px',
                'zIndex': 5,
            }
            
            layout.append(html.Div(
                display_value, # 生成された表示値を使用
                id=data['id'], 
                n_clicks=0,
                className=className, 
                style=style
            ))

    # 1. テキスト (z-index: 5)
    for data in recipe_dev_data:
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

    layout.append(html.Div(
        recipe_name_data['text'],
        id=recipe_name_data['id'],
        style={
            'position': 'absolute',
            'left': recipe_name_data['left'],
            'top': recipe_name_data['top'],
            'width': '780px', 
            'fontSize': '20px',
            'textAlign': 'center',
            'fontWeight': 'bold',
            'color': 'black',
            'fontFamily': 'Meiryo UI',
            'zIndex': 16,
        }
    ))

    # ステップ番号
    for data in step_num_data:
        # # 'left'と'top'の値からpxを除去し、オフセットを適用
        left_val = int(data['left'].replace('px', ''))+54
        top_val = int(data['top'].replace('px', ''))
        
        style={
            'position': 'absolute',
            'left': f'{left_val}px',
            'top': f'{top_val}px',
            'width': '128x', 
            'fontSize': '20px',
            'textAlign': 'center', #何故か中央揃えにならない
            'color': 'black',
            'fontFamily': 'Meiryo UI',
            'zIndex': 5,
        }
        layout.append(html.Div(data['text'],id=data['id'], style=style))

    # 5. ダミーコンポーネント (テキストボックスのOutコールバック用)
    layout.append(
        html.Div(id='dummy-button-reci4', style={'display': 'none'})
    )

    # 6. モニター値 (z-index: 5)
    for data in monitor_data:
        # 'top'の文字列から数値を取り出し、計算する
        top_value = int(data['top'].replace('px', '')) + 4
        className='recipe_monitor-style' # CSSクラスを適用
        style = {
            'position': 'absolute',
            'left': data['left'],
            'top': f'{top_value}px',
            'zIndex': 5,
        }
        layout.append(html.Div(data['id'], id=data['id'], className=className, style=style))

    # 7. 設定値 (z-index: 5)
    for data in textbox_data:
        top_value = int(data['top'].replace('px', '')) + 4
        className='recipe_setting-style clickable-setting' # 新しいCSSクラスを追加
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
    
    

    # 表示のたびに、呼ばれます
    if csv_recipe_data and len(csv_recipe_data) > 0:
        # レシピデータ読み込みに成功している場合は、PLCデータを受信、照合を要求する
        tcp_client_handler.read_recipe_data()
    else:
        # レシピデータがない場合の処理 (例: ログ出力やエラーハンドリングなど)
        print("recipe_edit_layout: 編集対象のレシピデータが存在しません。")

    # 8. ポップアップ用のレイアウト
    create_setting_modal(layout, '-reci4')

    return layout