from dash import html
from constans import FormatSpecifier, BASE_STYLES_MAP

# --------------------------------------------------------
# 数値表示のリスト
# コールバックで'children'を変更します
# --------------------------------------------------------
monitor_list = [
    # 白色のテキスト
    {'id': 'dg1_RF1_out_1', 'left': '324px', 'top': '88px', 'color': 'white', 'width': '121px', 'address': 6004, 'format': FormatSpecifier.F4_1},
    {'id': 'dg1_RF1_rev_1', 'left': '324px', 'top': '188px', 'color': 'white', 'width': '121px', 'address': 6006, 'format': FormatSpecifier.F4_1},
    {'id': 'dg1_RF1_vpp_1', 'left': '324px', 'top': '252px', 'color': 'white', 'width': '121px', 'address': 6016, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_RF1_arm_1', 'left': '324px', 'top': '316px', 'color': 'white', 'width': '121px', 'address': 6018, 'format': FormatSpecifier.F3_2},
    {'id': 'dg1_H1_1', 'left': '324px', 'top': '440px', 'color': 'white', 'width': '121px', 'address': 6020, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_H2_1', 'left': '324px', 'top': '560px', 'color': 'white', 'width': '121px', 'address': 6022, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_H3_1', 'left': '324px', 'top': '680px', 'color': 'white', 'width': '121px', 'address': 6024, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_MAT1_C1_1', 'left': '564px', 'top': '88px', 'color': 'white', 'width': '121px', 'address': 6008, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_MAT1_C2_1', 'left': '564px', 'top': '152px', 'color': 'white', 'width': '121px', 'address': 6010, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_MAT1_VDC_1', 'left': '564px', 'top': '216px', 'color': 'white', 'width': '121px', 'address': 6012, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_MAT1_tmp_1', 'left': '564px', 'top': '280px', 'color': 'white', 'width': '121px', 'address': 6014, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_SVM1_pos_1', 'left': '564px', 'top': '440px', 'color': 'white', 'width': '121px', 'address': 6092, 'format': FormatSpecifier.F3_2},

    {'id': 'dg1_IG1_1', 'left': '1080px', 'top': '68px', 'color': 'white', 'width': '153px', 'address': 6000, 'format': FormatSpecifier.FE_NOTATION},
    {'id': 'dg1_CM1_1', 'left': '1080px', 'top': '140px', 'color': 'white', 'width': '153px', 'address': 6002, 'format': FormatSpecifier.FE_NOTATION},
    {'id': 'dg1_PS1_1', 'left': '1080px', 'top': '212px', 'color': 'white', 'width': '121px', 'address': 6070, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_PS3_1', 'left': '1080px', 'top': '284px', 'color': 'white', 'width': '121px', 'address': 6074, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_PS2_1', 'left': '1080px', 'top': '428px', 'color': 'white', 'width': '121px', 'address': 6072, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_PS4_1', 'left': '1080px', 'top': '500px', 'color': 'white', 'width': '121px', 'address': 6076, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_SVM2_dg_1', 'left': '1080px', 'top': '572px', 'color': 'white', 'width': '121px', 'address': 6094, 'format': FormatSpecifier.F3_2},
    {'id': 'dg1_plasma_1', 'left': '1080px', 'top': '716px', 'color': 'white', 'width': '153px', 'address': 6122, 'format': 'date'}, # 表示は秒→時間
    #{'id': 'dg1_FLM1_1', 'left': '130px', 'top': '1004px', 'color': 'white', 'width': '121px', 'address': 6058, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_FLM2_1', 'left': '324px', 'top': '1004px', 'color': 'white', 'width': '121px', 'address': 6060, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_FLM3_1', 'left': '518px', 'top': '1004px', 'color': 'white', 'width': '121px', 'address': 6062, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_FLM4_1', 'left': '712px', 'top': '1004px', 'color': 'white', 'width': '121px', 'address': 6064, 'format': FormatSpecifier.F3_1},
    #{'id': 'dg1_FLM5_1', 'left': '906px', 'top': '1004px', 'color': 'white', 'width': '121px', 'address': 6066, 'format': FormatSpecifier.F3_1},
    {'id': 'dg1_FLM6_1', 'left': '1100px', 'top': '1004px', 'color': 'white', 'width': '121px', 'address': 6068, 'format': FormatSpecifier.F3_1},

    # シアンのテキスト
    {'id': 'dg1_RF1_out_2', 'left': '324px', 'top': '124px', 'color': 'cyan', 'width': '121px', 'address': 4000,'data_index': 0,
     'format': FormatSpecifier.F4_1},
    {'id': 'dg1_H1_2', 'left': '324px', 'top': '476px', 'color': 'cyan', 'width': '121px', 'address': 4002,'data_index': 1,
     'format': FormatSpecifier.F3_1},
    {'id': 'dg1_H2_2', 'left': '324px', 'top': '596px', 'color': 'cyan', 'width': '121px', 'address': 4004,'data_index': 2,
     'format': FormatSpecifier.F3_1},
    {'id': 'dg1_SVM1_pos_2', 'left': '564px', 'top': '476px', 'color': 'cyan', 'width': '121px', 'address': 4024,'data_index': 12,
     'format': FormatSpecifier.F3_2},
    {'id': 'dg1_SVM1_spd_2', 'left': '564px', 'top': '540px', 'color': 'cyan', 'width': '121px', 'address': 4026,'data_index': 13,
     'format': FormatSpecifier.F3_1},
]
# ID のリスト
diagram1_ids_children = [
    data['id'] for data in monitor_list
]
# ポンプ
pump_list = [
    {'id': 'dg1_TMP1', 'left': '580px', 'top': '668px', 'address': 903, 'name_color': 'white', 'name': 'TMP1'},
    {'id': 'dg1_RP1', 'left': '816px', 'top': '784px', 'address': 861, 'name_color': 'black', 'name': 'RP1'},
]
# 圧力センサー
pressure_sensor_list = [
    {'id': 'dg1_CM1','left': '120px', 'top': '140px', 'address': 947, 'name': 'CM1'},
    {'id': 'dg1_PS3', 'left': '924px', 'top': '68px', 'address': 947, 'name': 'PS3'},
    {'id': 'dg1_IG1', 'left': '924px', 'top': '140px', 'address': 947, 'name': 'IG1'},
    {'id': 'dg1_PS4', 'left': '360px', 'top': '792px', 'address': 947, 'name': 'PS4'},
    {'id': 'dg1_PS2', 'left': '816px', 'top': '720px', 'address': 947, 'name': 'PS2'},
]
# 流量センサー
flm_sensor_list = [
    #{'id': 'dg1_FLM1', 'left': '298px', 'top': '1052px', 'address': 89, 'name': 'FLM1'},
    {'id': 'dg1_FLM2', 'left': '492px', 'top': '1052px', 'address': 90, 'name': 'FLM2'},
    {'id': 'dg1_FLM3', 'left': '686px', 'top': '1052px', 'address': 91, 'name': 'FLM3'},
    {'id': 'dg1_FLM4', 'left': '880px', 'top': '1052px', 'address': 92, 'name': 'FLM4'},
    #{'id': 'dg1_FLM5', 'left': '1074px', 'top': '1052px', 'address': 93, 'name': 'FLM5'},
    {'id': 'dg1_FLM6', 'left': '1268px', 'top': '1052px', 'address': 94, 'name': 'FLM6'},
]
# チラー
chiller_list = [
    {'id': 'dg1_CHL1', 'left': '52px', 'top': '1114px', 'address': 27, 'name': 'CHL1'},
    {'id': 'dg1_CL1', 'left': '124px', 'top': '1250px', 'address': 42, 'name': 'CL1'},
]
# --------------------------------------------------------
# センサーON/OFFのリスト
# コールバックで'style'を変更します
# --------------------------------------------------------
def make_indicators(info_list, style_type):
    """
    個別の情報リストと共通のスタイルタイプに基づいて、
    コールバックで使用するインジケータ辞書のリストを生成する。
    """
    indicators = []
    for data in info_list:
        # 必要なすべての情報を統合した辞書を作成
        indicator = {
            'id': data['id'],
            'address': data['address'],
            'left': data['left'],
            'top': data['top'],

            'style_type': style_type, # 関数引数で受け取ったスタイルタイプ
        }
        indicators.append(indicator)
    return indicators

# コールバック用のindicatorsを一括生成
diagram1_style_indicators = (
    make_indicators(pump_list, 'BASE_48px') +
    make_indicators(pressure_sensor_list, 'BASE_36px') +
    make_indicators(flm_sensor_list, 'BASE_36px') +
    make_indicators(chiller_list, 'BASE_24px')
)
# --------------------------------------------------------
# バルブのリスト
# コールバックで'src'を変更します
# --------------------------------------------------------
YOKO_MUKI = False
top_valves = [
    {'id': 'dg1_AV8', 'left': '204px', 'top': '68px', 'address': 829, 'name': 'AV8', 'muki': YOKO_MUKI},
    {'id': 'dg1_AV2', 'left': '204px', 'top': '140px', 'address': 819, 'name': 'AV2', 'muki': YOKO_MUKI},
    {'id': 'dg1_AV4', 'left': '204px', 'top': '212px', 'address': 822, 'name': 'AV4', 'muki': YOKO_MUKI},
    {'id': 'dg1_AV6', 'left': '204px', 'top': '284px', 'address': 823, 'name': 'AV6', 'muki': YOKO_MUKI},
    {'id': 'dg1_AV7', 'left': '204px', 'top': '356px', 'address': 817, 'name': 'AV7', 'muki': YOKO_MUKI},
    {'id': 'dg1_AV1', 'left': '828px', 'top': '140px', 'address': 818, 'name': 'AV1', 'muki': YOKO_MUKI},
    {'id': 'dg1_AV3', 'left': '828px', 'top': '212px', 'address': 820, 'name': 'AV3', 'muki': YOKO_MUKI},
    {'id': 'dg1_AV5', 'left': '828px', 'top': '284px', 'address': 821, 'name': 'AV5', 'muki': YOKO_MUKI},
]
bottom_valves = [
    {'id': 'dg1_AV12', 'left': '348px', 'top': '864px', 'address': 833, 'name': 'AV12', 'muki': YOKO_MUKI},
    {'id': 'dg1_AV09', 'left': '720px', 'top': '648px', 'address': 830, 'name': 'AV09', 'muki': YOKO_MUKI},
    {'id': 'dg1_AV02', 'left': '720px', 'top': '720px', 'address': 814, 'name': 'AV02', 'muki': YOKO_MUKI},
    {'id': 'dg1_AV01', 'left': '720px', 'top': '792px', 'address': 996, 'name': 'AV01', 'muki': YOKO_MUKI},
    {'id': 'dg1_AV11', 'left': '720px', 'top': '864px', 'address': 832, 'name': 'AV11', 'muki': YOKO_MUKI},
    {'id': 'dg1_AV10', 'left': '816px', 'top': '864px', 'address': 831, 'name': 'AV10', 'muki': YOKO_MUKI},
]
diagram1_valve_indicators  = top_valves + bottom_valves

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

def _add_image(layout, image_list, src, width, height, z_index):
    """スタイル付きImg要素を作成するヘルパー関数。"""
    for valve in image_list:
        layout.append(html.Img(
            src=src,
            style={
                'position': 'absolute',
                'left': valve['left'],
                'top': valve['top'],
                'width': width, 'height': height,
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

def create_diagram1_layout():
    # Content-1 (模式図エリア) のモード 1 用レイアウト
    layout = []

    # 0. 流量計表示枠 (z-index: 0)
    light_gray_background1 = [
        {'left': '12px', 'top': '932px', 'width': '1417px', 'height': '357px'},
    ]
    _add_backgrounds(layout, light_gray_background1, '#e6f7ff', '1px solid #999999', 0)
    light_gray_background2 = [
        {'left': '28px', 'top': '1228px', 'width': '1377px', 'height': '13px'},
    ]
    _add_backgrounds(layout, light_gray_background2, '#DDE0E4', '1px solid #999999', 0)

    # 1. 黒の配管 (z-index: 1)
    black_h_pipes = [
        {'left': '252px', 'top': '84px', 'width': '49px'},
        {'left': '156px', 'top': '156px', 'width': '49px'},
        {'left': '252px', 'top': '156px', 'width': '49px'},
        {'left': '252px', 'top': '228px', 'width': '49px'},
        {'left': '252px', 'top': '300px', 'width': '49px'},
        {'left': '252px', 'top': '372px', 'width': '49px'},
        {'left': '804px', 'top': '84px', 'width': '121px'},
        {'left': '780px', 'top': '156px', 'width': '49px'},
        {'left': '780px', 'top': '228px', 'width': '49px'},
        {'left': '780px', 'top': '300px', 'width': '49px'},
        {'left': '876px', 'top': '156px', 'width': '49px'},

        {'left': '672px', 'top': '664px', 'width': '49px'},
        {'left': '672px', 'top': '736px', 'width': '49px'},
        {'left': '768px', 'top': '736px', 'width': '49px'},
        {'left': '396px', 'top': '808px', 'width': '49px'},
        {'left': '488px', 'top': '808px', 'width': '233px'},
        {'left': '768px', 'top': '808px', 'width': '49px'},
        {'left': '864px', 'top': '808px', 'width': '49px'},
        {'left': '396px', 'top': '880px', 'width': '325px'},
        {'left': '768px', 'top': '880px', 'width': '49px'},

        {'left': '172px', 'top': '1100px', 'width': '1177px'},
        {'left': '172px', 'top': '1160px', 'width': '1193px'},
        {'left': '1400px', 'top': '1160px', 'width': '13px'},
    ]
    black_v_pipes = [
        {'left': '804px', 'top': '84px', 'height': '73px'},
        {'left': '444px', 'top': '756px', 'height': '125px'},
        {'left': '488px', 'top': '756px', 'height': '53px'},
        {'left': '792px', 'top': '740px', 'height': '141px'},

        #{'left': '316px', 'top': '948px', 'height': '153px'},
        {'left': '510px', 'top': '948px', 'height': '153px'},
        {'left': '704px', 'top': '948px', 'height': '153px'},
        {'left': '898px', 'top': '948px', 'height': '153px'},
        #{'left': '1092px', 'top': '948px', 'height': '153px'},
        {'left': '1286px', 'top': '948px', 'height': '153px'},
        {'left': '1348px', 'top': '948px', 'height': '101px'},
        {'left': '1348px', 'top': '1084px', 'height': '17px'},

        #{'left': '316px', 'top': '1160px', 'height': '17px'},
        #{'left': '316px', 'top': '1212px', 'height': '41px'},
        {'left': '510px', 'top': '1160px', 'height': '17px'},
        {'left': '510px', 'top': '1212px', 'height': '41px'},
        {'left': '704px', 'top': '1160px', 'height': '17px'},
        {'left': '704px', 'top': '1212px', 'height': '41px'},
        {'left': '898px', 'top': '1160px', 'height': '17px'},
        {'left': '898px', 'top': '1212px', 'height': '41px'},
        #{'left': '1092px', 'top': '1160px', 'height': '17px'},
        #{'left': '1092px', 'top': '1212px', 'height': '41px'},
        {'left': '1286px', 'top': '1160px', 'height': '17px'},
        {'left': '1286px', 'top': '1212px', 'height': '41px'},
        {'left': '1348px', 'top': '1160px', 'height': '17px'},
        {'left': '1348px', 'top': '1212px', 'height': '41px'},
    ]
    _add_horizontal_pipes(layout, black_h_pipes, 'black', 1)
    _add_vertical_pipes(layout, black_v_pipes, 'black', 1)

    # 2. ピンクの配管 (z-index: 2)
    pink_h_pipes = [
        {'left': '156px', 'top': '84px', 'width': '49px'},
    ]
    _add_horizontal_pipes(layout, pink_h_pipes, 'magenta', 2)

    # 3. 紫の配管 (z-index: 3)
    purple_h_pipes = [
        {'left': '156px', 'top': '228px', 'width': '49px'},
        {'left': '156px', 'top': '300px', 'width': '49px'},
        {'left': '876px', 'top': '228px', 'width': '49px'},
        {'left': '876px', 'top': '300px', 'width': '49px'},
        {'left': '204px', 'top': '1220px', 'width': '33px'},
    ]
    purple_v_pipes = [
        {'left': '204px', 'top': '1160px', 'height': '17px'},
        {'left': '204px', 'top': '1212px', 'height': '9px'},
        {'left': '236px', 'top': '1100px', 'height': '121px'},
        {'left': '268px', 'top': '1100px', 'height': '13px'},
        {'left': '268px', 'top': '1148px', 'height': '13px'},
    ]
    _add_horizontal_pipes(layout, purple_h_pipes, 'blueviolet', 3)
    _add_vertical_pipes(layout, purple_v_pipes, 'blueviolet', 3)

    # 4. シアンの配管 (z-index: 4)
    cyan_h_pipes = [
        {'left': '768px', 'top': '664px', 'width': '49px'},
        {'left': '864px', 'top': '880px', 'width': '49px'},
    ]
    _add_horizontal_pipes(layout, cyan_h_pipes, 'cyan', 4)

    # 5. シアンブルーの配管 (z-index: 5)
    deepskyblue_h_pipes = [
        {'left': '156px', 'top': '372px', 'width': '49px'},
        {'left': '300px', 'top': '880px', 'width': '49px'},
    ]
    _add_horizontal_pipes(layout, deepskyblue_h_pipes, 'deepskyblue', 5)

    # 6. 濃いグレーの背景 (z-index: 6)
    dark_gray_backgrounds = [
        {'left': '300px', 'top': '40px', 'width': '241px', 'height': '353px'},
        {'left': '540px', 'top': '40px', 'width': '241px', 'height': '353px'},
        {'left': '300px', 'top': '392px', 'width': '241px', 'height': '365px'},
        {'left': '540px', 'top': '392px', 'width': '241px', 'height': '225px'},
        {'left': '540px', 'top': '616px', 'width': '133px', 'height': '141px'},

        {'left': '1056px', 'top': '40px', 'width': '241px', 'height': '73px'},
        {'left': '1056px', 'top': '112px', 'width': '241px', 'height': '73px'},
        {'left': '1056px', 'top': '184px', 'width': '241px', 'height': '73px'},
        {'left': '1056px', 'top': '256px', 'width': '241px', 'height': '73px'},
        {'left': '1056px', 'top': '400px', 'width': '241px', 'height': '73px'},
        {'left': '1056px', 'top': '472px', 'width': '241px', 'height': '73px'},
        {'left': '1056px', 'top': '544px', 'width': '241px', 'height': '73px'},
        {'left': '1056px', 'top': '688px', 'width': '241px', 'height': '73px'},

        {'left': '28px', 'top': '1076px', 'width': '145px', 'height': '149px'},
    ]
    _add_backgrounds(layout, dark_gray_backgrounds, '#777777', '1px solid white', 6)

    # 7. 薄いグレーの背景 (z-index: 7)
    light_gray_backgrounds = [
        {'left': '312px', 'top': '44px', 'width': '217px', 'height': '345px'},
        {'left': '552px', 'top': '44px', 'width': '217px', 'height': '345px'},
        {'left': '312px', 'top': '396px', 'width': '217px', 'height': '357px'},
        {'left': '552px', 'top': '396px', 'width': '217px', 'height': '217px'},

        {'left': '1068px', 'top': '44px', 'width': '217px', 'height': '65px'},
        {'left': '1068px', 'top': '116px', 'width': '217px', 'height': '65px'},
        {'left': '1068px', 'top': '188px', 'width': '217px', 'height': '65px'},
        {'left': '1068px', 'top': '260px', 'width': '217px', 'height': '65px'},
        {'left': '1068px', 'top': '404px', 'width': '217px', 'height': '65px'},
        {'left': '1068px', 'top': '476px', 'width': '217px', 'height': '65px'},
        {'left': '1068px', 'top': '548px', 'width': '217px', 'height': '65px'},
        {'left': '1068px', 'top': '692px', 'width': '217px', 'height': '65px'},

        {'left': '40px', 'top': '1080px', 'width': '121px', 'height': '141px'},
        
    ]
    _add_backgrounds(layout, light_gray_backgrounds, '#DDE0E4', '1px solid #999999', 7)

    # 8. 黒の背景 (z-index: 8)
    black_backgrounds = [
        {'left': '324px', 'top': '88px', 'width': '121px', 'height': '37px'},
        {'left': '324px', 'top': '124px', 'width': '121px', 'height': '37px'},
        {'left': '324px', 'top': '188px', 'width': '121px', 'height': '37px'},
        {'left': '324px', 'top': '252px', 'width': '121px', 'height': '37px'},
        {'left': '324px', 'top': '316px', 'width': '121px', 'height': '37px'},

        {'left': '324px', 'top': '440px', 'width': '121px', 'height': '37px'},
        {'left': '324px', 'top': '476px', 'width': '121px', 'height': '37px'},
        {'left': '324px', 'top': '560px', 'width': '121px', 'height': '37px'},
        {'left': '324px', 'top': '596px', 'width': '121px', 'height': '37px'},
        {'left': '324px', 'top': '680px', 'width': '121px', 'height': '37px'},

        {'left': '564px', 'top': '88px', 'width': '121px', 'height': '37px'},
        {'left': '564px', 'top': '152px', 'width': '121px', 'height': '37px'},
        {'left': '564px', 'top': '216px', 'width': '121px', 'height': '37px'},
        {'left': '564px', 'top': '280px', 'width': '121px', 'height': '37px'},
        {'left': '564px', 'top': '440px', 'width': '121px', 'height': '37px'},
        {'left': '564px', 'top': '476px', 'width': '121px', 'height': '37px'},
        {'left': '564px', 'top': '540px', 'width': '121px', 'height': '37px'},

        {'left': '1080px', 'top': '68px', 'width': '153px', 'height': '37px'},
        {'left': '1080px', 'top': '140px', 'width': '153px', 'height': '37px'},
        {'left': '1080px', 'top': '212px', 'width': '121px', 'height': '37px'},
        {'left': '1080px', 'top': '284px', 'width': '121px', 'height': '37px'},
        {'left': '1080px', 'top': '428px', 'width': '121px', 'height': '37px'},
        {'left': '1080px', 'top': '500px', 'width': '121px', 'height': '37px'},
        {'left': '1080px', 'top': '572px', 'width': '121px', 'height': '37px'},
        {'left': '1080px', 'top': '716px', 'width': '153px', 'height': '37px'},

        #{'left': '130px', 'top': '1004px', 'width': '121px', 'height': '37px'},
        {'left': '324px', 'top': '1004px', 'width': '121px', 'height': '37px'},
        {'left': '518px', 'top': '1004px', 'width': '121px', 'height': '37px'},
        {'left': '712px', 'top': '1004px', 'width': '121px', 'height': '37px'},
        #{'left': '906px', 'top': '1004px', 'width': '121px', 'height': '37px'},
        {'left': '1100px', 'top': '1004px', 'width': '121px', 'height': '37px'},
    ]
    _add_backgrounds(layout, black_backgrounds, 'black', '1px solid white', 8)

    # 8. ハンドバルブの画像 (z-index: 8)
    handvalve_h = [
        {'left': '1364px', 'top': '1136px'},
    ]
    handvalve_v = [
        {'left': '1336px', 'top': '1048px'},
        {'left': '1336px', 'top': '1176px'},
        {'left': '256px', 'top': '1112px'},
        {'left': '192px', 'top': '1176px'},
        #{'left': '304px', 'top': '1176px'},
        {'left': '498px', 'top': '1176px'},
        {'left': '692px', 'top': '1176px'},
        {'left': '886px', 'top': '1176px'},
        #{'left': '1080px', 'top': '1176px'},
        {'left': '1274px', 'top': '1176px'},
        
    ]
    _add_image(layout, handvalve_h, '/assets/images/hand_valve.png', '36px', '36px', 8)
    _add_image(layout, handvalve_v, '/assets/images/hand_valve_tate.png', '36px', '36px', 8)

    # 9. ポンプ 機器名 (z-index: 9)
    _add_device_name(layout, pump_list, offset_x=0, offset_y=-24, width='48px', color='black', z_index=9)
    # 9. センサー 機器名 (z-index: 9)
    _add_device_name(layout, pressure_sensor_list, offset_x=-4, offset_y=-24, width='48px', color='black', z_index=9)
    # 9. バルブ 機器名 (z-index: 9)
    _add_device_name(layout, top_valves, offset_x=0, offset_y=-24, width='48px', color='black', z_index=9)
    _add_device_name(layout, bottom_valves, offset_x=0, offset_y=-24, width='48px', color='black', z_index=9)

    # 11. 上部のバルブ (z-index: 11)
    for valve in diagram1_valve_indicators :
        layout.append(html.Img(
            id=valve['id'],
            src='/assets/images/valve_off.png',
            style={
                'position': 'absolute',
                'left': valve['left'],
                'top': valve['top'],
                'width': '48px', 'height': '36px',
                'zIndex': 11,
            }
        ))

    # センサー、ポンプ等のマークの生成 
    for item in diagram1_style_indicators:        
        # 1. ベーススタイルを取得
        base_style = BASE_STYLES_MAP[item['style_type']].copy()
        
        # 2. 座標情報で上書き
        base_style['left'] = item['left']
        base_style['top'] = item['top']
        
        # 3. 初期色を設定 (例: 初期状態は灰色)
        base_style['backgroundColor'] = 'gray'
        
        # コンポーネントの初期スタイルとして設定
        layout.append(html.Div(id=item['id'], style=base_style))


    # 16. 機器名称 (z-index: 16)
    text_list = [
        {'left': '324px', 'top': '44px', 'text': 'RF1 RF電源'},
        {'left': '324px', 'top': '64px', 'text': '伝送出力'},
        {'left': '324px', 'top': '164px', 'text': '反射出力'},
        {'left': '324px', 'top': '228px', 'text': '電圧'},
        {'left': '324px', 'top': '292px', 'text': '電流'},

        {'left': '324px', 'top': '396px', 'text': 'H1 ヒーター'},
        {'left': '324px', 'top': '416px', 'text': '温度'},
        {'left': '324px', 'top': '516px', 'text': 'H2 ヒーター'},
        {'left': '324px', 'top': '536px', 'text': '温度'},
        {'left': '324px', 'top': '636px', 'text': '----'},
        {'left': '324px', 'top': '656px', 'text': '温度過昇温'},
        
        {'left': '448px', 'top': '96px', 'text': 'W'},
        {'left': '448px', 'top': '132px', 'text': 'W'},
        {'left': '448px', 'top': '196px', 'text': 'W'},
        {'left': '448px', 'top': '260px', 'text': 'Vpp'},
        {'left': '448px', 'top': '324px', 'text': 'Arms'},

        {'left': '448px', 'top': '448px', 'text': '℃'},
        {'left': '448px', 'top': '484px', 'text': '℃'},
        {'left': '448px', 'top': '568px', 'text': '℃'},
        {'left': '448px', 'top': '604px', 'text': '℃'},
        {'left': '448px', 'top': '688px', 'text': '℃'},

        {'left': '564px', 'top': '44px', 'text': 'MAT1 マッチャー'},
        {'left': '564px', 'top': '64px', 'text': 'C1'},
        {'left': '564px', 'top': '128px', 'text': 'C2'},
        {'left': '564px', 'top': '192px', 'text': 'VDC'},
        {'left': '564px', 'top': '256px', 'text': '温度センサ'},

        {'left': '564px', 'top': '396px', 'text': 'SVM1 ヒーター昇降'},
        {'left': '564px', 'top': '416px', 'text': '位置'},
        {'left': '564px', 'top': '516px', 'text': '速度'},

        {'left': '688px', 'top': '96px', 'text': '%'},
        {'left': '688px', 'top': '160px', 'text': '%'},
        {'left': '688px', 'top': '224px', 'text': 'V'},
        {'left': '688px', 'top': '288px', 'text': '℃'},

        {'left': '688px', 'top': '448px', 'text': 'mm'},
        {'left': '688px', 'top': '484px', 'text': 'mm'},
        {'left': '688px', 'top': '548px', 'text': 'mm/s'},

        {'left': '1080px', 'top': '44px', 'text': 'IG1 チャンバー内圧'},
        {'left': '1080px', 'top': '116px', 'text': 'CM1 チャンバー内圧'},
        {'left': '1080px', 'top': '188px', 'text': 'PS1 エア元圧'},
        {'left': '1080px', 'top': '260px', 'text': 'PS3 チャンバー内圧'},
        {'left': '1080px', 'top': '404px', 'text': 'PS2 フォアライン圧力'},
        {'left': '1080px', 'top': '476px', 'text': 'PS4 ヒーター内圧'},
        {'left': '1080px', 'top': '548px', 'text': 'SVM2 開度調整弁'},
        {'left': '1080px', 'top': '692px', 'text': 'プラズマ点灯積算時間'},

        {'left': '1236px', 'top': '76px', 'text': 'Pa'},
        {'left': '1236px', 'top': '148px', 'text': 'Pa'},
        {'left': '1204px', 'top': '220px', 'text': 'kPa'},
        {'left': '1204px', 'top': '292px', 'text': 'kPa'},
        {'left': '1204px', 'top': '436px', 'text': 'kPa'},
        {'left': '1204px', 'top': '508px', 'text': 'kPa'},
        {'left': '1204px', 'top': '580px', 'text': '%'},

        {'left': '160px', 'top': '56px', 'text': 'G02'},
        {'left': '160px', 'top': '200px', 'text': 'G01'},
        {'left': '160px', 'top': '272px', 'text': 'G01'},
        {'left': '160px', 'top': '344px', 'text': 'N2'},

        {'left': '304px', 'top': '852px', 'text': 'N2'},
        {'left': '884px', 'top': '200px', 'text': 'G01'},
        {'left': '884px', 'top': '272px', 'text': 'G01'},
        {'left': '788px', 'top': '636px', 'text': 'N2'},
        {'left': '884px', 'top': '852px', 'text': 'N2'},

        #{'left': '130px', 'top': '960px', 'text': 'FLM1'},
        #{'left': '130px', 'top': '980px', 'text': 'RF電源 流量'},
        {'left': '324px', 'top': '960px', 'text': 'FLM2'},
        {'left': '324px', 'top': '980px', 'text': '自動整合器 流量'},
        {'left': '518px', 'top': '960px', 'text': 'FLM3'},
        {'left': '518px', 'top': '980px', 'text': '上部電源 流量'},
        {'left': '712px', 'top': '960px', 'text': 'FLM4'},
        {'left': '712px', 'top': '980px', 'text': 'チャンバ 流量'},
        #{'left': '906px', 'top': '960px', 'text': 'FLM5'},
        #{'left': '906px', 'top': '980px', 'text': 'チャンバ2 流量'},
        {'left': '1100px', 'top': '960px', 'text': 'FLM6'},
        {'left': '1100px', 'top': '980px', 'text': 'ヒーターステージ 流量'},
        #{'left': '254px', 'top': '1012px', 'text': 'L/min'},
        {'left': '448px', 'top': '1012px', 'text': 'L/min'},
        {'left': '642px', 'top': '1012px', 'text': 'L/min'},
        {'left': '836px', 'top': '1012px', 'text': 'L/min'},
        #{'left': '1030px', 'top': '1012px', 'text': 'L/min'},
        {'left': '1224px', 'top': '1012px', 'text': 'L/min'},
        #{'left': '240px', 'top': '1058px', 'text': 'FLM1'},
        {'left': '434px', 'top': '1058px', 'text': 'FLM2'},
        {'left': '628px', 'top': '1058px', 'text': 'FLM3'},
        {'left': '822px', 'top': '1058px', 'text': 'FLM4'},
        #{'left': '1016px', 'top': '1058px', 'text': 'FLM5'},
        {'left': '1210px', 'top': '1058px', 'text': 'FLM6'},
        {'left': '52px', 'top': '1080px', 'text': 'CHL1 チラー'},
        {'left': '84px', 'top': '1114px', 'text': 'ON'},
        {'left': '32px', 'top': '1248px', 'text': 'CL1 AMP'},
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