# -*- coding: utf-8 -*-
from dash import html
from enum import Enum 

from constans import FormatSpecifier, BASE_STYLES_MAP
    
# --------------------------------------------------------
# 数値表示のリスト
# コールバックで'children'を変更します
# --------------------------------------------------------
monitor_list = [
    # 白色のテキスト
    {'id': 'SVM4moni', 'left': '68px', 'top': '156px', 'color': 'white', 'width': '85px', 'address': 6104, 'format': FormatSpecifier.F3_2},
    {'id': 'LAMP2moni', 'left': '60px', 'top': '244px', 'color': 'white', 'width': '85px', 'address': 6032, 'format': FormatSpecifier.F3_2_SIGNED},
    {'id': 'EC2moni', 'left': '68px', 'top': '284px', 'color': 'white', 'width': '85px', 'address': 6028, 'format': FormatSpecifier.F3_2},    

    {'id': 'SVM2moni', 'left': '68px', 'top': '368px', 'color': 'white', 'width': '85px', 'address': 6094, 'format': FormatSpecifier.F3_2},
    {'id': 'RF1outmoni', 'left': '412px', 'top': '24px', 'color': 'white', 'width': '85px', 'address': 6004, 'format': FormatSpecifier.F4_1},
    {'id': 'RF1revmoni', 'left': '412px', 'top': '72px', 'color': 'white', 'width': '85px', 'address': 6006, 'format': FormatSpecifier.F4_1},
    {'id': 'MAT1C1moni', 'left': '420px', 'top': '136px', 'color': 'white', 'width': '85px', 'address': 6008, 'format': FormatSpecifier.F3_1},
    {'id': 'MAT1C2moni', 'left': '420px', 'top': '160px', 'color': 'white', 'width': '85px', 'address': 6010, 'format': FormatSpecifier.F3_1},
    {'id': 'MAT1DCmoni', 'left': '408px', 'top': '184px', 'color': 'white', 'width': '85px', 'address': 6012, 'format': FormatSpecifier.F3_1_SIGNED},
    {'id': 'MAT1TPmoni', 'left': '420px', 'top': '208px', 'color': 'white', 'width': '85px', 'address': 6014, 'format': FormatSpecifier.F3_1},
    {'id': 'H1moni', 'left': '372px', 'top': '284px', 'color': 'white', 'width': '65px', 'address': 6020, 'format': FormatSpecifier.F3_1},
    {'id': 'H2moni', 'left': '372px', 'top': '348px', 'color': 'white', 'width': '65px', 'address': 6022, 'format': FormatSpecifier.F3_1},
    {'id': 'CM1moni', 'left': '80px', 'top': '68px', 'color': 'white', 'width': '113px', 'address': 6002, 'format': FormatSpecifier.FE_NOTATION},
    {'id': 'IG1moni', 'left': '740px', 'top': '68px', 'color': 'white', 'width': '113px', 'address': 6000, 'format': FormatSpecifier.FE_NOTATION},

    {'id': 'SVM3moni', 'left': '700px', 'top': '156px', 'color': 'white', 'width': '85px', 'address': 6096, 'format': FormatSpecifier.F3_2},
    {'id': 'LAMP1moni', 'left': '692px', 'top': '244px', 'color': 'white', 'width': '85px', 'address': 6030, 'format': FormatSpecifier.F3_2_SIGNED},
    {'id': 'EC1moni', 'left': '700px', 'top': '284px', 'color': 'white', 'width': '85px', 'address': 6026, 'format': FormatSpecifier.F3_2},

    

    # シアンのテキスト
    {'id': 'SVM4sett', 'left': '68px', 'top': '180px', 'color': 'cyan', 'width': '85px', 'address': 5042, 'data_index': 21,
     'format': FormatSpecifier.F3_2},
    {'id': 'EC2sett', 'left': '68px', 'top': '308px', 'color': 'cyan', 'width': '85px', 'address': 5022, 'data_index': 11,
     'format': FormatSpecifier.F3_2},
    {'id': 'SVM2sett', 'left': '68px', 'top': '392px', 'color': 'cyan', 'width': '85px', 'address': 5028, 'data_index': 14,
     'format': FormatSpecifier.F3_2},
    {'id': 'RF1outset', 'left': '412px', 'top': '48px', 'color': 'cyan', 'width': '85px', 'address': 5000, 'data_index': 0,
     'format': FormatSpecifier.F4_1},
    {'id': 'H1sett', 'left': '440px', 'top': '284px', 'color': 'cyan', 'width': '65px', 'address': 5002, 'data_index': 1,
     'format': FormatSpecifier.F3_1},
    {'id': 'H2sett', 'left': '440px', 'top': '348px', 'color': 'cyan', 'width': '65px', 'address': 5004, 'data_index': 2,
     'format': FormatSpecifier.F3_1},
    {'id': 'SVM3sett', 'left': '700px', 'top': '180px', 'color': 'cyan', 'width': '85px', 'address': 5032,'data_index': 16,
     'format': FormatSpecifier.F3_2},
    {'id': 'EC1sett', 'left': '700px', 'top': '308px', 'color': 'cyan', 'width': '85px', 'address': 5020, 'data_index': 10,
     'format': FormatSpecifier.F3_2},
]
monitor2 = [
    {'id': 'Plasmoni', 'left': '66px', 'top': '472px', 'color': 'white', 'width': '113px', 'address': 6122, 'format': 'date'},
]

