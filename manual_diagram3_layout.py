from dash import html
from constans import FormatSpecifier, BASE_STYLES_MAP

# --------------------------------------------------------
# 数値表示のリスト
# コールバックで'children'を変更します
# --------------------------------------------------------
monitor_list = [
    # 白色のテキスト
    {'id': 'dg3_MFC6_moni', 'left': '212px', 'top': '44px', 'color': 'white', 'width': '121px', 'address': 6044, 'format': FormatSpecifier.F3_1},
    {'id': 'dg3_MFC1_moni', 'left': '212px', 'top': '116px', 'color': 'white', 'width': '121px', 'address': 6034, 'format': FormatSpecifier.F3_1},
    {'id': 'dg3_MFC2_moni', 'left': '460px', 'top': '44px', 'color': 'white', 'width': '121px', 'address': 6036, 'format': FormatSpecifier.F3_1},
    {'id': 'dg3_MFC3_moni', 'left': '708px', 'top': '44px', 'color': 'white', 'width': '121px', 'address': 6038, 'format': FormatSpecifier.F3_1},
    {'id': 'dg3_MFC7_moni', 'left': '956px', 'top': '44px', 'color': 'white', 'width': '121px', 'address': 6046, 'format': FormatSpecifier.F3_1},
    {'id': 'dg3_MFC4_moni', 'left': '956px', 'top': '116px', 'color': 'white', 'width': '121px', 'address': 6040, 'format': FormatSpecifier.F3_1},
    {'id': 'dg3_MFC5_moni', 'left': '1204px', 'top': '44px', 'color': 'white', 'width': '121px', 'address': 6042, 'format': FormatSpecifier.F3_1},

    {'id': 'dg3_PT6_moni', 'left': '212px', 'top': '1000px', 'color': 'white', 'width': '121px', 'address': 6088, 'format': FormatSpecifier.F3_1},
    {'id': 'dg3_PT1_moni', 'left': '212px', 'top': '1072px', 'color': 'white', 'width': '121px', 'address': 6078, 'format': FormatSpecifier.F3_1},
    {'id': 'dg3_PT2_moni', 'left': '460px', 'top': '1000px', 'color': 'white', 'width': '121px', 'address': 6080, 'format': FormatSpecifier.F3_1},
    {'id': 'dg3_PT3_moni', 'left': '708px', 'top': '1000px', 'color': 'white', 'width': '121px', 'address': 6082, 'format': FormatSpecifier.F3_1},
    {'id': 'dg3_PT7_moni', 'left': '956px', 'top': '1000px', 'color': 'white', 'width': '121px', 'address': 6090, 'format': FormatSpecifier.F3_1},
    {'id': 'dg3_PT4_moni', 'left': '956px', 'top': '1072px', 'color': 'white', 'width': '121px', 'address': 6084, 'format': FormatSpecifier.F3_1},
    {'id': 'dg3_PT5_moni', 'left': '1204px', 'top': '1000px', 'color': 'white', 'width': '121px', 'address': 6086, 'format': FormatSpecifier.F3_1},

    {'id': 'dg3_FLU1', 'left': '212px', 'top': '1160px', 'color': 'white', 'width': '121px', 'address': 6056, 'format': FormatSpecifier.F3_2},
    {'id': 'dg3_FLU2', 'left': '212px', 'top': '1232px', 'color': 'white', 'width': '121px', 'address': 6054, 'format': FormatSpecifier.F3_2},
]
# ID のリスト
diagram3_ids_children = [
    data['id'] for data in monitor_list
]
# --------------------------------------------------------
# バルブのリスト
# コールバックで'src'を変更します
# --------------------------------------------------------
# 縦向きのバルブ
YOKO_MUKI = False
TATE_MUKI = True
tate_L_valves = [
    {'id': 'dg3_N2DP2', 'left': '134px', 'top': '348px', 'address': 859, 'name': 'N2DP2', 'muki': TATE_MUKI},
    {'id': 'dg3_N2BP2', 'left': '268px', 'top': '348px', 'address': 834, 'name': 'N2BP2', 'muki': TATE_MUKI},
    {'id': 'dg3_N2CP2', 'left': '134px', 'top': '496px', 'address': 858, 'name': 'N2CP2', 'muki': TATE_MUKI},
    {'id': 'dg3_N2BP1', 'left': '134px', 'top': '628px', 'address': 835, 'name': 'N2BP1', 'muki': TATE_MUKI},
    {'id': 'dg3_N2AP1', 'left': '268px', 'top': '628px', 'address': 835, 'name': 'N2AP1', 'muki': TATE_MUKI},
    {'id': 'dg3_N2BP0', 'left': '134px', 'top': '848px', 'address': 849, 'name': 'N2BP0', 'muki': TATE_MUKI},
    {'id': 'dg3_N2AP0', 'left': '268px', 'top': '848px', 'address': 849, 'name': 'N2AP0', 'muki': TATE_MUKI},
]
tate_R_valves = [
    {'id': 'dg3_EXP1', 'left': '512px', 'top': '262px', 'address': 824, 'name': 'EXP1', 'muki': TATE_MUKI},
    {'id': 'dg3_EXP2', 'left': '668px', 'top': '262px', 'address': 825, 'name': 'EXP2', 'muki': TATE_MUKI},
    {'id': 'dg3_EXP3', 'left': '826px', 'top': '262px', 'address': 826, 'name': 'EXP3', 'muki': TATE_MUKI},

    {'id': 'dg3_G6P2', 'left': '338px', 'top': '348px', 'address': 828, 'name': 'G6P2', 'muki': TATE_MUKI},
    {'id': 'dg3_G1P2', 'left': '468px', 'top': '348px', 'address': 827, 'name': 'G1P2', 'muki': TATE_MUKI},
    {'id': 'dg3_G2P2', 'left': '628px', 'top': '348px', 'address': 838, 'name': 'G2P2', 'muki': TATE_MUKI},
    {'id': 'dg3_G3P2', 'left': '790px', 'top': '348px', 'address': 840, 'name': 'G3P2', 'muki': TATE_MUKI},
    {'id': 'dg3_G7P2', 'left': '948px', 'top': '348px', 'address': 842, 'name': 'G7P2', 'muki': TATE_MUKI},
    {'id': 'dg3_G4P2', 'left': '1078px', 'top': '348px', 'address': 844, 'name': 'G4P2', 'muki': TATE_MUKI},
    {'id': 'dg3_G5P2', 'left': '1210px', 'top': '348px', 'address': 846, 'name': 'G5P2', 'muki': TATE_MUKI},

    {'id': 'dg3_G6P1', 'left': '338px', 'top': '628px', 'address': 850, 'name': 'G6P1', 'muki': TATE_MUKI},
    {'id': 'dg3_G1P1', 'left': '468px', 'top': '628px', 'address': 851, 'name': 'G1P1', 'muki': TATE_MUKI},
    {'id': 'dg3_G2P1', 'left': '628px', 'top': '628px', 'address': 852, 'name': 'G2P1', 'muki': TATE_MUKI},
    {'id': 'dg3_G3P1', 'left': '790px', 'top': '628px', 'address': 853, 'name': 'G3P1', 'muki': TATE_MUKI},
    {'id': 'dg3_G7P1', 'left': '948px', 'top': '628px', 'address': 854, 'name': 'G7P1', 'muki': TATE_MUKI},
    {'id': 'dg3_G4P1', 'left': '1078px', 'top': '628px', 'address': 855, 'name': 'G4P1', 'muki': TATE_MUKI},
    {'id': 'dg3_G5P1', 'left': '1210px', 'top': '628px', 'address': 856, 'name': 'G5P1', 'muki': TATE_MUKI},

    {'id': 'dg3_G1P0', 'left': '468px', 'top': '848px', 'address': 848, 'name': 'G1P0', 'muki': TATE_MUKI},
    {'id': 'dg3_G2P0', 'left': '628px', 'top': '848px', 'address': 848, 'name': 'G2P0', 'muki': TATE_MUKI},
    {'id': 'dg3_G3P0', 'left': '790px', 'top': '848px', 'address': 848, 'name': 'G3P0', 'muki': TATE_MUKI},
    {'id': 'dg3_G4P0', 'left': '1078px', 'top': '848px', 'address': 848, 'name': 'G4P0', 'muki': TATE_MUKI},
    {'id': 'dg3_G5P0', 'left': '1210px', 'top': '848px', 'address': 848, 'name': 'G5P0', 'muki': TATE_MUKI},
]
# 横向きのバルブ 
yoko_valves = [
    {'id': 'dg3_G6P3', 'left': '380px', 'top': '522px', 'address': 836, 'name': 'G6P3', 'muki': YOKO_MUKI},
    {'id': 'dg3_G1P3', 'left': '512px', 'top': '522px', 'address': 837, 'name': 'G1P3', 'muki': YOKO_MUKI},
    {'id': 'dg3_G2P3', 'left': '672px', 'top': '522px', 'address': 839, 'name': 'G2P3', 'muki': YOKO_MUKI},
    {'id': 'dg3_G3P3', 'left': '834px', 'top': '522px', 'address': 841, 'name': 'G3P3', 'muki': YOKO_MUKI},
    {'id': 'dg3_G7P3', 'left': '992px', 'top': '522px', 'address': 843, 'name': 'G7P3', 'muki': YOKO_MUKI},
    {'id': 'dg3_G4P3', 'left': '1124px', 'top': '522px', 'address': 845, 'name': 'G4P3', 'muki': YOKO_MUKI},
    {'id': 'dg3_G5P3', 'left': '1252px', 'top': '522px', 'address': 847, 'name': 'G5P3', 'muki': YOKO_MUKI},
]

