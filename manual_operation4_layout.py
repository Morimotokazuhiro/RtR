from dash import html

# --------------------------------------------------------
# テキストとアドレスのリスト
# --------------------------------------------------------
# 改行文字コード（自由に変更可）
NEWLINE = '<br>'
text_data = [
    # 左の列
    {'left': '36px', 'top': '100px', 'text': 'N2AP0/BP0'+NEWLINE+'N2パージ一次'},
    {'left': '36px', 'top': '100px', 'text': 'N2AP1/BP1'+NEWLINE+'N2パージ二次'},
    {'left': '36px', 'top': '100px', 'text': 'N2BP2'+NEWLINE+'N2パージ三次'},
    {'left': '36px', 'top': '100px', 'text': 'N2CP2'+NEWLINE+'N2パージ三次'},
    {'left': '36px', 'top': '100px', 'text': 'N2DP2'+NEWLINE+'N2パージ三次'},
    {'left': '36px', 'top': '100px', 'text': 'G1~G5P0'+NEWLINE+'プロセスガス一次'},    
    {'left': '36px', 'top': '100px', 'text': 'G6P1'+NEWLINE+'H2ガス二次'},
    {'left': '36px', 'top': '100px', 'text': 'G6P2'+NEWLINE+'H2ガス三次'},
    {'left': '36px', 'top': '100px', 'text': 'G1P1'+NEWLINE+'H2ガス二次'},
    {'left': '36px', 'top': '100px', 'text': 'G1P2'+NEWLINE+'H2ガス三次'},
    # 真ん中の列
    {'left': '496px', 'top': '100px', 'text': 'G2P1'+NEWLINE+'CH4ガス二次'},
    {'left': '496px', 'top': '100px', 'text': 'G2P2'+NEWLINE+'CH4ガス三次'},
    {'left': '496px', 'top': '100px', 'text': 'G3P1'+NEWLINE+'O2ガス二次'},
    {'left': '496px', 'top': '100px', 'text': 'G3P2'+NEWLINE+'O2ガス三次'},
    {'left': '496px', 'top': '100px', 'text': 'G7P1'+NEWLINE+'Arガス二次'},
    {'left': '496px', 'top': '100px', 'text': 'G7P2'+NEWLINE+'Arガス三次'},
    {'left': '496px', 'top': '100px', 'text': 'G4P1'+NEWLINE+'Arガス二次'},
    {'left': '496px', 'top': '100px', 'text': 'G4P2'+NEWLINE+'Arガス三次'},
    {'left': '496px', 'top': '100px', 'text': 'G5P1'+NEWLINE+'N2ガス二次'},
    {'left': '496px', 'top': '100px', 'text': 'G5P2'+NEWLINE+'N2ガス三次'},
    # 右の列
    {'left': '956px', 'top': '100px', 'text': 'G6P3'+NEWLINE+'G6：N2パージ'},
    {'left': '956px', 'top': '100px', 'text': 'G1P3'+NEWLINE+'G1：N2パージ'},
    {'left': '956px', 'top': '100px', 'text': 'G2P3'+NEWLINE+'G2：N2パージ'},
    {'left': '956px', 'top': '100px', 'text': 'G3P3'+NEWLINE+'G3：N2パージ'},
    {'left': '956px', 'top': '100px', 'text': 'G7P3'+NEWLINE+'G7：N2パージ'},
    {'left': '956px', 'top': '100px', 'text': 'G4P3'+NEWLINE+'G4：N2パージ'},
    {'left': '956px', 'top': '100px', 'text': 'G5P3'+NEWLINE+'G5：N2パージ'}
]
# --------------------------------------------------------
# ボタンのリスト
# コールバックで'src'を変更し、押下時のアドレス参照にも使います
# --------------------------------------------------------
button_data = [
    # 左の列 ONスイッチ
    {'id': 'op4_AP0_1', 'img_id': 'op4_AP0_img1', 'left': '204px','top': '100px', 'sw_address': 3049, 'address': 849, 'type':'ON', 'reverse': False},
    {'id': 'op4_AP1_1', 'img_id': 'op4_AP1_img1','left': '204px','top': '100px', 'sw_address': 3035, 'address': 835, 'type':'ON', 'reverse': False},
    {'id': 'op4_BP2_1', 'img_id': 'op4_BP2_img1','left': '204px','top': '100px', 'sw_address': 3034, 'address': 834, 'type':'ON', 'reverse': False},
    {'id': 'op4_CP2_1', 'img_id': 'op4_CP2_img1','left': '204px','top': '100px', 'sw_address': 3058, 'address': 858, 'type':'ON', 'reverse': False},
    {'id': 'op4_DP2_1', 'img_id': 'op4_DP2_img1','left': '204px','top': '100px', 'sw_address': 3059, 'address': 859, 'type':'ON', 'reverse': False},
    {'id': 'op4_G1P0_1', 'img_id': 'op4_G1P0_img1','left': '204px','top': '100px', 'sw_address': 3048, 'address': 848, 'type':'ON', 'reverse': False},
    {'id': 'op4_G6P1_1', 'img_id': 'op4_G6P1_img1','left': '204px','top': '100px', 'sw_address': 3050, 'address': 850, 'type':'ON', 'reverse': False},
    {'id': 'op4_G6P2_1', 'img_id': 'op4_G6P2_img1','left': '204px','top': '100px', 'sw_address': 3028, 'address': 828, 'type':'ON', 'reverse': False},
    {'id': 'op4_G1P1_1', 'img_id': 'op4_G1P1_img1','left': '204px','top': '100px', 'sw_address': 3051, 'address': 851, 'type':'ON', 'reverse': False},
    {'id': 'op4_G1P2_1', 'img_id': 'op4_G1P2_img1','left': '204px','top': '100px', 'sw_address': 3027, 'address': 827, 'type':'ON', 'reverse': False},
    # 左の列 OFFスイッチ
    {'id': 'op4_AP0_2', 'img_id': 'op4_AP0_img2','left': '336px','top': '100px', 'sw_address': 3249, 'address': 849, 'type':'OFF', 'reverse': True},
    {'id': 'op4_AP1_2', 'img_id': 'op4_AP1_img2','left': '336px','top': '100px', 'sw_address': 3235, 'address': 835, 'type':'OFF', 'reverse': True},
    {'id': 'op4_BP2_2', 'img_id': 'op4_BP2_img2','left': '336px','top': '100px', 'sw_address': 3234, 'address': 834, 'type':'OFF', 'reverse': True},
    {'id': 'op4_CP2_2', 'img_id': 'op4_CP2_img2','left': '336px','top': '100px', 'sw_address': 3258, 'address': 858, 'type':'OFF', 'reverse': True},
    {'id': 'op4_DP2_2', 'img_id': 'op4_DP2_img2','left': '336px','top': '100px', 'sw_address': 3259, 'address': 859, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G1P0_2', 'img_id': 'op4_G1P0_img2','left': '336px','top': '100px', 'sw_address': 3248, 'address': 848, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G6P1_2', 'img_id': 'op4_G6P1_img2','left': '336px','top': '100px', 'sw_address': 3250, 'address': 850, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G6P2_2', 'img_id': 'op4_G6P2_img2','left': '336px','top': '100px', 'sw_address': 3228, 'address': 828, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G1P1_2', 'img_id': 'op4_G1P1_img2','left': '336px','top': '100px', 'sw_address': 3251, 'address': 851, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G1P2_2', 'img_id': 'op4_G1P2_img2','left': '336px','top': '100px', 'sw_address': 3227, 'address': 827, 'type':'OFF', 'reverse': True},
    # 真ん中の列 ONスイッチ
    {'id': 'op4_G2P1_1', 'img_id': 'op4_G2P1_img1','left': '664px','top': '100px', 'sw_address': 3052, 'address': 852, 'type':'ON', 'reverse': False},
    {'id': 'op4_G2P2_1', 'img_id': 'op4_G2P2_img1','left': '664px','top': '100px', 'sw_address': 3038, 'address': 838, 'type':'ON', 'reverse': False},
    {'id': 'op4_G3P1_1', 'img_id': 'op4_G3P1_img1','left': '664px','top': '100px', 'sw_address': 3053, 'address': 853, 'type':'ON', 'reverse': False},
    {'id': 'op4_G3P2_1', 'img_id': 'op4_G3P2_img1','left': '664px','top': '100px', 'sw_address': 3040, 'address': 840, 'type':'ON', 'reverse': False},
    {'id': 'op4_G7P1_1', 'img_id': 'op4_G7P1_img1','left': '664px','top': '100px', 'sw_address': 3054, 'address': 854, 'type':'ON', 'reverse': False},
    {'id': 'op4_G7P2_1', 'img_id': 'op4_G7P2_img1','left': '664px','top': '100px', 'sw_address': 3042, 'address': 842, 'type':'ON', 'reverse': False},
    {'id': 'op4_G4P1_1', 'img_id': 'op4_G4P1_img1','left': '664px','top': '100px', 'sw_address': 3055, 'address': 855, 'type':'ON', 'reverse': False},
    {'id': 'op4_G4P2_1', 'img_id': 'op4_G4P2_img1','left': '664px','top': '100px', 'sw_address': 3044, 'address': 844, 'type':'ON', 'reverse': False},
    {'id': 'op4_G5P1_1', 'img_id': 'op4_G5P1_img1','left': '664px','top': '100px', 'sw_address': 3056, 'address': 856, 'type':'ON', 'reverse': False},
    {'id': 'op4_G5P2_1', 'img_id': 'op4_G5P2_img1','left': '664px','top': '100px', 'sw_address': 3046, 'address': 846, 'type':'ON', 'reverse': False},
    # 真ん中の列 OFFスイッチ
    {'id': 'op4_G2P1_2', 'img_id': 'op4_G2P1_img2','left': '796px','top': '100px', 'sw_address': 3252, 'address': 852, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G2P2_2', 'img_id': 'op4_G2P2_img2','left': '796px','top': '100px', 'sw_address': 3238, 'address': 838, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G3P1_2', 'img_id': 'op4_G3P1_img2','left': '796px','top': '100px', 'sw_address': 3253, 'address': 853, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G3P2_2', 'img_id': 'op4_G3P2_img2','left': '796px','top': '100px', 'sw_address': 3240, 'address': 840, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G7P1_2', 'img_id': 'op4_G7P1_img2','left': '796px','top': '100px', 'sw_address': 3254, 'address': 854, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G7P2_2', 'img_id': 'op4_G7P2_img2','left': '796px','top': '100px', 'sw_address': 3242, 'address': 842, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G4P1_2', 'img_id': 'op4_G4P1_img2','left': '796px','top': '100px', 'sw_address': 3255, 'address': 855, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G4P2_2', 'img_id': 'op4_G4P2_img2','left': '796px','top': '100px', 'sw_address': 3244, 'address': 844, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G5P1_2', 'img_id': 'op4_G5P1_img2','left': '796px','top': '100px', 'sw_address': 3256, 'address': 856, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G5P2_2', 'img_id': 'op4_G5P2_img2','left': '796px','top': '100px', 'sw_address': 3246, 'address': 846, 'type':'OFF', 'reverse': True},
    # 右の列 ONスイッチ
    {'id': 'op4_G6P3_1', 'img_id': 'op4_G6P3_img1','left': '1124px','top': '100px', 'sw_address': 3036, 'address': 836, 'type':'ON', 'reverse': False},
    {'id': 'op4_G1P3_1', 'img_id': 'op4_G1P3_img1','left': '1124px','top': '100px', 'sw_address': 3037, 'address': 837, 'type':'ON', 'reverse': False},
    {'id': 'op4_G2P3_1', 'img_id': 'op4_G2P3_img1','left': '1124px','top': '100px', 'sw_address': 3039, 'address': 839, 'type':'ON', 'reverse': False},
    {'id': 'op4_G3P3_1', 'img_id': 'op4_G3P3_img1','left': '1124px','top': '100px', 'sw_address': 3041, 'address': 841, 'type':'ON', 'reverse': False},
    {'id': 'op4_G7P3_1', 'img_id': 'op4_G7P3_img1','left': '1124px','top': '100px', 'sw_address': 3043, 'address': 843, 'type':'ON', 'reverse': False},
    {'id': 'op4_G4P3_1', 'img_id': 'op4_G4P3_img1','left': '1124px','top': '100px', 'sw_address': 3045, 'address': 845, 'type':'ON', 'reverse': False},
    {'id': 'op4_G5P3_1', 'img_id': 'op4_G5P3_img1','left': '1124px','top': '100px', 'sw_address': 3047, 'address': 847, 'type':'ON', 'reverse': False},
    # 右の列 OFFスイッチ
    {'id': 'op4_G6P3_2', 'img_id': 'op4_G6P3_img2','left': '1256px','top': '100px', 'sw_address': 3236, 'address': 836, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G1P3_2', 'img_id': 'op4_G1P3_img2','left': '1256px','top': '100px', 'sw_address': 3237, 'address': 837, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G2P3_2', 'img_id': 'op4_G2P3_img2','left': '1256px','top': '100px', 'sw_address': 3239, 'address': 839, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G3P3_2', 'img_id': 'op4_G3P3_img2','left': '1256px','top': '100px', 'sw_address': 3241, 'address': 841, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G7P3_2', 'img_id': 'op4_G7P3_img2','left': '1256px','top': '100px', 'sw_address': 3243, 'address': 843, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G4P3_2', 'img_id': 'op4_G4P3_img2','left': '1256px','top': '100px', 'sw_address': 3245, 'address': 845, 'type':'OFF', 'reverse': True},
    {'id': 'op4_G5P3_2', 'img_id': 'op4_G5P3_img2','left': '1256px','top': '100px', 'sw_address': 3247, 'address': 847, 'type':'OFF', 'reverse': True},
]

# インターロックランプ
lamp_data = [
    # 左の列 ランプ
    {'id': 'op4_AP0LP_1', 'img_id': 'op4_AP0LP_img1', 'left': '176px','top': '100px', 'address': 3449},
    {'id': 'op4_AP1LP_1', 'img_id': 'op4_AP1LP_img1','left': '176px','top': '100px', 'address': 3435},
    {'id': 'op4_BP2LP_1', 'img_id': 'op4_BP2LP_img1','left': '176px','top': '100px', 'address': 3434},
    {'id': 'op4_CP2LP_1', 'img_id': 'op4_CP2LP_img1','left': '176px','top': '100px', 'address': 3458},
    {'id': 'op4_DP2LP_1', 'img_id': 'op4_DP2LP_img1','left': '176px','top': '100px', 'address': 3459},
    {'id': 'op4_G1P0LP_1', 'img_id': 'op4_G1P0LP_img1','left': '176px','top': '100px', 'address': 3448},
    {'id': 'op4_G6P1LP_1', 'img_id': 'op4_G6P1LP_img1','left': '176px','top': '100px', 'address': 3450},
    {'id': 'op4_G6P2LP_1', 'img_id': 'op4_G6P2LP_img1','left': '176px','top': '100px', 'address': 3428},
    {'id': 'op4_G1P1LP_1', 'img_id': 'op4_G1P1LP_img1','left': '176px','top': '100px', 'address': 3451},
    {'id': 'op4_G1P2LP_1', 'img_id': 'op4_G1P2LP_img1','left': '176px','top': '100px', 'address': 3427},
    # 真ん中の列 ランプ
    {'id': 'op4_G2P1LP_1', 'img_id': 'op4_G2P1LP_img1','left': '636px','top': '100px', 'address': 3452},
    {'id': 'op4_G2P2LP_1', 'img_id': 'op4_G2P2LP_img1','left': '636px','top': '100px', 'address': 3438},
    {'id': 'op4_G3P1LP_1', 'img_id': 'op4_G3P1LP_img1','left': '636px','top': '100px', 'address': 3453},
    {'id': 'op4_G3P2LP_1', 'img_id': 'op4_G3P2LP_img1','left': '636px','top': '100px', 'address': 3440},
    {'id': 'op4_G7P1LP_1', 'img_id': 'op4_G7P1LP_img1','left': '636px','top': '100px', 'address': 3454},
    {'id': 'op4_G7P2LP_1', 'img_id': 'op4_G7P2LP_img1','left': '636px','top': '100px', 'address': 3442},
    {'id': 'op4_G4P1LP_1', 'img_id': 'op4_G4P1LP_img1','left': '636px','top': '100px', 'address': 3455},
    {'id': 'op4_G4P2LP_1', 'img_id': 'op4_G4P2LP_img1','left': '636px','top': '100px', 'address': 3444},
    {'id': 'op4_G5P1LP_1', 'img_id': 'op4_G5P1LP_img1','left': '636px','top': '100px', 'address': 3456},
    {'id': 'op4_G5P2LP_1', 'img_id': 'op4_G5P2LP_img1','left': '636px','top': '100px', 'address': 3446},
    # 右の列 ランプ
    {'id': 'op4_G6P3LP_1', 'img_id': 'op4_G6P3LP_img1','left': '1096px','top': '100px', 'address': 3436},
    {'id': 'op4_G1P3LP_1', 'img_id': 'op4_G1P3LP_img1','left': '1096px','top': '100px', 'address': 3437},
    {'id': 'op4_G2P3LP_1', 'img_id': 'op4_G2P3LP_img1','left': '1096px','top': '100px', 'address': 3439},
    {'id': 'op4_G3P3LP_1', 'img_id': 'op4_G3P3LP_img1','left': '1096px','top': '100px', 'address': 3441},
    {'id': 'op4_G7P3LP_1', 'img_id': 'op4_G7P3LP_img1','left': '1096px','top': '100px', 'address': 3443},
    {'id': 'op4_G4P3LP_1', 'img_id': 'op4_G4P3LP_img1','left': '1096px','top': '100px', 'address': 3445},
    {'id': 'op4_G5P3LP_1', 'img_id': 'op4_G5P3LP_img1','left': '1096px','top': '100px', 'address': 3447},
]

BASE_TOP = 8
# ラベルのy座標の再割り当て
for i, item in enumerate(text_data):
    index = i % 10
    item['top'] = f'{index*72+BASE_TOP}px'  # itemはtext_list[i]と同じ辞書への参照なので、itemを更新すれば元のリストも更新される

# ボタンのy座標の再割り当て（レイアウトの表示を見て、新たなBASE_TOPを作るか確認すること）
COLUM5_RAW6 = 40 + 7     # 5列目は7行目まで
for i, item in enumerate(button_data):
    index = 0
    if i >= COLUM5_RAW6:
        index = i - COLUM5_RAW6
    else:
        index = i % 10
    item['top'] = f'{index*72+BASE_TOP}px'

LP_BASE_TOP = 12
# ランプのy座標の再割り当て（レイアウトの表示を見て、新たなBASE_TOPを作るか確認すること）
LP_COLUM5_RAW6 = 100 #10 + 7     # 2列目は7行目まで # 折り返しはないので100で設定
for i, item in enumerate(lamp_data):
    index = 0
    if i >= LP_COLUM5_RAW6:
        index = i - LP_COLUM5_RAW6
    else:
        index = i % 10
    item['top'] = f'{index*72+LP_BASE_TOP}px'

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

# 四角の背景
def _add_backgrounds(layout, bg_list, border_style, z_index):
    """汎用的な背景Div要素をレイアウトに追加するヘルパー関数"""
    for bg in bg_list:
        color = bg['color']
        layout.append(html.Div(style={
            'position': 'absolute',
            'left': bg['left'],
            'top': bg['top'],
            'width': bg['width'],
            'height': bg['height'],
            'backgroundColor': color,
            'border': border_style,
            'zIndex': z_index,
        }))

def create_operation4_layout():
    # Content-3 (操作エリア) のモード 2 用レイアウト
    layout = []

    # 0. 配管操作グループ枠組み (z-index: 4)
    background_lists = [
        {'left': '40px', 'top': '76px', 'width': '444px', 'height': '288px', 'color': "#C4B2FF86"},
        {'left': '40px', 'top': '436px', 'width': '444px', 'height': '288px', 'color': "#B2CEFF86"},
        {'left': '500px', 'top': '4px', 'width': '444px', 'height': '144px', 'color': "#FFB2FA86"},
        {'left': '500px', 'top': '148px', 'width': '444px', 'height': '144px', 'color': "#B2FFC186"},
        {'left': '500px', 'top': '292px', 'width': '444px', 'height': '432px', 'color': "#FFC0B286"},
    ]
    _add_backgrounds(layout, background_lists, '1px solid #999999', 4)

    # 1. テキスト (z-index: 5)
    for i,data in enumerate(text_data):
        # # 'left'と'top'の値からpxを除去し、オフセットを適用
        id = f'op4_text{i}'
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

    # 2. 操作ボタン (z-index: 5)
    for data in button_data:
        button_text = data['type'] # 'ON' または 'OFF'
        
        layout.append(html.Button(
            id=data['id'],
            n_clicks=0,
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
                    button_text,
                    style={
                        'position': 'absolute',
                        # ボタンの中央に配置
                        'top': '50%',
                        'left': '50%',
                        'transform': 'translate(-50%, -50%)', # CSSで完全な中央揃え
                        'fontSize': '20px',
                        'fontFamily': 'Meiryo UI',
                        'fontWeight': 'bold',
                        'color': 'black', # 文字色
                        'zIndex': 2 # 画像より上
                    }
                )
            ],
            style={
                'position': 'absolute',
                'left': data['left'], 'top': data['top'],
                'width': '128px', 'height': '64px',
                'fontSize': '18px',
                'zIndex': 5,
                # children の absolute 配置を基準にするため、position: relative は必須
                #'position': 'relative', 
                'padding': '0', # Paddingを除去して画像を表示
                'border': 'none', # ボーダーを除去
                'background': 'none',# 背景を除去
                'overflow': 'hidden' # 子要素がはみ出さないように
            }
        ))
    # 3. ダミーコンポーネント (操作ボタンのOutコールバック用)
    layout.append(
        html.Div(id='dummy-button-op4', style={'display': 'none'}) 
    )

    # 4. インターロックランプの追加
    for data in lamp_data:
        _add_lamp(layout, data)

    return layout