# ID のリスト
chamber_monitor_indicators = monitor_list + monitor2
chamber_ids_children = [
    data['id'] for data in monitor_list
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
            'reverse': data.get('reverse', False),
            'style_type': style_type, # 関数引数で受け取ったスタイルタイプ
        }
        indicators.append(indicator)
    return indicators


# idは必要に応じて、プレフィックス（接頭辞）「ch_」を付ける。（IDの重複はエラーになる）
# ポンプ
pump_list = [
    {'id': 'ch_TMP1', 'left': '544px', 'top': '376px', 'address': 903, 'name_color': 'white', 'name': 'TMP1'},
    {'id': 'ch_RP1', 'left': '696px', 'top': '452px', 'address': 861, 'name_color': 'black', 'name': 'RP1'},
]
# 圧力センサー # 番地47は仮
pressure_sensor_list = [
    {'id': 'ch_CM1','left': '236px', 'top': '68px', 'address': 47, 'name': 'CM1'},
    {'id': 'ch_PS3', 'left': '624px', 'top': '24px', 'address': 47, 'name': 'PS3'},
    {'id': 'ch_IG1', 'left': '624px', 'top': '68px', 'address': 47, 'name': 'IG1'},
    {'id': 'ch_PS4', 'left': '432px', 'top': '460px', 'address': 47, 'name': 'PS4'},
    {'id': 'ch_PS2', 'left': '692px', 'top': '400px', 'address': 47, 'name': 'PS2'},
]
# 扉センサー
door_sensor_list = [
    {'id': 'ch_PX1', 'left': '36px', 'top': '108px', 'address': 32, 'name': 'PX1'},
    {'id': 'ch_PX2', 'left': '668px', 'top': '108px', 'address': 33, 'name': 'PX2'},
]
# ON信号
on_signal_list = [
    {'id': 'ch_SVM4_ON', 'left': '60px', 'top': '208px', 'address': 65},
    #{'id': 'ch_SVM2_ON', 'left': '60px', 'top': '420px', 'address': 47},
    {'id': 'ch_RF1_ON', 'left': '376px', 'top': '100px', 'address': 15},
    #{'id': 'ch_SVM1_ON', 'left': '376px', 'top': '416px', 'address': 47},
    {'id': 'ch_SVM3_ON', 'left': '692px', 'top': '208px', 'address': 64},
    
]
# ALM信号
alm_signal_list = [
    {'id': 'ch_SVM4_ALM', 'left': '112px', 'top': '208px', 'address': 632, 'reverse': True},
    {'id': 'ch_SVM2_ALM', 'left': '60px', 'top': '420px', 'address': 630, 'reverse': True},
    {'id': 'ch_RF1_ALM', 'left': '376px', 'top': '236px', 'address': 628, 'reverse': True},
    {'id': 'ch_MAT1_ALM', 'left': '376px', 'top': '312px', 'address': 636, 'reverse': True},
    {'id': 'ch_H1_ALM', 'left': '376px', 'top': '376px', 'address': 634, 'reverse': True},
    {'id': 'ch_H2_ALM', 'left': '428px', 'top': '100px', 'address': 635, 'reverse': True},
    {'id': 'ch_SVM1_ALM', 'left': '376px', 'top': '416px', 'address': 629, 'reverse': True},
    {'id': 'ch_SVM3_ALM', 'left': '744px', 'top': '208px', 'address': 631, 'reverse': True},
]
# コールバック用のindicatorsを一括生成
chamber_style_indicators = (
    make_indicators(pump_list, 'BASE_36px') +
    make_indicators(pressure_sensor_list, 'BASE_24px') +
    make_indicators(door_sensor_list, 'BASE_24px') +
    make_indicators(on_signal_list, 'BASE_16px') +
    make_indicators(alm_signal_list, 'BASE_16px')
)