# 3. 'src' プロパティを更新する為の辞書
# (コールバックでid、addressを参照し、画像のsrcを変更する)
diagram3_valve_indicators = (
    tate_L_valves + tate_R_valves +
    yoko_valves
)

# 圧力センサー
sensor_list = [
    {'id': 'dg3_PT6', 'left': '338px', 'top': '700px', 'address': 87,'style_type': 'BASE_36px', 'name': 'PT G6'},
    {'id': 'dg3_PT1', 'left': '468px', 'top': '700px', 'address': 82,'style_type': 'BASE_36px', 'name': 'PT G1'},
    {'id': 'dg3_PT2', 'left': '628px', 'top': '700px', 'address': 83,'style_type': 'BASE_36px', 'name': 'PT G2'},
    {'id': 'dg3_PT3', 'left': '790px', 'top': '700px', 'address': 84,'style_type': 'BASE_36px', 'name': 'PT G3'},
    {'id': 'dg3_PT7', 'left': '948px', 'top': '700px', 'address': 88,'style_type': 'BASE_36px', 'name': 'PT G7'},
    {'id': 'dg3_PT4', 'left': '1078px', 'top': '700px', 'address': 85,'style_type': 'BASE_36px', 'name': 'PT G4'},
    {'id': 'dg3_PT5', 'left': '1210px', 'top': '700px', 'address': 86,'style_type': 'BASE_36px', 'name': 'PT G5'},
]

