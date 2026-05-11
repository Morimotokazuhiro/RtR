import math

from dash import html
from constans import FormatSpecifier

# --------------------------------------------------------
# 数値表示のリスト
# コールバックで'children'を変更します
# --------------------------------------------------------
monitor_list = [
    # 白色のテキスト
    {'id': 'dg2_LAMP2_1', 'left': '320px', 'top': '88px', 'color': 'white', 'width': '121px', 'address': 6032, 'format': FormatSpecifier.F3_2_SIGNED},
    {'id': 'dg2_LAMP2r_1', 'left': '320px', 'top': '152px', 'color': 'white', 'width': '121px', 'address': 6120, 'format': FormatSpecifier.F3_2_SIGNED},
    {'id': 'dg2_EC2_1', 'left': '320px', 'top': '492px', 'color': 'white', 'width': '121px', 'address': 6028, 'format': FormatSpecifier.F3_2},
    {'id': 'dg2_SVM4_spd_1', 'left': '52px', 'top': '88px', 'color': 'white', 'width': '121px', 'address': 6104, 'format': FormatSpecifier.F3_1},
    {'id': 'dg2_SVM4_rpm_1', 'left': '52px', 'top': '188px', 'color': 'white', 'width': '121px', 'address': 6106, 'format': FormatSpecifier.F3_3},
    {'id': 'dg2_SVM4_acc_1', 'left': '52px', 'top': '252px', 'color': 'white', 'width': '121px', 'address': 6108, 'format': FormatSpecifier.F1_3},
    {'id': 'dg2_SVM4_dec_1', 'left': '52px', 'top': '352px', 'color': 'white', 'width': '121px', 'address': 6110, 'format': FormatSpecifier.F1_3},

    {'id': 'dg2_SVM3_spd_1', 'left': '1188px', 'top': '88px', 'color': 'white', 'width': '121px', 'address': 6096, 'format': FormatSpecifier.F3_1},
    {'id': 'dg2_SVM3_rpm_1', 'left': '1188px', 'top': '188px', 'color': 'white', 'width': '121px', 'address': 6098, 'format': FormatSpecifier.F3_3},
    {'id': 'dg2_SVM3_acc_1', 'left': '1188px', 'top': '252px', 'color': 'white', 'width': '121px', 'address': 6100, 'format': FormatSpecifier.F1_3},
    {'id': 'dg2_SVM3_dec_1', 'left': '1188px', 'top': '352px', 'color': 'white', 'width': '121px', 'address': 6102, 'format': FormatSpecifier.F1_3},
    {'id': 'dg2_LAMP1_1', 'left': '912px', 'top': '88px', 'color': 'white', 'width': '121px', 'address': 6030, 'format': FormatSpecifier.F3_2_SIGNED},
    {'id': 'dg2_LAMP1r_1', 'left': '912px', 'top': '152px', 'color': 'white', 'width': '121px', 'address': 6118, 'format': FormatSpecifier.F3_2_SIGNED},
    {'id': 'dg2_EC1_1', 'left': '964px', 'top': '492px', 'color': 'white', 'width': '121px', 'address': 6026, 'format': FormatSpecifier.F3_2},

    # シアンのテキスト
    {'id': 'dg2_EC2_2', 'left': '320px', 'top': '528px', 'color': 'cyan', 'width': '121px', 'address': 4022, 'data_index': 11,
     'format': FormatSpecifier.F3_1},
    {'id': 'dg2_SVM4_spd_2', 'left': '52px', 'top': '124px', 'color': 'cyan', 'width': '121px', 'address': 4042,'data_index': 21,
     'format': FormatSpecifier.F3_1},
    {'id': 'dg2_SVM4_acc_2', 'left': '52px', 'top': '288px', 'color': 'cyan', 'width': '121px', 'address': 4044, 'data_index': 22,
     'format': FormatSpecifier.F3_1},
    {'id': 'dg2_SVM4_dec_2', 'left': '52px', 'top': '388px', 'color': 'cyan', 'width': '121px', 'address': 4046, 'data_index': 23,
     'format': FormatSpecifier.F3_1},
    {'id': 'dg2_SVM4_spd_u_2', 'left': '52px', 'top': '452px', 'color': 'cyan', 'width': '121px', 'address': 4048, 'data_index': 24,
     'format': FormatSpecifier.F3_1},
    {'id': 'dg2_SVM4_spd_l_2', 'left': '52px', 'top': '516px', 'color': 'cyan', 'width': '121px', 'address': 4050, 'data_index': 25,
     'format': FormatSpecifier.F3_1},

     {'id': 'dg2_SVM3_spd_2', 'left': '1188px', 'top': '124px', 'color': 'cyan', 'width': '121px', 'address': 4032,'data_index': 16,
     'format': FormatSpecifier.F3_1},
    {'id': 'dg2_SVM3_acc_2', 'left': '1188px', 'top': '288px', 'color': 'cyan', 'width': '121px', 'address': 4034, 'data_index': 17,
     'format': FormatSpecifier.F3_1},
    {'id': 'dg2_SVM3_dec_2', 'left': '1188px', 'top': '388px', 'color': 'cyan', 'width': '121px', 'address': 4036, 'data_index': 18,
     'format': FormatSpecifier.F3_1},
    {'id': 'dg2_SVM3_spd_u_2', 'left': '1188px', 'top': '452px', 'color': 'cyan', 'width': '121px', 'address': 4038, 'data_index': 19,
     'format': FormatSpecifier.F3_1},
    {'id': 'dg2_SVM3_spd_l_2', 'left': '1188px', 'top': '516px', 'color': 'cyan', 'width': '121px', 'address': 4040, 'data_index': 20,
     'format': FormatSpecifier.F3_1},
    {'id': 'dg2_EC1_2', 'left': '964px', 'top': '528px', 'color': 'cyan', 'width': '121px', 'address': 4020, 'data_index': 10,
     'format': FormatSpecifier.F3_1},
]
# ID のリスト
diagram2_ids_children = [
    data['id'] for data in monitor_list
]
# 20px: モード設定用
BASE_20px_CIRCLE = {
    'position': 'absolute',
    'width': '20px', 'height': '20px',
    'borderRadius': '50%',
    'backgroundColor': 'lime',  # 仮の初期色
    'border': '1px solid white',
    'zIndex': 9,
}
# モード設定
mode_list = [
    {'id': 'dg2_SVM4_rt_mode_1','left': '60px', 'top': '588px', 'address': 876, 'name': '正転', 'reverse': False},
    {'id': 'dg2_SVM4_rt_mode_2','left': '144px', 'top': '588px', 'address': 876, 'name': '逆転', 'reverse': True},
    {'id': 'dg2_SVM4_con_mode_1','left': '60px', 'top': '652px', 'address': 878, 'name': '有効', 'reverse': False},
    {'id': 'dg2_SVM4_con_mode_2','left': '144px', 'top': '652px', 'address': 878, 'name': '無効', 'reverse': True},

    {'id': 'dg2_SVM3_rt_mode_1','left': '1196px', 'top': '588px', 'address': 872, 'name': '正転', 'reverse': False},
    {'id': 'dg2_SVM3_rt_mode_2','left': '1280px', 'top': '588px', 'address': 872, 'name': '逆転', 'reverse': True},
    {'id': 'dg2_SVM3_con_mode_1','left': '1196px', 'top': '652px', 'address': 874, 'name': '有効', 'reverse': False},
    {'id': 'dg2_SVM3_con_mode_2','left': '1280px', 'top': '652px', 'address': 874, 'name': '無効', 'reverse': True},

]


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
# 円の背景
def _add_circles(layout, circle_list, color, border_style, z_index):
    """汎用的な円形Div要素をレイアウトに追加するヘルパー関数"""
    for circle in circle_list:
        # 真円にするため、widthとheightは同じ値を使用することが前提
        layout.append(html.Div(style={
            'position': 'absolute',
            'left': circle['left'],
            'top': circle['top'],
            'width': circle['size'],
            'height': circle['size'],
            'backgroundColor': color,
            'border': border_style,
            'zIndex': z_index,
            'borderRadius': '50%', # ✨ この行を追加・変更 ✨
        }))