# --------------------------------------------------------
# バルブのリスト
# コールバックで'src'を変更します
# --------------------------------------------------------
# 上部のバルブ
YOKO_MUKI = False
top_valves = [
    {'id': 'ch_AV8', 'left': '284px', 'top': '24px', 'address': 829, 'name': 'AV8', 'muki': YOKO_MUKI},
    {'id': 'ch_AV2', 'left': '284px', 'top': '68px', 'address': 819, 'name': 'AV2', 'muki': YOKO_MUKI},
    {'id': 'ch_AV4', 'left': '284px', 'top': '112px', 'address': 822, 'name': 'AV4', 'muki': YOKO_MUKI},
    {'id': 'ch_AV6', 'left': '284px', 'top': '156px', 'address': 823, 'name': 'AV6', 'muki': YOKO_MUKI},
    {'id': 'ch_AV7', 'left': '284px', 'top': '288px', 'address': 817, 'name': 'AV7', 'muki': YOKO_MUKI},
    {'id': 'ch_AV1', 'left': '564px', 'top': '68px', 'address': 818, 'name': 'AV1', 'muki': YOKO_MUKI},
    {'id': 'ch_AV3', 'left': '564px', 'top': '112px', 'address': 820, 'name': 'AV3', 'muki': YOKO_MUKI},
    {'id': 'ch_AV5', 'left': '564px', 'top': '156px', 'address': 821, 'name': 'AV5', 'muki': YOKO_MUKI},
]
# 下部のバルブ 
bottom_valves = [
    {'id': 'ch_AV12', 'left': '420px', 'top': '508px', 'address': 833, 'name': 'AV12', 'muki': YOKO_MUKI},
    {'id': 'ch_AV09', 'left': '624px', 'top': '352px', 'address': 830, 'name': 'AV09', 'muki': YOKO_MUKI},
    {'id': 'ch_AV02', 'left': '624px', 'top': '400px', 'address': 814, 'name': 'AV02', 'muki': YOKO_MUKI},
    {'id': 'ch_AV01', 'left': '624px', 'top': '460px', 'address': 996, 'name': 'AV01', 'muki': YOKO_MUKI},
    {'id': 'ch_AV11', 'left': '624px', 'top': '508px', 'address': 832, 'name': 'AV11', 'muki': YOKO_MUKI},
    {'id': 'ch_AV10', 'left': '696px', 'top': '508px', 'address': 831, 'name': 'AV10', 'muki': YOKO_MUKI},
]

# 3. 'src' プロパティを更新する為の辞書
# (コールバックでid、addressを参照し、画像のsrcを変更する)
chamber_src_indicators = (
    top_valves +
    bottom_valves
)

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
                'fontSize': '12px',
                'fontWeight': 'bold',
                'color': item.get('name_color', color), # name_colorが定義されていればそれを使用、なければcolor
                'fontFamily': 'Meiryo UI',
                'zIndex': z_index,
            }
        ))

def _add_signal_label(layout, item_list, text: str, offset_x: int, offset_y: int, z_index: int):
    """
    ON/ALM信号などの固定テキストラベルを描画するヘルパー関数。
    """
    for item in item_list:
        # 'left'と'top'の値からpxを除去し、オフセットを適用
        left_val = int(item['left'].replace('px', '')) + offset_x
        top_val = int(item['top'].replace('px', '')) + offset_y
        
        layout.append(html.Div(
            text,
            style={
                'position': 'absolute',
                'left': f'{left_val}px',
                'top': f'{top_val}px',
                'fontSize': '12px',
                'fontWeight': 'bold',
                'color': 'black',
                'fontFamily': 'Meiryo UI',
                'zIndex': z_index,
            }
        ))