# --------------------------------------------------------
# 図形描画用のヘルパー関数
# --------------------------------------------------------
def _add_horizontal_pipes(layout, pipe_list, color, z_index):
    """水平方向の配管（高さ: 4px）をレイアウトに追加するヘルパー関数"""
    for pipe in pipe_list:
        layout.append(html.Div(style={
            'position': 'absolute',
            'left': pipe['left'],
            'top': pipe['top'],
            'width': pipe['width'],
            'height': '4px',
            'backgroundColor': color,
            'zIndex': z_index,
        }))

def _add_vertical_pipes(layout, pipe_list, color, z_index):
    """垂直方向の配管（幅: 4px）をレイアウトに追加するヘルパー関数"""
    for pipe in pipe_list:
        layout.append(html.Div(style={
            'position': 'absolute',
            'left': pipe['left'],
            'top': pipe['top'],
            'width': '4px',
            'height': pipe['height'],
            'backgroundColor': color,
            'zIndex': z_index,
        }))

# 四角の背景
def _add_backgrounds(layout, bg_list, color, border_style, z_index):
    """汎用的な背景Div要素をレイアウトに追加するヘルパー関数"""
    for bg in bg_list:
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

def _add_color_backgrounds(layout, bg_list, border_style, z_index):
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

# ゲージ（円）を生成
def _add_create_gauge(layout, gauge_list, size, color, border_style, z_index):
    for gg in gauge_list:
        layout.append(html.Div(style={
            'position': 'absolute',
            'left': gg['left'],
            'top': gg['top'],
            'width': size,
            'height': size,
            'borderRadius': '50%',
            'backgroundColor': color,
            'border': border_style,
            'zIndex': z_index,
        }))

def _add_text(layout, text_list):
    for text in text_list:
        layout.append(html.Div(
            text['text'],
            style={
                'position': 'absolute',
                'left': text['left'],
                'top': text['top'],
                'fontSize': '18px',
                'fontWeight': 'bold',
                'color': 'black',
                'fontFamily': 'Meiryo UI',
                'zIndex': 16,
            }
        ))

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
                'textAlign': 'center',
                'width': width,
                'fontSize': '18px',
                'fontWeight': 'bold',
                'color': item.get('name_color', color), # name_colorが定義されていればそれを使用、なければcolor
                'fontFamily': 'Meiryo UI',
                'zIndex': z_index,
            }
        ))