# 線の描写
def _add_lines_free(layout, line_list, color, thickness=2, style='solid', z_index=1):
    """
    開始点(x1, y1)と終了点(x2, y2)を指定して自由な線を描画するヘルパー関数。
    """
    # 線のスタイル定義 (CSSグラデーションで実現)
    line_styles = {
        'solid': {
            'backgroundColor': color,
            'backgroundImage': 'none',
        },
        'dashed': {
            'backgroundColor': 'transparent', # グラデーションを使うため背景は透明に
            # 水平方向の破線パターンを作成 (色 4px、透明 2px を繰り返す)
            'backgroundImage': f'linear-gradient(to right, {color} 4px, transparent 0%)',
            'backgroundSize': '6px 100%',
        },
        'dotted': {
            'backgroundColor': 'transparent',
            # 水平方向の点線パターンを作成 (色 2px、透明 4px を繰り返す)
            'backgroundImage': f'linear-gradient(to right, {color} 2px, transparent 0%)',
            'backgroundSize': '6px 100%', 
        }
    }
    selected_style = line_styles.get(style, line_styles['solid'])

    for line in line_list:
        # ピクセル値を取得（ここでは例としてpx単位を想定）
        try:
            x1 = int(line['start_x'].replace('px', ''))
            y1 = int(line['start_y'].replace('px', ''))
            x2 = int(line['end_x'].replace('px', ''))
            y2 = int(line['end_y'].replace('px', ''))
        except (KeyError, ValueError):
            continue

        length = math.hypot(x2 - x1, y2 - y1)
        angle_rad = math.atan2(y2 - y1, x2 - x1)
        angle_deg = math.degrees(angle_rad)

        # 基本スタイルと選択されたスタイルを結合
        base_style = {
            'position': 'absolute',
            'zIndex': z_index,
            'height': f'{thickness}px', 
            'width': f'{length}px',
            'left': f'{x1}px',
            'top': f'{y1}px', 
            'transformOrigin': '0 50%', 
            'transform': f'rotate({angle_deg}deg)',
        }
        
        # スタイルを上書き・追加
        final_style = {**base_style, **selected_style}

        # 斜め線の場合、グラデーションも回転させる必要あり
        if angle_deg != 0 and angle_deg != 180 and style != 'solid':
             # 線全体の回転角度に合わせて、グラデーションの方向も調整する
            # ただし、CSSグラデーションの回転角度は複雑なため、
            # 簡単な表現で妥協するか、より高度な背景設定が必要です。
            # ここではシンプルに、グラデーションの回転は省略します。
            # (斜め線の場合、破線/点線が少し歪んで見える可能性があることに注意)
             pass
        
        layout.append(html.Div(style=final_style))

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
                'fontSize': '16px',
                'fontWeight': 'bold',
                'color': item.get('name_color', color), # name_colorが定義されていればそれを使用、なければcolor
                'fontFamily': 'Meiryo UI',
                'zIndex': z_index,
            }
        ))

