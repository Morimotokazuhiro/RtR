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
    {'left': '36px', 'top': '8px', 'text': 'SVM4'+NEWLINE+'フォイル搬送'},
    {'left': '36px', 'top': '96px', 'text': '回転方向'},
    {'left': '36px', 'top': '168px', 'text': '巻取径演算'},
    {'left': '36px', 'top': '240px', 'text': 'テンション制御'},
    {'left': '36px', 'top': '368px', 'text': 'EC2'+NEWLINE+'B室角度'},
    {'left': '36px', 'top': '440px', 'text': 'LAMP2'+NEWLINE+'厚み測定値ゼロ点'},
    {'left': '36px', 'top': '512px', 'text': 'SVM4'+NEWLINE+'オートチューニング'},
    {'left': '36px', 'top': '584px', 'text': 'SVM2'+NEWLINE+'オートチューニング'},
    
    # 左の列設定
    {'left': '420px', 'top': '8px', 'text': '速度'+NEWLINE+'(cm/min)'},
    {'left': '420px', 'top': '80px', 'text': '加速時間'+NEWLINE+'(sec)'},
    {'left': '420px', 'top': '152px', 'text': '減速時間'+NEWLINE+'(sec)'},
    {'left': '420px', 'top': '224px', 'text': '速度上限'+NEWLINE+'(cm/min)'},
    {'left': '420px', 'top': '296px', 'text': '速度下限'+NEWLINE+'(cm/min)'},
    {'left': '420px', 'top': '368px', 'text': '角度'+NEWLINE+'(° )'},

    # 右の列
    {'left': '756px', 'top': '8px', 'text': 'SVM3'+NEWLINE+'フォイル搬送'},
    {'left': '756px', 'top': '96px', 'text': '回転方向'},
    {'left': '756px', 'top': '168px', 'text': '巻取径演算'},
    {'left': '756px', 'top': '240px', 'text': 'テンション制御'},
    {'left': '756px', 'top': '368px', 'text': 'EC1'+NEWLINE+'A室角度'},
    {'left': '756px', 'top': '440px', 'text': 'LAMP1'+NEWLINE+'厚み測定値ゼロ点'},
    {'left': '756px', 'top': '512px', 'text': 'SVM3'+NEWLINE+'オートチューニング'},    
    
    # 右の列設定
    {'left': '1140px', 'top': '8px', 'text': '速度'+NEWLINE+'(cm/min)'},
    {'left': '1140px', 'top': '80px', 'text': '加速時間'+NEWLINE+'(sec)'},
    {'left': '1140px', 'top': '152px', 'text': '減速時間'+NEWLINE+'(sec)'},
    {'left': '1140px', 'top': '224px', 'text': '速度上限'+NEWLINE+'(cm/min)'},
    {'left': '1140px', 'top': '296px', 'text': '速度下限'+NEWLINE+'(cm/min)'},
    {'left': '1140px', 'top': '368px', 'text': '角度'+NEWLINE+'(° )'},
]
# --------------------------------------------------------
# ボタンのリスト
# コールバックで'src'を変更し、押下時のアドレス参照にも使います
# --------------------------------------------------------
lp_button_data = [
    # 左の列
    {'id': 'op3_SVM4_run_1', 'img_id': 'op3_SVM4_run_img1', 'left': '204px','top': '8px', 'sw_address': 3075, 'address': 875, 'type':'ON', 'name':'回転', 'reverse': False},
    {'id': 'op3_SVM4_run_2', 'img_id': 'op3_SVM4_run_img2', 'left': '316px','top': '8px', 'sw_address': 3275, 'address': 875, 'type':'OFF', 'name':'停止', 'reverse': True},

    {'id': 'op3_SVM4_rot_1', 'img_id': 'op3_SVM4_rot_img1', 'left': '204px','top': '80px', 'sw_address': 3076, 'address': 876, 'type':'ON', 'name':'正転', 'reverse': False},
    {'id': 'op3_SVM4_rot_2', 'img_id': 'op3_SVM4_rot_img2', 'left': '316px','top': '80px', 'sw_address': 3276, 'address': 876, 'type':'OFF', 'name':'逆転', 'reverse': True},

    {'id': 'op3_SVM4_kei_1', 'img_id': 'op3_SVM4_kei_img1', 'left': '204px','top': '152px', 'sw_address': 3077, 'address': 877, 'type':'ON', 'name':'有効', 'reverse': False},
    {'id': 'op3_SVM4_kei_2', 'img_id': 'op3_SVM4_kei_img2', 'left': '316px','top': '152px', 'sw_address': 3277, 'address': 877, 'type':'OFF', 'name':'無効', 'reverse': True},
    
    {'id': 'op3_SVM4_con_1', 'img_id': 'op3_SVM4_con_img1', 'left': '204px','top': '224px', 'sw_address': 3078, 'address': 878, 'type':'ON', 'name':'有効', 'reverse': False},
    {'id': 'op3_SVM4_con_2', 'img_id': 'op3_SVM4_con_img2', 'left': '316px','top': '224px', 'sw_address': 3278, 'address': 878, 'type':'OFF', 'name':'無効', 'reverse': True},

    {'id': 'op3_LAMP2_zero_1', 'img_id': 'op3_LAMP2_zero_img1', 'left': '204px','top': '440px', 'sw_address': 3082, 'address': 882, 'type':'ON', 'name':'ON', 'reverse': False},

    {'id': 'op3_SVM4_tun_1', 'img_id': 'op3_SVM4_tun_img1', 'left': '204px','top': '512px', 'sw_address': 3087, 'address': 887, 'type':'ON', 'name':'有効', 'reverse': False},
    {'id': 'op3_SVM4_tun_2', 'img_id': 'op3_SVM4_tun_img2', 'left': '316px','top': '512px', 'sw_address': 3287, 'address': 887, 'type':'OFF', 'name':'無効', 'reverse': True},

    {'id': 'op3_SVM2_tun_1', 'img_id': 'op3_SVM2_tun_img1', 'left': '204px','top': '584px', 'sw_address': 3089, 'address': 889, 'type':'ON', 'name':'有効', 'reverse': False},
    {'id': 'op3_SVM2_tun_2', 'img_id': 'op3_SVM2_tun_img2', 'left': '316px','top': '584px', 'sw_address': 3289, 'address': 889, 'type':'OFF', 'name':'無効', 'reverse': True},

    # 右の列
    {'id': 'op3_SVM3_run_1', 'img_id': 'op3_SVM3_run_img1', 'left': '924px','top': '8px', 'sw_address': 3071, 'address': 871, 'type':'ON', 'name':'回転', 'reverse': False},
    {'id': 'op3_SVM3_run_2', 'img_id': 'op3_SVM3_run_img2', 'left': '1036px','top': '8px', 'sw_address': 3271, 'address': 871, 'type':'OFF', 'name':'停止', 'reverse': True},

    {'id': 'op3_SVM3_rot_1', 'img_id': 'op3_SVM3_rot_img1', 'left': '924px','top': '80px', 'sw_address': 3072, 'address': 872, 'type':'ON', 'name':'正転', 'reverse': False},
    {'id': 'op3_SVM3_rot_2', 'img_id': 'op3_SVM3_rot_img2', 'left': '1036px','top': '80px', 'sw_address': 3272, 'address': 872, 'type':'OFF', 'name':'逆転', 'reverse': True},

    {'id': 'op3_SVM3_kei_1', 'img_id': 'op3_SVM3_kei_img1', 'left': '924px','top': '152px', 'sw_address': 3073, 'address': 873, 'type':'ON', 'name':'有効', 'reverse': False},
    {'id': 'op3_SVM3_kei_2', 'img_id': 'op3_SVM3_kei_img2', 'left': '1036px','top': '152px', 'sw_address': 3273, 'address': 873, 'type':'OFF', 'name':'無効', 'reverse': True},
    
    {'id': 'op3_SVM3_con_1', 'img_id': 'op3_SVM3_con_img1', 'left': '924px','top': '224px', 'sw_address': 3074, 'address': 874, 'type':'ON', 'name':'有効', 'reverse': False},
    {'id': 'op3_SVM3_con_2', 'img_id': 'op3_SVM3_con_img2', 'left': '1036px','top': '224px', 'sw_address': 3274, 'address': 874, 'type':'OFF', 'name':'無効', 'reverse': True},

    {'id': 'op3_LAMP1_zero_1', 'img_id': 'op3_LAMP1_zero_img1', 'left': '924px','top': '440px', 'sw_address': 3081, 'address': 881, 'type':'ON', 'name':'ON', 'reverse': False},

    {'id': 'op3_SVM3_tun_1', 'img_id': 'op3_SVM3_tun_img1', 'left': '924px','top': '512px', 'sw_address': 3086, 'address': 886, 'type':'ON', 'name':'有効', 'reverse': False},
    {'id': 'op3_SVM3_tun_2', 'img_id': 'op3_SVM3_tun_img2', 'left': '1036px','top': '512px', 'sw_address': 3286, 'address': 886, 'type':'OFF', 'name':'無効', 'reverse': True},
]
# --------------------------------------------------------
# モニターと設定の入力ボックスのリスト
# コールバックで'children'を変更します
# --------------------------------------------------------
setting_data = [
    {'id': 'op3_SMV4_spd_SV', 'left': '536px','top': '8px', 'address': 4042, 'data_index': 21,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op3_SMV4_spd_trigger',
        'name': 'SMV4 搬送速度', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op3_SMV4_acc_SV', 'left': '536px','top': '80px', 'address': 4044, 'data_index': 22,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op3_SMV4_acc_trigger',
        'name': 'SMV4 加速時間', 'min_value': 0.0, 'max_value': 10.0},
    {'id': 'op3_SMV4_dec_SV', 'left': '536px','top': '152px', 'address': 4046, 'data_index': 23,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op3_SMV4_dec_trigger',
        'name': 'SMV4 減速時間', 'min_value': 0.0, 'max_value': 10.0},
    {'id': 'op3_SMV4_upp_SV', 'left': '536px','top': '224px', 'address': 4048, 'data_index': 24,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op3_SMV4_upp_trigger',
        'name': 'SMV4 速度上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op3_SMV4_low_SV', 'left': '536px','top': '296px', 'address': 4050, 'data_index': 25,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op3_SMV4_low_trigger',
        'name': 'SMV4 速度下限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op3_EC2_dg_SV', 'left': '536px','top': '368px', 'address': 4022, 'data_index': 11,
        'format': FormatSpecifier.F3_2, 'trigger_id': 'op3_EC2_dg_trigger',
        'name': 'EC2 角度', 'min_value': 0.0, 'max_value': 360.0},

    {'id': 'op3_SMV3_spd_SV', 'left': '1256px','top': '8px', 'address': 4032, 'data_index': 16,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op3_SMV3_spd_trigger',
        'name': 'SMV3 搬送速度', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op3_SMV3_acc_SV', 'left': '1256px','top': '80px', 'address': 4034, 'data_index': 17,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op3_SMV3_acc_trigger',
        'name': 'SMV3 加速時間', 'min_value': 0.0, 'max_value': 10.0},
    {'id': 'op3_SMV3_dec_SV', 'left': '1256px','top': '152px', 'address': 4036, 'data_index': 18,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op3_SMV3_dec_trigger',
        'name': 'SMV3 減速時間', 'min_value': 0.0, 'max_value': 10.0},
    {'id': 'op3_SMV3_upp_SV', 'left': '1256px','top': '224px', 'address': 4038, 'data_index': 19,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op3_SMV3_upp_trigger',
        'name': 'SMV3 速度上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op3_SMV3_low_SV', 'left': '1256px','top': '296px', 'address': 4040, 'data_index': 20,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'op3_SMV3_low_trigger',
        'name': 'SMV3 速度下限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'op3_EC1_dg_SV', 'left': '1256px','top': '368px', 'address': 4020, 'data_index': 10,
        'format': FormatSpecifier.F3_2, 'trigger_id': 'op3_EC1_dg_trigger',
        'name': 'EC1 角度', 'min_value': 0.0, 'max_value': 360.0},
]
# インターロックランプ
lamp_data = [
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
            'width': '108px', 'height': '64px',
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

def create_operation3_layout():
    """
    手動運転画面のモード3 (操作ボタンエリア) のレイアウト
    """
    layout = []

    # 1. テキスト (z-index: 5)
    for i,data in enumerate(text_data):
        # # 'left'と'top'の値からpxを除去し、オフセットを適用
        id = f'op3_text{i}'
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
    # _add_button(layout, button_data[0], '/assets/images/PlasticRect_G.png')
    # _add_button(layout, button_data[1], '/assets/images/PlasticRect_R.png')
    # _add_button(layout, button_data[2], '/assets/images/PlasticRect_G.png')
    
    # 4. インターロックランプの追加
    # for data in lamp_data:
    #     _add_lamp(layout, data)

    # 5. ダミーコンポーネント (操作ボタンのOutコールバック用)
    layout.append(
        html.Div(id='dummy-button-op3', style={'display': 'none'})
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
    create_setting_modal(layout, '-op3')
    
    return layout