def create_diagram3_layout():

    layout = []
    

    # 6. 濃いグレーの背景 (z-index: 6)
    dark_gray_backgrounds = [
        {'left': '188px', 'top': '16px', 'width': '241px', 'height': '73px'},
        {'left': '188px', 'top': '88px', 'width': '241px', 'height': '73px'},
        {'left': '436px', 'top': '16px', 'width': '241px', 'height': '73px'},
        {'left': '684px', 'top': '16px', 'width': '241px', 'height': '73px'},
        {'left': '932px', 'top': '16px', 'width': '241px', 'height': '73px'},
        {'left': '932px', 'top': '88px', 'width': '241px', 'height': '73px'},
        {'left': '1180px', 'top': '16px', 'width': '241px', 'height': '73px'},

        {'left': '188px', 'top': '972px', 'width': '241px', 'height': '73px'},
        {'left': '188px', 'top': '1044px', 'width': '241px', 'height': '73px'},
        {'left': '436px', 'top': '972px', 'width': '241px', 'height': '73px'},
        {'left': '684px', 'top': '972px', 'width': '241px', 'height': '73px'},
        {'left': '932px', 'top': '972px', 'width': '241px', 'height': '73px'},
        {'left': '932px', 'top': '1044px', 'width': '241px', 'height': '73px'},
        {'left': '1180px', 'top': '972px', 'width': '241px', 'height': '73px'},

        {'left': '188px', 'top': '1132px', 'width': '241px', 'height': '73px'},
        {'left': '188px', 'top': '1204px', 'width': '241px', 'height': '73px'},
    ]
    _add_backgrounds(layout, dark_gray_backgrounds, '#777777', '1px solid white', 6)

    # 7. 薄いグレーの背景 (z-index: 7)
    light_gray_backgrounds = [
        {'left': '200px', 'top': '20px', 'width': '217px', 'height': '65px'},
        {'left': '200px', 'top': '92px', 'width': '217px', 'height': '65px'},
        {'left': '448px', 'top': '20px', 'width': '217px', 'height': '65px'},
        {'left': '696px', 'top': '20px', 'width': '217px', 'height': '65px'},
        {'left': '944px', 'top': '20px', 'width': '217px', 'height': '65px'},
        {'left': '944px', 'top': '92px', 'width': '217px', 'height': '65px'},
        {'left': '1192px', 'top': '20px', 'width': '217px', 'height': '65px'},

        {'left': '4px', 'top': '172px', 'width': '1421px', 'height': '789px'},

        # {'left': '42px', 'top': '334px', 'width': '271px', 'height': '586px'},
        # {'left': '320px', 'top': '334px', 'width': '281px', 'height': '586px'},
        # {'left': '608px', 'top': '334px', 'width': '153px', 'height': '586px'},
        # {'left': '768px', 'top': '334px', 'width': '153px', 'height': '586px'},
        # {'left': '928px', 'top': '334px', 'width': '417px', 'height': '586px'},

        {'left': '200px', 'top': '976px', 'width': '217px', 'height': '65px'},
        {'left': '200px', 'top': '1048px', 'width': '217px', 'height': '65px'},
        {'left': '448px', 'top': '976px', 'width': '217px', 'height': '65px'},
        {'left': '696px', 'top': '976px', 'width': '217px', 'height': '65px'},
        {'left': '944px', 'top': '976px', 'width': '217px', 'height': '65px'},
        {'left': '944px', 'top': '1048px', 'width': '217px', 'height': '65px'},
        {'left': '1192px', 'top': '976px', 'width': '217px', 'height': '65px'},

        {'left': '200px', 'top': '1136px', 'width': '217px', 'height': '65px'},
        {'left': '200px', 'top': '1208px', 'width': '217px', 'height': '65px'},
    ]
    _add_backgrounds(layout, light_gray_backgrounds, '#DDE0E4', '1px solid #999999', 7)

    # 7. カラフルな背景 (z-index: 7)
    color_backgrounds = [
        {'left': '42px', 'top': '334px', 'width': '271px', 'height': '586px', 'color': "#C4B2FF86"},
        {'left': '320px', 'top': '334px', 'width': '281px', 'height': '586px', 'color': "#B2CEFF86"},
        {'left': '608px', 'top': '334px', 'width': '153px', 'height': '586px', 'color': "#FFB2FA86"},
        {'left': '768px', 'top': '334px', 'width': '153px', 'height': '586px', 'color': "#B2FFC186"},
        {'left': '928px', 'top': '334px', 'width': '417px', 'height': '586px', 'color': "#FFC0B286"},
    ]
    _add_color_backgrounds(layout, color_backgrounds, '1px solid #999999', 7)

    # 8. 黒の背景 (z-index: 8)
    black_backgrounds = [
        {'left': '212px', 'top': '44px', 'width': '121px', 'height': '37px'},
        {'left': '212px', 'top': '116px', 'width': '121px', 'height': '37px'},
        {'left': '460px', 'top': '44px', 'width': '121px', 'height': '37px'},
        {'left': '708px', 'top': '44px', 'width': '121px', 'height': '37px'},
        {'left': '956px', 'top': '44px', 'width': '121px', 'height': '37px'},
        {'left': '956px', 'top': '116px', 'width': '121px', 'height': '37px'},
        {'left': '1204px', 'top': '44px', 'width': '121px', 'height': '37px'},

        {'left': '212px', 'top': '1000px', 'width': '121px', 'height': '37px'},
        {'left': '212px', 'top': '1072px', 'width': '121px', 'height': '37px'},
        {'left': '460px', 'top': '1000px', 'width': '121px', 'height': '37px'},
        {'left': '708px', 'top': '1000px', 'width': '121px', 'height': '37px'},
        {'left': '956px', 'top': '1000px', 'width': '121px', 'height': '37px'},
        {'left': '956px', 'top': '1072px', 'width': '121px', 'height': '37px'},
        {'left': '1204px', 'top': '1000px', 'width': '121px', 'height': '37px'},

        {'left': '212px', 'top': '1160px', 'width': '121px', 'height': '37px'},
        {'left': '212px', 'top': '1232px', 'width': '121px', 'height': '37px'},
    ]
    _add_backgrounds(layout, black_backgrounds, 'black', '1px solid white', 8)

    # 9. バルブ 機器名 (z-index: 9)
    _add_device_name(layout, tate_L_valves, offset_x=-68, offset_y=12, width='60px', color='black', z_index=9)
    _add_device_name(layout, tate_R_valves, offset_x=36, offset_y=12, width='60px', color='black', z_index=9)
    _add_device_name(layout, yoko_valves, offset_x=0, offset_y=-24, width='40px', color='black', z_index=9)

    # 11. 黒の配管 (z-index: 11)
    black_h_pipes = [
        {'left': '356px', 'top': '538px', 'width': '26px'},
        {'left': '484px', 'top': '538px', 'width': '26px'},
        {'left': '646px', 'top': '538px', 'width': '26px'},
        {'left': '808px', 'top': '538px', 'width': '26px'},
        {'left': '964px', 'top': '538px', 'width': '26px'},
        {'left': '1096px', 'top': '538px', 'width': '26px'},
        {'left': '1228px', 'top': '538px', 'width': '26px'},

        {'left': '356px', 'top': '828px', 'width': '131px'},
        {'left': '964px', 'top': '828px', 'width': '133px'},
    ]
    black_v_pipes = [
        {'left': '152px', 'top': '676px', 'height': '173px'},
        {'left': '284px', 'top': '676px', 'height': '173px'},
        {'left': '152px', 'top': '896px', 'height': '24px'},
        {'left': '284px', 'top': '896px', 'height': '24px'},

        {'left': '356px', 'top': '396px', 'height': '233px'},
        {'left': '356px', 'top': '676px', 'height': '156px'},
        {'left': '484px', 'top': '396px', 'height': '233px'},
        {'left': '484px', 'top': '676px', 'height': '173px'},
        {'left': '484px', 'top': '896px', 'height': '24px'},

        {'left': '646px', 'top': '396px', 'height': '233px'},
        {'left': '646px', 'top': '676px', 'height': '173px'},
        {'left': '646px', 'top': '896px', 'height': '24px'},

        {'left': '808px', 'top': '396px', 'height': '233px'},
        {'left': '808px', 'top': '676px', 'height': '173px'},
        {'left': '808px', 'top': '896px', 'height': '24px'},

        {'left': '964px', 'top': '396px', 'height': '233px'},
        {'left': '964px', 'top': '676px', 'height': '156px'},

        {'left': '1096px', 'top': '396px', 'height': '233px'},
        {'left': '1096px', 'top': '676px', 'height': '173px'},
        {'left': '1096px', 'top': '896px', 'height': '24px'},

        {'left': '1228px', 'top': '396px', 'height': '233px'},
        {'left': '1228px', 'top': '676px', 'height': '173px'},
        {'left': '1228px', 'top': '896px', 'height': '24px'},
    ]
    _add_horizontal_pipes(layout, black_h_pipes, 'black', 11)
    _add_vertical_pipes(layout, black_v_pipes, 'black', 11)

    # 12. エメラルドの配管 (z-index: 12)
    green_h_pipes = [
        {'left': '428px', 'top': '540px', 'width': '26px'},
        {'left': '560px', 'top': '540px', 'width': '26px'},
        {'left': '720px', 'top': '540px', 'width': '26px'},
        {'left': '284px', 'top': '606px', 'width': '466px'},
    ]
    green_v_pipes = [
        {'left': '454px', 'top': '540px', 'height': '67px'},
        {'left': '584px', 'top': '540px', 'height': '67px'},
        {'left': '746px', 'top': '540px', 'height': '67px'},
        {'left': '284px', 'top': '606px', 'height': '26px'},
    ]
    _add_horizontal_pipes(layout, green_h_pipes, '#009999', 12)
    _add_vertical_pipes(layout, green_v_pipes, '#009999', 12)

    # 12. ピンクの配管 (z-index: 12)
    pink_h_pipes = [
        {'left': '24px', 'top': '212px', 'width': '941px'},
    ]
    pink_v_pipes = [
        {'left': '356px', 'top': '212px', 'height': '137px'},
        {'left': '964px', 'top': '212px', 'height': '137px'},
    ]
    _add_horizontal_pipes(layout, pink_h_pipes, 'magenta', 12)
    _add_vertical_pipes(layout, pink_v_pipes, 'magenta', 12)

    # 13. 紫の配管 (z-index: 13)
    purple_h_pipes = [
        {'left': '24px', 'top': '250px', 'width': '1205px'},
    ]
    purple_v_pipes = [
        {'left': '484px', 'top': '252px', 'height': '97px'},
        {'left': '644px', 'top': '252px', 'height': '97px'},
        {'left': '808px', 'top': '252px', 'height': '97px'},
        {'left': '1096px', 'top': '252px', 'height': '97px'},
        {'left': '1228px', 'top': '252px', 'height': '97px'},
    ]
    _add_horizontal_pipes(layout, purple_h_pipes, 'blueviolet', 13)
    _add_vertical_pipes(layout, purple_v_pipes, 'blueviolet', 13)

    # 14. シアンブルーの配管 (z-index: 14)
    deepskyblue_h_pipes = [
        {'left': '24px', 'top': '322px', 'width': '261px'},
        {'left': '154px', 'top': '578px', 'width': '1172px'},
        {'left': '884px', 'top': '540px', 'width': '26px'},
        {'left': '1040px', 'top': '540px', 'width': '26px'},
        {'left': '1172px', 'top': '540px', 'width': '26px'},
        {'left': '1300px', 'top': '540px', 'width': '26px'},
    ]
    deepskyblue_v_pipes = [
        {'left': '152px', 'top': '322px', 'height': '26px'},
        {'left': '284px', 'top': '322px', 'height': '26px'},
        {'left': '152px', 'top': '394px', 'height': '103px'},
        {'left': '284px', 'top': '394px', 'height': '183px'},
        {'left': '152px', 'top': '544px', 'height': '85px'},
        {'left': '908px', 'top': '540px', 'height': '39px'},
        {'left': '1064px', 'top': '540px', 'height': '39px'},
        {'left': '1196px', 'top': '540px', 'height': '39px'},
        {'left': '1324px', 'top': '540px', 'height': '39px'},
    ]
    _add_horizontal_pipes(layout, deepskyblue_h_pipes, 'deepskyblue', 14)
    _add_vertical_pipes(layout, deepskyblue_v_pipes, 'deepskyblue', 14)

    # 14. シアンの配管 (z-index: 14)
    cyan_v_pipes = [
        {'left': '530px', 'top': '182px', 'height': '79px'},
        {'left': '530px', 'top': '308px', 'height': '26px'},
        {'left': '686px', 'top': '182px', 'height': '79px'},
        {'left': '686px', 'top': '308px', 'height': '26px'},
        {'left': '844px', 'top': '182px', 'height': '79px'},
        {'left': '844px', 'top': '308px', 'height': '26px'},
    ]
    _add_vertical_pipes(layout, cyan_v_pipes, 'cyan', 14)

    # 15. 垂直のバルブ (z-index: 15)
    tate_valves = tate_L_valves + tate_R_valves
    for valve in tate_valves:
        layout.append(html.Img(
            id=valve['id'],
            src='/assets/images/valve_off_tate.png',
            style={
                'position': 'absolute',
                'left': valve['left'],
                'top': valve['top'],
                'width': '36px', 'height': '48px',
                'zIndex': 15,
            }
        ))

    # 15. 水平のバルブ (z-index: 15)
    for valve in yoko_valves:
        layout.append(html.Img(
            id=valve['id'],
            src='/assets/images/valve_off.png',
            style={
                'position': 'absolute',
                'left': valve['left'],
                'top': valve['top'],
                'width': '48px', 'height': '36px',
                'zIndex': 15,
            }
        ))

    # 15. レギュレータ (z-index: 15)
    regu_L = [
        {'left': '134px', 'top': '762px', 'name': 'N2BRG'},
        {'left': '268px', 'top': '762px', 'name': 'N2ARG'},
    ]
    regu_R = [
        {'left': '338px', 'top': '424px', 'name': 'MFC G6'},
        {'left': '468px', 'top': '424px', 'name': 'MFC G1'},
        {'left': '628px', 'top': '424px', 'name': 'MFC G2'},
        {'left': '790px', 'top': '424px', 'name': 'MFC G3'},
        {'left': '948px', 'top': '424px', 'name': 'MFC G7'},
        {'left': '1078px', 'top': '424px', 'name': 'MFC G4'},
        {'left': '1210px', 'top': '424px', 'name': 'MFC G5'},

        {'left': '338px', 'top': '760px', 'name': 'G6 RG'},
        {'left': '468px', 'top': '760px', 'name': 'G1 RG'},
        {'left': '628px', 'top': '760px', 'name': 'G2 RG'},
        {'left': '790px', 'top': '760px', 'name': 'G3 RG'},
        {'left': '948px', 'top': '760px', 'name': 'G7 RG'},
        {'left': '1078px', 'top': '760px', 'name': 'G4 RG'},
        {'left': '1210px', 'top': '760px', 'name': 'G5 RG'},
    ]
    regus = regu_L + regu_R
    for regu in regus:
        regu['width'] = '36px'
        regu['height'] = '48px'
    
    _add_backgrounds(layout, regus, '#777777', '1px solid white', 15)
    _add_device_name(layout, regu_L, offset_x=-80, offset_y=12, width='72px', color='black', z_index=9)
    _add_device_name(layout, regu_R, offset_x=40, offset_y=12, width='72px', color='black', z_index=9)

    # 15. ゲージPT (z-index: 15)
    # センサー、ポンプ等のマークの生成 
    for item in sensor_list:        
        # 1. ベーススタイルを取得
        base_style = BASE_STYLES_MAP[item['style_type']].copy()
        
        # 2. 座標情報で上書き
        base_style['left'] = item['left']
        base_style['top'] = item['top']
        
        # 3. 初期色を設定 (例: 初期状態は灰色)
        base_style['backgroundColor'] = 'gray'
        
        # コンポーネントの初期スタイルとして設定
        layout.append(html.Div(id=item['id'], style=base_style))

    _add_device_name(layout, sensor_list, offset_x=40, offset_y=6, width='60px', color='black', z_index=15)

    gauge_list = [
        {'left': '134px', 'top': '700px', 'name': 'N2BG1'},
        {'left': '266px', 'top': '700px', 'name': 'N2AG1'},
    ]
    _add_create_gauge(layout, gauge_list, size='36px', color='gray', border_style='1px solid white', z_index=15)
    _add_device_name(layout, gauge_list, offset_x=-72, offset_y=6, width='60px', color='black', z_index=15)

    # 16. 機器名称 (z-index: 16)
    text_list = [
        {'left': '212px', 'top': '20px', 'text': 'MFC G6 H2マスフロー'},
        {'left': '212px', 'top': '92px', 'text': 'MFC G1 H2マスフロー'},
        {'left': '460px', 'top': '20px', 'text': 'MFC G2 CH4マスフロー'},
        {'left': '708px', 'top': '20px', 'text': 'MFC G3 O2マスフロー'},
        {'left': '956px', 'top': '20px', 'text': 'MFC G7 Arマスフロー'},
        {'left': '956px', 'top': '92px', 'text': 'MFC G4 Arマスフロー'},
        {'left': '1204px', 'top': '20px', 'text': 'MFC G5 N2マスフロー'},

        {'left': '336px', 'top': '52px', 'text': 'sccm'},
        {'left': '336px', 'top': '124px', 'text': 'sccm'},
        {'left': '584px', 'top': '52px', 'text': 'sccm'},
        {'left': '832px', 'top': '52px', 'text': 'sccm'},
        {'left': '1080px', 'top': '52px', 'text': 'sccm'},
        {'left': '1080px', 'top': '124px', 'text': 'sccm'},
        {'left': '1328px', 'top': '52px', 'text': 'sccm'},

        {'left': '212px', 'top': '976px', 'text': 'PT6 H2ガスレギュレータ'},
        {'left': '212px', 'top': '1048px', 'text': 'PT1 H2ガスレギュレータ'},
        {'left': '460px', 'top': '976px', 'text': 'PT2 CH4ガスレギュレータ'},
        {'left': '708px', 'top': '976px', 'text': 'PT3 O2ガスレギュレータ'},
        {'left': '956px', 'top': '976px', 'text': 'PT7 Arガスレギュレータ'},
        {'left': '956px', 'top': '1048px', 'text': 'PT4 Arガスレギュレータ'},
        {'left': '1204px', 'top': '976px', 'text': 'PT5 N2ガスレギュレータ'},

        {'left': '336px', 'top': '1008px', 'text': 'kPa'},
        {'left': '336px', 'top': '1080px', 'text': 'kPa'},
        {'left': '584px', 'top': '1008px', 'text': 'kPa'},
        {'left': '832px', 'top': '1008px', 'text': 'kPa'},
        {'left': '1080px', 'top': '1008px', 'text': 'kPa'},
        {'left': '1080px', 'top': '1080px', 'text': 'kPa'},
        {'left': '1328px', 'top': '1008px', 'text': 'kPa'},

        {'left': '212px', 'top': '1136px', 'text': 'FLU1 TMP1 N2パージ'},
        {'left': '212px', 'top': '1208px', 'text': 'FLU2 RP1 N2パージ'},

        {'left': '336px', 'top': '1168px', 'text': 'L/min'},
        {'left': '336px', 'top': '1240px', 'text': 'L/min'},

        {'left': '24px', 'top': '182px', 'text': 'G02 上部電極シールド'},
        {'left': '24px', 'top': '220px', 'text': 'G01 プロセスガス'},
        {'left': '24px', 'top': '290px', 'text': 'チャンバパージ/ヒーター'},
        {'left': '544px', 'top': '182px', 'text': 'N2'},
        {'left': '700px', 'top': '182px', 'text': 'N2'},
        {'left': '856px', 'top': '182px', 'text': 'N2'},
        {'left': '154px', 'top': '920px', 'text': 'N2 IN'},
        {'left': '448px', 'top': '920px', 'text': 'H2 IN'},
        {'left': '652px', 'top': '920px', 'text': 'CH4 IN'},
        {'left': '812px', 'top': '920px', 'text': 'O2 IN'},
        {'left': '1068px', 'top': '920px', 'text': 'Ar IN'},
        {'left': '1196px', 'top': '920px', 'text': 'N2 IN'},
    ]
    _add_text(layout, text_list)
    
    # フォントの幅に合わせたスタイルを定義
    font_styles = {
        '121px': {'width': '121px', 'textAlign': 'center', 'fontWeight': 'bold'},
        '153px': {'width': '153px', 'textAlign': 'center', 'fontWeight': 'bold'}
    }
    # 17. モニター値 (z-index: 17)
    for data in monitor_list:
        # 'top'の文字列から数値を取り出し、計算する
        top_value = int(data['top'].replace('px', '')) + 6
        style = {
            'position': 'absolute',
            'left': data['left'],
            'top': f'{top_value}px', # 'top': f'calc({data["top"]} + 2px)'の書式はCSS不可
            'fontSize': '22px',
            'color': data['color'],
            'zIndex': 17,
            **font_styles[data['width']]
        }
        layout.append(html.Div(data['id'], id=data['id'], style=style))

    return layout