def create_diagram2_layout():
    # Content-1 (模式図エリア) のモード 2 用レイアウト
    layout = []

    # 6. 濃いグレーの背景 (z-index: 6)
    dark_gray_backgrounds = [
        {'left': '28px', 'top': '40px', 'width': '241px', 'height': '681px'},
        {'left': '296px', 'top': '40px', 'width': '241px', 'height': '157px'},
        {'left': '296px', 'top': '444px', 'width': '189px', 'height': '161px'},
        {'left': '888px', 'top': '40px', 'width': '241px', 'height': '157px'},
        {'left': '940px', 'top': '444px', 'width': '189px', 'height': '161px'},
        {'left': '1164px', 'top': '40px', 'width': '241px', 'height': '681px'},
    ]
    _add_backgrounds(layout, dark_gray_backgrounds, '#777777', '1px solid white', 6)

    # 6. 濃いグレーの背景 (z-index: 6)
    dark_gray_backgrounds_g = [
        {'left': '296px', 'top': '208px', 'width': '317px', 'height': '225px'},
        {'left': '812px', 'top': '208px', 'width': '317px', 'height': '225px'},
        {'left': '612px', 'top': '308px', 'width': '201px', 'height': '125px'},
    ]
    _add_backgrounds(layout, dark_gray_backgrounds_g, '#777777', 'none', 6)

    # 7. 薄いグレーの背景 (z-index: 7)
    light_gray_backgrounds = [
        {'left': '40px', 'top': '44px', 'width': '217px', 'height': '673px'},
        {'left': '308px', 'top': '44px', 'width': '217px', 'height': '149px'},
        {'left': '308px', 'top': '448px', 'width': '165px', 'height': '153px'},
        {'left': '900px', 'top': '44px', 'width': '217px', 'height': '149px'},
        {'left': '952px', 'top': '448px', 'width': '165px', 'height': '153px'},
        {'left': '1176px', 'top': '44px', 'width': '217px', 'height': '673px'},
    ]
    _add_backgrounds(layout, light_gray_backgrounds, '#DDE0E4', '1px solid #999999', 7)

    # 7. 薄いグレーの背景 (z-index: 7)
    light_gray_backgrounds_g = [
        {'left': '308px', 'top': '212px', 'width': '293px', 'height': '217px'},
        {'left': '824px', 'top': '212px', 'width': '293px', 'height': '217px'},
        {'left': '600px', 'top': '312px', 'width': '225px', 'height': '117px'},
    ]
    _add_backgrounds(layout, light_gray_backgrounds_g, '#DDE0E4', 'none', 7)

    # 8. 黒の背景 (z-index: 8)
    black_backgrounds = [
        {'left': '52px', 'top': '88px', 'width': '121px', 'height': '37px'},
        {'left': '52px', 'top': '124px', 'width': '121px', 'height': '37px'},
        {'left': '52px', 'top': '188px', 'width': '121px', 'height': '37px'},
        {'left': '52px', 'top': '252px', 'width': '121px', 'height': '37px'},
        {'left': '52px', 'top': '288px', 'width': '121px', 'height': '37px'},
        {'left': '52px', 'top': '352px', 'width': '121px', 'height': '37px'},
        {'left': '52px', 'top': '388px', 'width': '121px', 'height': '37px'},
        {'left': '52px', 'top': '452px', 'width': '121px', 'height': '37px'},
        {'left': '52px', 'top': '516px', 'width': '121px', 'height': '37px'},
        {'left': '52px', 'top': '580px', 'width': '169px', 'height': '37px'},
        {'left': '52px', 'top': '644px', 'width': '169px', 'height': '37px'},
        
        {'left': '320px', 'top': '88px', 'width': '121px', 'height': '37px'},
        {'left': '320px', 'top': '152px', 'width': '121px', 'height': '37px'},
        {'left': '320px', 'top': '492px', 'width': '121px', 'height': '37px'},
        {'left': '320px', 'top': '528px', 'width': '121px', 'height': '37px'},
        {'left': '912px', 'top': '88px', 'width': '121px', 'height': '37px'},
        {'left': '912px', 'top': '152px', 'width': '121px', 'height': '37px'},
        {'left': '964px', 'top': '492px', 'width': '121px', 'height': '37px'},
        {'left': '964px', 'top': '528px', 'width': '121px', 'height': '37px'},

        {'left': '1188px', 'top': '88px', 'width': '121px', 'height': '37px'},
        {'left': '1188px', 'top': '124px', 'width': '121px', 'height': '37px'},
        {'left': '1188px', 'top': '188px', 'width': '121px', 'height': '37px'},
        {'left': '1188px', 'top': '252px', 'width': '121px', 'height': '37px'},
        {'left': '1188px', 'top': '288px', 'width': '121px', 'height': '37px'},
        {'left': '1188px', 'top': '352px', 'width': '121px', 'height': '37px'},
        {'left': '1188px', 'top': '388px', 'width': '121px', 'height': '37px'},
        {'left': '1188px', 'top': '452px', 'width': '121px', 'height': '37px'},
        {'left': '1188px', 'top': '516px', 'width': '121px', 'height': '37px'},
        {'left': '1188px', 'top': '580px', 'width': '169px', 'height': '37px'},
        {'left': '1188px', 'top': '644px', 'width': '169px', 'height': '37px'},
    ]
    _add_backgrounds(layout, black_backgrounds, 'black', '1px solid white', 8)

    # 8. 薄いグレーのイラスト (z-index: 8)
    illusts = [
        {'left': '364px', 'top': '228px', 'width': '17px', 'height': '57px'},
        {'left': '1044px', 'top': '228px', 'width': '17px', 'height': '57px'},
    ]
    _add_backgrounds(layout, illusts, '#BBBBBB', '1px solid white', 8)

    circle_illusts = [
        {'left': '352px', 'top': '356px', 'size': '40px'},
        {'left': '456px', 'top': '356px', 'size': '32px'},
        {'left': '556px', 'top': '356px', 'size': '32px'},
        {'left': '832px', 'top': '356px', 'size': '32px'},
        {'left': '932px', 'top': '356px', 'size': '32px'},
        {'left': '1032px', 'top': '356px', 'size': '40px'},
    ]
    _add_circles(layout, circle_illusts, '#BBBBBB', '1px solid black', 8)

    transparent_circle_illusts = [
        {'left': '332px', 'top': '336px', 'size': '80px'},
        {'left': '1012px', 'top': '336px', 'size': '80px'},
    ]
    _add_circles(layout, transparent_circle_illusts, 'transparent', '1px dashed black', 8)

    # 8. 黒線のイラスト (z-index: 8)
    line_illusts = [
        {'start_x': '372px', 'start_y': '356px', 'end_x': '472px', 'end_y': '388px'},
        {'start_x': '472px', 'start_y': '388px', 'end_x': '572px', 'end_y': '356px'},
        {'start_x': '572px', 'start_y': '356px', 'end_x': '848px', 'end_y': '356px'},
        {'start_x': '848px', 'start_y': '356px', 'end_x': '948px', 'end_y': '388px'},
        {'start_x': '948px', 'start_y': '388px', 'end_x': '1048px', 'end_y': '356px'},
    ]
    _add_lines_free(layout, line_illusts, color='black', thickness=1, style='solid',z_index=8)

    dashed_line_illusts = [
        {'start_x': '368px', 'start_y': '324px', 'end_x': '372px', 'end_y': '284px'},
        {'start_x': '372px', 'start_y': '284px', 'end_x': '376px', 'end_y': '324px'},
        {'start_x': '1048px', 'start_y': '324px', 'end_x': '1052px', 'end_y': '284px'},
        {'start_x': '1052px', 'start_y': '284px', 'end_x': '1056px', 'end_y': '324px'},
    ]
    _add_lines_free(layout, dashed_line_illusts, color='black', thickness=1, style='dashed',z_index=8)

    # 9. モード設定のテキスト (z-index: 9)
    _add_device_name(layout, mode_list, offset_x=28, offset_y=0, width='40px', color='cyan', z_index=9)

    # センサー、ポンプ等のマークの生成 
    for item in mode_list:
        # 1. ベーススタイルを取得
        base_style = BASE_20px_CIRCLE.copy()
        
        # 2. 座標情報で上書き
        base_style['left'] = item['left']
        base_style['top'] = item['top']
        
        # 3. 初期色を設定 (例: 初期状態は灰色)
        base_style['backgroundColor'] = 'gray'
        
        # コンポーネントの初期スタイルとして設定
        layout.append(html.Div(id=item['id'], style=base_style))

    # 16. 機器名称 (z-index: 16)
    text_list = [
        {'left': '52px', 'top': '44px', 'text': 'SVM4'},
        {'left': '52px', 'top': '64px', 'text': 'フォイル搬送速度'},
        {'left': '52px', 'top': '164px', 'text': 'モーター回転数'},
        {'left': '52px', 'top': '228px', 'text': '加速時間'},
        {'left': '52px', 'top': '328px', 'text': '減速時間'},
        {'left': '52px', 'top': '428px', 'text': 'テンション制御速度上限'},
        {'left': '52px', 'top': '492px', 'text': 'テンション制御速度下限'},
        {'left': '52px', 'top': '556px', 'text': '回転方向'},
        {'left': '52px', 'top': '620px', 'text': 'テンション制御'},
        {'left': '176px', 'top': '96px', 'text': 'cm/min'},
        {'left': '176px', 'top': '132px', 'text': 'cm/min'},
        {'left': '176px', 'top': '196px', 'text': 'rpm'},
        {'left': '176px', 'top': '260px', 'text': 'sec'},
        {'left': '176px', 'top': '296px', 'text': 'sec'},
        {'left': '176px', 'top': '360px', 'text': 'sec'},
        {'left': '176px', 'top': '396px', 'text': 'sec'},
        {'left': '176px', 'top': '460px', 'text': 'cm/min'},
        {'left': '176px', 'top': '524px', 'text': 'cm/min'},

        {'left': '320px', 'top': '44px', 'text': 'LAMP2'},
        {'left': '320px', 'top': '64px', 'text': 'B室厚み'},
        {'left': '320px', 'top': '128px', 'text': 'B室ロール径'},
        {'left': '320px', 'top': '448px', 'text': 'EC2'},
        {'left': '320px', 'top': '468px', 'text': 'B室角度'},
        {'left': '912px', 'top': '44px', 'text': 'LAMP1'},
        {'left': '912px', 'top': '64px', 'text': 'A室厚み'},
        {'left': '912px', 'top': '128px', 'text': 'A室ロール径'},
        {'left': '964px', 'top': '448px', 'text': 'EC1'},
        {'left': '964px', 'top': '468px', 'text': 'A室角度'},
        {'left': '444px', 'top': '96px', 'text': 'mm'},
        {'left': '444px', 'top': '160px', 'text': 'mm'},
        {'left': '444px', 'top': '500px', 'text': '° '},
        {'left': '444px', 'top': '536px', 'text': '° '},
        {'left': '1036px', 'top': '96px', 'text': 'mm'},
        {'left': '1036px', 'top': '160px', 'text': 'mm'},
        {'left': '1088px', 'top': '500px', 'text': '° '},
        {'left': '1088px', 'top': '536px', 'text': '° '},

        {'left': '1188px', 'top': '44px', 'text': 'SVM3'},
        {'left': '1188px', 'top': '64px', 'text': 'フォイル搬送速度'},
        {'left': '1188px', 'top': '164px', 'text': 'モーター回転数'},
        {'left': '1188px', 'top': '228px', 'text': '加速時間'},
        {'left': '1188px', 'top': '328px', 'text': '減速時間'},
        {'left': '1188px', 'top': '428px', 'text': 'テンション制御速度上限'},
        {'left': '1188px', 'top': '492px', 'text': 'テンション制御速度下限'},
        {'left': '1188px', 'top': '556px', 'text': '回転方向'},
        {'left': '1188px', 'top': '620px', 'text': 'テンション制御'},
        {'left': '1312px', 'top': '96px', 'text': 'cm/min'},
        {'left': '1312px', 'top': '132px', 'text': 'cm/min'},
        {'left': '1312px', 'top': '196px', 'text': 'rpm'},
        {'left': '1312px', 'top': '260px', 'text': 'sec'},
        {'left': '1312px', 'top': '296px', 'text': 'sec'},
        {'left': '1312px', 'top': '360px', 'text': 'sec'},
        {'left': '1312px', 'top': '396px', 'text': 'sec'},
        {'left': '1312px', 'top': '460px', 'text': 'cm/min'},
        {'left': '1312px', 'top': '524px', 'text': 'cm/min'},

        {'left': '396px', 'top': '228px', 'text': 'LAMP2'},
        {'left': '396px', 'top': '312px', 'text': 'SVM4'},
        {'left': '456px', 'top': '396px', 'text': 'EC2'},
        {'left': '968px', 'top': '228px', 'text': 'LAMP1'},
        {'left': '968px', 'top': '312px', 'text': 'SVM3'},
        {'left': '932px', 'top': '396px', 'text': 'EC1'},
    ]
    _add_text(layout, text_list)

    # 17. モニター値 (z-index: 17)
    font_style = {'width': '121px', 'textAlign': 'center', 'fontWeight': 'bold'}
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
            **font_style
        }
        layout.append(html.Div(data['id'], id=data['id'], style=style))

    return layout