def create_chamber_layout():
    # フォントの幅に合わせたスタイルを定義
    font_styles = {
        '65px': {'width': '65px', 'textAlign': 'center', 'fontWeight': 'bold'},
        '85px': {'width': '85px', 'textAlign': 'center', 'fontWeight': 'bold'},
        '113px': {'width': '113px', 'textAlign': 'center', 'fontWeight': 'bold'}
    }

    """
    パイプラインのレイアウトを生成します。
    すべての図形、テキスト、および画像を絶対位置で配置します。
    """
    layout = []

    # 1. 黒の配管 (z-index: 1)
    black_h_pipes = [
        {'left': '320px', 'top': '36px', 'width': '33px'},
        {'left': '320px', 'top': '80px', 'width': '33px'},
        {'left': '260px', 'top': '80px', 'width': '25px'},
        {'left': '320px', 'top': '124px', 'width': '33px'},
        {'left': '320px', 'top': '168px', 'width': '33px'},
        {'left': '320px', 'top': '300px', 'width': '33px'},
        {'left': '548px', 'top': '36px', 'width': '77px'},
        {'left': '532px', 'top': '80px', 'width': '33px'},
        {'left': '600px', 'top': '80px', 'width': '25px'},
        {'left': '532px', 'top': '124px', 'width': '33px'},
        {'left': '532px', 'top': '168px', 'width': '33px'},
        {'left': '592px', 'top': '364px', 'width': '33px'},
        {'left': '592px', 'top': '412px', 'width': '33px'},
        {'left': '660px', 'top': '412px', 'width': '33px'},
        {'left': '456px', 'top': '472px', 'width': '25px'},
        {'left': '504px', 'top': '472px', 'width': '121px'},
        {'left': '660px', 'top': '472px', 'width': '101px'},
        {'left': '456px', 'top': '520px', 'width': '169px'},
        {'left': '660px', 'top': '520px', 'width': '37px'},
    ]
    black_v_pipes = [
        {'left': '548px', 'top': '36px', 'height': '45px'},
        {'left': '480px', 'top': '440px', 'height': '81px'},
        {'left': '504px', 'top': '440px', 'height': '35px'},
        {'left': '676px', 'top': '412px', 'height': '109px'},
    ]
    _add_horizontal_pipes(layout, black_h_pipes, 'black', 1)
    _add_vertical_pipes(layout, black_v_pipes, 'black', 1)

    # 2. ピンクの配管 (z-index: 2)
    pink_h_pipes = [
        {'left': '236px', 'top': '36px', 'width': '49px'},
    ]
    _add_horizontal_pipes(layout, pink_h_pipes, 'magenta', 2)

    # 3. 紫の配管 (z-index: 3)
    purple_h_pipes = [
        {'left': '236px', 'top': '124px', 'width': '49px'},
        {'left': '236px', 'top': '168px', 'width': '49px'},
        {'left': '600px', 'top': '124px', 'width': '49px'},
        {'left': '600px', 'top': '168px', 'width': '49px'},
    ]
    _add_horizontal_pipes(layout, purple_h_pipes, 'blueviolet', 3)

    # 4. シアンの配管 (z-index: 4)
    cyan_h_pipes = [
        {'left': '660px', 'top': '364px', 'width': '49px'},
        {'left': '732px', 'top': '520px', 'width': '49px'},
    ]
    _add_horizontal_pipes(layout, cyan_h_pipes, 'cyan', 4)

    # 5. シアンブルーの配管 (z-index: 5)
    deepskyblue_h_pipes = [
        {'left': '236px', 'top': '300px', 'width': '49px'},
        {'left': '372px', 'top': '520px', 'width': '49px'},
    ]
    _add_horizontal_pipes(layout, deepskyblue_h_pipes, 'deepskyblue', 5)

    # 6. 濃いグレーの背景 (z-index: 6)
    dark_gray_backgrounds = [
        {'left': '36px', 'top': '452px', 'width': '181px', 'height': '53px'},
        {'left': '8px', 'top': '48px', 'width': '221px', 'height': '53px'},
        {'left': '216px', 'top': '212px', 'width': '453px', 'height': '41px'},
        {'left': '532px', 'top': '336px', 'width': '61px', 'height': '89px'},
        {'left': '36px', 'top': '136px', 'width': '181px', 'height': '205px'},
        {'left': '36px', 'top': '348px', 'width': '181px', 'height': '97px'},
        {'left': '352px', 'top': '4px', 'width': '181px', 'height': '437px'},
        {'left': '668px', 'top': '48px', 'width': '221px', 'height': '53px'},
        {'left': '668px', 'top': '136px', 'width': '181px', 'height': '205px'},
    ]
    _add_backgrounds(layout, dark_gray_backgrounds, '#777777', '1px solid white', 6)

    # 7. 薄いグレーの背景 (z-index: 7)
    light_gray_backgrounds = [
        {'left': '48px', 'top': '456px', 'width': '157px', 'height': '45px'},
        {'left': '20px', 'top': '52px', 'width': '197px', 'height': '45px'},
        {'left': '48px', 'top': '140px', 'width': '157px', 'height': '197px'},
        {'left': '48px', 'top': '352px', 'width': '157px', 'height': '89px'},
        {'left': '364px', 'top': '8px', 'width': '157px', 'height': '113px'},
        {'left': '364px', 'top': '120px', 'width': '157px', 'height': '137px'},
        {'left': '364px', 'top': '268px', 'width': '157px', 'height': '129px'},
        {'left': '364px', 'top': '396px', 'width': '157px', 'height': '41px'},
        {'left': '680px', 'top': '52px', 'width': '197px', 'height': '45px'},
        {'left': '680px', 'top': '140px', 'width': '157px', 'height': '197px'},
    ]
    _add_backgrounds(layout, light_gray_backgrounds, '#DDE0E4', '1px solid #999999', 7)

    # 8. ポンプ 機器名 (z-index: 8)
    # 元のロジック: 'left': f'calc({pump["left"]} + 0px)', 'top': f'calc({pump["top"]} - 18px)', 'width': '36px', 'textAlign': 'center'
    _add_device_name(layout, pump_list, offset_x=0, offset_y=-18, width='36px', color='black', z_index=8)

    # 9. 圧力センサー 機器名 (z-index: 9)
    # 元のロジック: 'left': sensor['left'], 'top': f'calc({sensor["top"]} - 18px)', 'width': '24px', 'textAlign': 'center'
    _add_device_name(layout, pressure_sensor_list, offset_x=0, offset_y=-18, width='24px', color='black', z_index=9)

    # 10. 扉センサー 機器名 (z-index: 10)
    # 元のロジック: 'left': f'calc({sensor["left"]} + 28px)', 'top': f'calc({sensor["top"]} + 4px)', 'width': 'auto', 'textAlign': 'left' (デフォルト)
    _add_device_name(layout, door_sensor_list, offset_x=28, offset_y=4, width='auto', color='black', z_index=10)


    # 11. 上部のバルブ (z-index: 11)
    for valve in top_valves:
        layout.append(html.Img(
            id=valve['id'],
            src='/assets/images/valve_off.png',
            style={
                'position': 'absolute',
                'left': valve['left'],
                'top': valve['top'],
                'width': '36px', 'height': '24px',
                'zIndex': 11,
            }
        ))

    # 12. 下部のバルブ (z-index: 12)
    for valve in bottom_valves:
        layout.append(html.Img(
            id=valve['id'],
            src='/assets/images/valve_off.png',
            style={
                'position': 'absolute',
                'left': valve['left'],
                'top': valve['top'],
                'width': '36px', 'height': '24px',
                'zIndex': 12,
            }
        ))

    # 機器名部分
    # 元のロジック: 'left': f'calc({valve["left"]} + 4px)', 'top': f'calc({valve["top"]} - 18px)', 'width': 'auto', 'textAlign': 'left' (デフォルト)
    _add_device_name(layout, top_valves, offset_x=4, offset_y=-18, width='auto', color='black', z_index=11)
    
    # 元のロジック: 'left': valve['left'], 'top': f'calc({valve["top"]} - 18px)', 'width': '36px', 'textAlign': 'center'
    _add_device_name(layout, bottom_valves, offset_x=0, offset_y=-18, width='36px', color='black', z_index=12)

    # 13. ON信号 機器名 (z-index: 13)
    # 元のロジック: 'left': f'calc({signal["left"]} + 20px)', 'top': signal['top']
    _add_signal_label(layout, on_signal_list, 'ON', offset_x=20, offset_y=0, z_index=13)

    # 14. ALM信号 機器名 (z-index: 14)
    # 元のロジック: 'left': f'calc({signal["left"]} + 20px)', 'top': signal['top']
    _add_signal_label(layout, alm_signal_list, 'ALM', offset_x=20, offset_y=0, z_index=14)



    # センサー、ポンプ等のマークの生成 
    for item in chamber_style_indicators:        
        # 1. ベーススタイルを取得
        base_style = BASE_STYLES_MAP[item['style_type']].copy()
        
        # 2. 座標情報で上書き
        base_style['left'] = item['left']
        base_style['top'] = item['top']
        
        # 3. 初期色を設定 (例: 初期状態は灰色)
        base_style['backgroundColor'] = 'gray'
        
        # コンポーネントの初期スタイルとして設定
        layout.append(html.Div(id=item['id'], style=base_style))
        
    # 15. 黒の背景 (z-index: 15)
    black_backgrounds = [
        {'left': '60px', 'top': '472px', 'width': '113px', 'height': '25px'},
        {'left': '72px', 'top': '68px', 'width': '113px', 'height': '25px'},
        {'left': '60px', 'top': '156px', 'width': '85px', 'height': '25px'},
        {'left': '60px', 'top': '180px', 'width': '85px', 'height': '25px'},
        {'left': '60px', 'top': '244px', 'width': '85px', 'height': '25px'},
        {'left': '60px', 'top': '284px', 'width': '85px', 'height': '25px'},
        {'left': '60px', 'top': '308px', 'width': '85px', 'height': '25px'},
        {'left': '60px', 'top': '368px', 'width': '85px', 'height': '25px'},
        {'left': '60px', 'top': '392px', 'width': '85px', 'height': '25px'},
        
        {'left': '404px', 'top': '24px', 'width': '85px', 'height': '25px'},
        {'left': '404px', 'top': '48px', 'width': '85px', 'height': '25px'},
        {'left': '404px', 'top': '72px', 'width': '85px', 'height': '25px'},
        {'left': '404px', 'top': '136px', 'width': '85px', 'height': '25px'},
        {'left': '404px', 'top': '160px', 'width': '85px', 'height': '25px'},
        {'left': '404px', 'top': '184px', 'width': '85px', 'height': '25px'},
        {'left': '404px', 'top': '208px', 'width': '85px', 'height': '25px'},
        {'left': '368px', 'top': '284px', 'width': '65px', 'height': '25px'},
        {'left': '436px', 'top': '284px', 'width': '65px', 'height': '25px'},
        {'left': '368px', 'top': '348px', 'width': '65px', 'height': '25px'},
        {'left': '436px', 'top': '348px', 'width': '65px', 'height': '25px'},
        
        {'left': '732px', 'top': '68px', 'width': '113px', 'height': '25px'},
        {'left': '692px', 'top': '156px', 'width': '85px', 'height': '25px'},
        {'left': '692px', 'top': '180px', 'width': '85px', 'height': '25px'},
        {'left': '692px', 'top': '244px', 'width': '85px', 'height': '25px'},
        {'left': '692px', 'top': '284px', 'width': '85px', 'height': '25px'},
        {'left': '692px', 'top': '308px', 'width': '85px', 'height': '25px'},
    ]

    _add_backgrounds(layout, black_backgrounds, 'black', '1px solid white', 15)

    # 16. 機器名称 (z-index: 16)
    device_names = [
        {'left': '60px', 'top': '458px', 'text': 'プラズマ点灯積算時間'},
        {'left': '28px', 'top': '52px', 'text': 'CM1 チャンバー内圧'},
        {'left': '60px', 'top': '142px', 'text': 'SVM4'},
        {'left': '60px', 'top': '230px', 'text': 'LAMP2 変位センサ'},
        {'left': '60px', 'top': '270px', 'text': 'EC2 B室角度'},
        {'left': '60px', 'top': '354px', 'text': 'SVM2'},
        {'left': '192px', 'top': '72px', 'text': 'Pa'},
        {'left': '148px', 'top': '160px', 'text': 'cm/min'},
        {'left': '148px', 'top': '184px', 'text': 'cm/min'},
        {'left': '148px', 'top': '248px', 'text': 'mm'},
        {'left': '148px', 'top': '288px', 'text': '°'},
        {'left': '148px', 'top': '312px', 'text': '°'},
        {'left': '148px', 'top': '372px', 'text': '%'},
        {'left': '148px', 'top': '396px', 'text': '%'},
        
        {'left': '376px', 'top': '10px', 'text': 'RF1 RF電源'},
        {'left': '376px', 'top': '122px', 'text': 'MAT1 マッチャー'},
        {'left': '376px', 'top': '270px', 'text': 'H1 ヒーター'},
        {'left': '376px', 'top': '334px', 'text': 'H2 ヒーター'},
        {'left': '376px', 'top': '398px', 'text': 'SVM1'},
        {'left': '376px', 'top': '28px', 'text': 'Out'},
        {'left': '376px', 'top': '76px', 'text': 'Rev'},
        {'left': '376px', 'top': '140px', 'text': 'C1'},
        {'left': '376px', 'top': '164px', 'text': 'C2'},
        {'left': '368px', 'top': '188px', 'text': 'VDC'},
        {'left': '368px', 'top': '212px', 'text': 'Temp'},
        {'left': '492px', 'top': '28px', 'text': 'W'},
        {'left': '492px', 'top': '52px', 'text': 'W'},
        {'left': '492px', 'top': '76px', 'text': 'W'},
        {'left': '492px', 'top': '140px', 'text': '%'},
        {'left': '492px', 'top': '164px', 'text': '%'},
        {'left': '492px', 'top': '188px', 'text': 'V'},
        {'left': '492px', 'top': '212px', 'text': '℃'},
        {'left': '504px', 'top': '288px', 'text': '℃'},
        {'left': '504px', 'top': '352px', 'text': '℃'},
        
        
        {'left': '692px', 'top': '54px', 'text': 'IG1 チャンバー内圧'},
        {'left': '692px', 'top': '142px', 'text': 'SVM3'},
        {'left': '692px', 'top': '230px', 'text': 'LAMP1 変位センサ'},
        {'left': '692px', 'top': '270px', 'text': 'EC1 A室角度'},
        {'left': '852px', 'top': '72px', 'text': 'Pa'},
        {'left': '780px', 'top': '160px', 'text': 'cm/min'},
        {'left': '780px', 'top': '184px', 'text': 'cm/min'},
        {'left': '780px', 'top': '248px', 'text': 'mm'},
        {'left': '780px', 'top': '288px', 'text': '°'},
        {'left': '780px', 'top': '312px', 'text': '°'},

        {'left': '236px', 'top': '20px', 'text': 'G02'},
        {'left': '236px', 'top': '108px', 'text': 'G01'},
        {'left': '236px', 'top': '152px', 'text': 'G01'},
        {'left': '236px', 'top': '284px', 'text': 'N2'},
        {'left': '372px', 'top': '504px', 'text': 'N2'},
        {'left': '624px', 'top': '108px', 'text': 'G01'},
        {'left': '624px', 'top': '152px', 'text': 'G01'},
        {'left': '688px', 'top': '348px', 'text': 'N2'},
        {'left': '760px', 'top': '504px', 'text': 'N2'},
    ]
    for name in device_names:
        layout.append(html.Div(
            name['text'],
            style={
                'position': 'absolute',
                'left': name['left'],
                'top': name['top'],
                'fontSize': '12px',
                'fontWeight': 'bold',
                'color': 'black',
                'fontFamily': 'Meiryo UI',
                'zIndex': 16,
            }
        ))
    
    # 17. モニター値 (z-index: 17)
    for data in chamber_monitor_indicators:
        # 'top'の文字列から数値を取り出し、計算する
        top_value = int(data['top'].replace('px', '')) + 4
        style = {
            'position': 'absolute',
            'left': data['left'],
            'top': f'{top_value}px', # 'top': f'calc({data["top"]} + 2px)'の書式はCSS不可
            'fontSize': '18px',
            'color': data['color'],
            'zIndex': 17,
            **font_styles[data['width']]
        }
        layout.append(html.Div(data['id'], id=data['id'], style=style))

    return layout
