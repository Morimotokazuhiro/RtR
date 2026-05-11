from dash import html
from constans import BASE_STYLES_MAP

# monitor_data をグローバル変数として定義
TATE_MUKI = True
YOKO_MUKI = False
monitor_data = [
    # 垂直方向のバルブ
    {'id': 'pi_EXP1', 'left': '238px', 'top': '64px', 'address': 824, 'name': 'EXP1', 'muki': TATE_MUKI},
    {'id': 'pi_EXP2', 'left': '426px', 'top': '64px', 'address': 825, 'name': 'EXP2', 'muki': TATE_MUKI},
    {'id': 'pi_EXP3', 'left': '522px', 'top': '64px', 'address': 826, 'name': 'EXP3', 'muki': TATE_MUKI},
    {'id': 'pi_N2DP2', 'left': '90px', 'top': '120px', 'address': 859, 'name': 'N2DP2', 'muki': TATE_MUKI},
    {'id': 'pi_N2BP2', 'left': '178px', 'top': '120px', 'address': 834, 'name': 'N2BP2', 'muki': TATE_MUKI},
    {'id': 'pi_G6P2', 'left': '258px', 'top': '120px', 'address': 828, 'name': 'G6P2', 'muki': TATE_MUKI},
    {'id': 'pi_G1P2', 'left': '352px', 'top': '120px', 'address': 827, 'name': 'G1P2', 'muki': TATE_MUKI},
    {'id': 'pi_G2P2', 'left': '446px', 'top': '120px', 'address': 838, 'name': 'G2P2', 'muki': TATE_MUKI},
    {'id': 'pi_G3P2', 'left': '540px', 'top': '120px', 'address': 840, 'name': 'G3P2', 'muki': TATE_MUKI},
    {'id': 'pi_G7P2', 'left': '634px', 'top': '120px', 'address': 842, 'name': 'G7P2', 'muki': TATE_MUKI},
    {'id': 'pi_G4P2', 'left': '728px', 'top': '120px', 'address': 844, 'name': 'G4P2', 'muki': TATE_MUKI},
    {'id': 'pi_G5P2', 'left': '822px', 'top': '120px', 'address': 846, 'name': 'G5P2', 'muki': TATE_MUKI},

    {'id': 'pi_N2CP2', 'left': '90px', 'top': '220px', 'address': 858, 'name': 'N2CP2', 'muki': TATE_MUKI},
    {'id': 'pi_N2BP1', 'left': '90px', 'top': '304px', 'address': 835, 'name': 'N2BP1', 'muki': TATE_MUKI},
    {'id': 'pi_N2AP1', 'left': '178px', 'top': '304px', 'address': 835, 'name': 'N2AP1', 'muki': TATE_MUKI},
    {'id': 'pi_G6P1', 'left': '258px', 'top': '304px', 'address': 850, 'name': 'G6P1', 'muki': TATE_MUKI},
    {'id': 'pi_G1P1', 'left': '352px', 'top': '304px', 'address': 851, 'name': 'G1P1', 'muki': TATE_MUKI},
    {'id': 'pi_G2P1', 'left': '446px', 'top': '304px', 'address': 852, 'name': 'G2P1', 'muki': TATE_MUKI},
    {'id': 'pi_G3P1', 'left': '540px', 'top': '304px', 'address': 853, 'name': 'G3P1', 'muki': TATE_MUKI},
    {'id': 'pi_G7P1', 'left': '634px', 'top': '304px', 'address': 854, 'name': 'G7P1', 'muki': TATE_MUKI},
    {'id': 'pi_G4P1', 'left': '728px', 'top': '304px', 'address': 855, 'name': 'G4P1', 'muki': TATE_MUKI},
    {'id': 'pi_G5P1', 'left': '822px', 'top': '304px', 'address': 856, 'name': 'G5P1', 'muki': TATE_MUKI},

    {'id': 'pi_N2BP0', 'left': '90px', 'top': '456px', 'address': 849, 'name': 'N2BP0', 'muki': TATE_MUKI},
    {'id': 'pi_N2AP0', 'left': '178px', 'top': '456px', 'address': 849, 'name': 'N2AP0', 'muki': TATE_MUKI},
    {'id': 'pi_G1P0', 'left': '352px', 'top': '456px', 'address': 848, 'name': 'G1P0', 'muki': TATE_MUKI},
    {'id': 'pi_G2P0', 'left': '446px', 'top': '456px', 'address': 848, 'name': 'G2P0', 'muki': TATE_MUKI},
    {'id': 'pi_G3P0', 'left': '540px', 'top': '456px', 'address': 848, 'name': 'G3P0', 'muki': TATE_MUKI},
    {'id': 'pi_G4P0', 'left': '728px', 'top': '456px', 'address': 848, 'name': 'G4P0', 'muki': TATE_MUKI},
    {'id': 'pi_G5P0', 'left': '822px', 'top': '456px', 'address': 848, 'name': 'G5P0', 'muki': TATE_MUKI},
    # 水平方向のバルブ
    {'id': 'pi_G6P3', 'left': '288px', 'top': '236px', 'address': 836, 'name': 'G6P3', 'muki': YOKO_MUKI},
    {'id': 'pi_G1P3', 'left': '380px', 'top': '236px', 'address': 837, 'name': 'G1P3', 'muki': YOKO_MUKI},
    {'id': 'pi_G2P3', 'left': '476px', 'top': '236px', 'address': 839, 'name': 'G2P3', 'muki': YOKO_MUKI},
    {'id': 'pi_G3P3', 'left': '570px', 'top': '236px', 'address': 841, 'name': 'G3P3', 'muki': YOKO_MUKI},
    {'id': 'pi_G7P3', 'left': '664px', 'top': '236px', 'address': 843, 'name': 'G7P3', 'muki': YOKO_MUKI},
    {'id': 'pi_G4P3', 'left': '758px', 'top': '236px', 'address': 845, 'name': 'G4P3', 'muki': YOKO_MUKI},
    {'id': 'pi_G5P3', 'left': '852px', 'top': '236px', 'address': 847, 'name': 'G5P3', 'muki': YOKO_MUKI}
]
sensor_list = [
    {'id': 'pi_G6', 'left': '256px', 'top': '356px', 'address': 87,'style_type': 'BASE_24px', 'name_color': 'black', 'name': 'PT G6'},
    {'id': 'pi_G1', 'left': '350px', 'top': '356px', 'address': 82,'style_type': 'BASE_24px', 'name_color': 'black', 'name': 'PT G1'},
    {'id': 'pi_G2', 'left': '444px', 'top': '356px', 'address': 83,'style_type': 'BASE_24px', 'name_color': 'black', 'name': 'PT G2'},
    {'id': 'pi_G3', 'left': '538px', 'top': '356px', 'address': 84,'style_type': 'BASE_24px', 'name_color': 'black', 'name': 'PT G3'},
    {'id': 'pi_G7', 'left': '632px', 'top': '356px', 'address': 88,'style_type': 'BASE_24px', 'name_color': 'black', 'name': 'PT G7'},
    {'id': 'pi_G4', 'left': '726px', 'top': '356px', 'address': 85,'style_type': 'BASE_24px', 'name_color': 'black', 'name': 'PT G4'},
    {'id': 'pi_G5', 'left': '820px', 'top': '356px', 'address': 86,'style_type': 'BASE_24px', 'name_color': 'black', 'name': 'PT G5'},
]

# 配管のスタイルを定義する関数
def create_pipe_div(left, top, width=None, height=None, color='#ccc', z_index=1, thickness=4):
    style = {
        'position': 'absolute',
        'border-radius': '2px',
        'background-color': color,
        'border': 'none',
        'z-index': z_index
    }
    
    if width:
        style['width'] = f'{width}px'
        style['height'] = f'{thickness}px'
    
    if height:
        style['width'] = f'{thickness}px'
        style['height'] = f'{height}px'
    
    style['left'] = f'{left}px'
    style['top'] = f'{top}px'
    
    # 戻り値をリストにラップ
    return [html.Div(style=style)]

# 四角い線を定義する関数
def create_rectangle(left, top, width, height, color='#999999', z_index=1):
    style = {
        'position': 'absolute',
        'left': f'{left}px',
        'top': f'{top}px',
        'width': f'{width}px',
        'height': f'{height}px',
        'border': f'1px solid {color}',
        'z-index': z_index
    }
    # 戻り値をリストにラップ
    return [html.Div(style=style)]

# 垂直方向のバルブを生成する関数
def create_vertical_valve(id, left, top, name):
    return [
        html.Div(
            style={'position': 'absolute', 'left': left, 'top': top, 'height': '36px', 'width': '24px'},
            children=[
                html.Img(id=id, src='/assets/images/valve_off_tate.png', style={'height': '36px', 'width': '24px'}),
                html.P(name, style={
                    'position': 'absolute', 
                    'left': '-46px', 
                    'top': '0px', 
                    'width': '44px',
                    'font-family': 'Meiryo UI',
                    'font-size': '12px', 
                    'text-align': 'right',
                    'font-weight': 'bold',
                    'z-index': 13,
                    'white-space': 'nowrap'
                    })
            ]
        )
    ]

# 水平方向のバルブを生成する関数
def create_horizontal_valve(id, left, top, name):
    top_px = int(top.replace('px', ''))     # intに変換
    label_top = f'{top_px - 28}px'          # 文字列に戻す
    return [
        html.Div(
            style={'position': 'absolute', 'left': left, 'top': top, 'height': '24px', 'width': '36px'},
            children=[
                html.Img(id=id, src='/assets/images/valve_off.png', style={'height': '24px', 'width': '36px'}),
                html.P(name, style={
                    'position': 'absolute', 
                    'left': '0', 
                    'top': '-28px', 
                    'width': '44px',
                    'font-family': 'Meiryo UI',
                    'font-size': '12px', 
                    'font-weight': 'bold',
                    'z-index': 13,
                    'white-space': 'nowrap'
                    })
            ]
        )
    ]


# マスフローコントローラー（MFC）を生成
def create_mfc(left, top, name):
    label_width = 48
    return [
        html.Img(
            src='/assets/images/mfc_on_tate.png',
            style={
                'position': 'absolute',
                'left': f'{left}px',
                'top': f'{top}px',
                'width': '24px',
                'height': '36px',
                'z-index': 9
            }
        ),
        html.P(
            name,
            style={
                'position': 'absolute',
                'left': f'{left - label_width - 2}px',
                'top': f'{top}px',
                'font-family': 'Meiryo UI',
                'font-size': '12px',
                'font-weight': 'bold',
                'color': 'black',
                'width': f'{label_width}px',
                'text-align': 'right',
                'z-index': 9
            }
        )
    ]

# レギュレーター（RG）を生成
def create_regulator(left, top, name):
    label_width = 44
    return [
        html.Img(
            src='/assets/images/regulator_tate.png',
            style={
                'position': 'absolute',
                'left': f'{left}px',
                'top': f'{top}px',
                'width': '24px',
                'height': '36px',
                'z-index': 10
            }
        ),
        html.P(
            name,
            style={
                'position': 'absolute',
                'left': f'{left - label_width - 2}px',
                'top': f'{top - 4}px',
                'font-family': 'Meiryo UI',
                'font-size': '12px',
                'font-weight': 'bold',
                'color': 'black',
                'width': f'{label_width}px',
                'text-align': 'right',
                'z-index': 10
            }
        )
    ]

# ゲージ（円）を生成
def create_gauge(left, top, name, color):
    label_width = 44
    return [
        html.Div(
            style={
                'position': 'absolute',
                'left': f'{left}px',
                'top': f'{top}px',
                'width': '24px',
                'height': '24px',
                'border-radius': '50%',
                'background-color': color,
                'border': '1px solid white',
                'z-index': 11
            }
        ),
        html.P(
            name,
            style={
                'position': 'absolute',
                'left': f'{left - label_width - 2}px',
                'top': f'{top - 8}px',
                'font-family': 'Meiryo UI',
                'font-size': '12px',
                'font-weight': 'bold',
                'color': 'black',
                'width': f'{label_width}px',
                'text-align': 'right',
                'z-index': 11
            }
        )
    ]

# テキストラベルを生成
def create_text(left, top, text):
    return [
        html.P(
            text,
            style={
                'position': 'absolute',
                'left': f'{left}px',
                'top': f'{top}px',
                'font-family': 'Meiryo UI',
                'font-size': '12px',
                'font-weight': 'bold',
                'color': 'black',
                'z-index': 8
            }
        )
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
                'fontSize': '12px',
                'fontWeight': 'bold',
                'color': item.get('name_color', color), # name_colorが定義されていればそれを使用、なければcolor
                'fontFamily': 'Meiryo UI',
                'zIndex': z_index,
            }
        ))

# 全ての配管レイアウトとバルブを生成する関数
def create_pipe_layout():
    layout = []

    # 1. 四角の線 (z-index: 1)
    layout.extend(create_rectangle(left=28, top=108, width=185, height=393, z_index=1))
    layout.extend(create_rectangle(left=216, top=108, width=209, height=393, z_index=1))
    layout.extend(create_rectangle(left=428, top=108, width=93, height=393, z_index=1))
    layout.extend(create_rectangle(left=524, top=108, width=89, height=393, z_index=1))
    layout.extend(create_rectangle(left=616, top=108, width=297, height=393, z_index=1))

    # 2. 黒の配管 (z-index: 2)
    layout.extend(create_pipe_div(left=100, top=340, height=161, color='black', z_index=2))
    layout.extend(create_pipe_div(left=188, top=340, height=161, color='black', z_index=2))
    layout.extend(create_pipe_div(left=268, top=156, height=289, color='black', z_index=2))
    layout.extend(create_pipe_div(left=644, top=156, height=289, color='black', z_index=2))
    layout.extend(create_pipe_div(left=362, top=156, height=345, color='black', z_index=2))
    layout.extend(create_pipe_div(left=456, top=156, height=345, color='black', z_index=2))
    layout.extend(create_pipe_div(left=550, top=156, height=345, color='black', z_index=2))
    layout.extend(create_pipe_div(left=738, top=156, height=345, color='black', z_index=2))
    layout.extend(create_pipe_div(left=832, top=156, height=345, color='black', z_index=2))
    layout.extend(create_pipe_div(left=268, top=248, width=21, color='black', z_index=2))
    layout.extend(create_pipe_div(left=362, top=248, width=21, color='black', z_index=2))
    layout.extend(create_pipe_div(left=456, top=248, width=21, color='black', z_index=2))
    layout.extend(create_pipe_div(left=550, top=248, width=21, color='black', z_index=2))
    layout.extend(create_pipe_div(left=644, top=248, width=21, color='black', z_index=2))
    layout.extend(create_pipe_div(left=738, top=248, width=21, color='black', z_index=2))
    layout.extend(create_pipe_div(left=832, top=248, width=21, color='black', z_index=2))
    layout.extend(create_pipe_div(left=268, top=444, width=97, color='black', z_index=2))
    layout.extend(create_pipe_div(left=644, top=444, width=97, color='black', z_index=2))

    # 3. シアンの配管 (z-index: 3)
    layout.extend(create_pipe_div(left=248, top=12, height=97, color='cyan', z_index=3))
    layout.extend(create_pipe_div(left=436, top=12, height=97, color='cyan', z_index=3))
    layout.extend(create_pipe_div(left=532, top=12, height=97, color='cyan', z_index=3))
    layout.extend(create_pipe_div(left=16, top=188, width=85, color='cyan', z_index=3))

    # 4. エメラルドの配管 (z-index: 4)
    layout.extend(create_pipe_div(left=188, top=288, width=440, color='#009999', z_index=4))
    layout.extend(create_pipe_div(left=322, top=248, width=21, color='#009999', z_index=4))
    layout.extend(create_pipe_div(left=416, top=248, width=21, color='#009999', z_index=4))
    layout.extend(create_pipe_div(left=510, top=248, width=21, color='#009999', z_index=4))
    layout.extend(create_pipe_div(left=604, top=248, width=21, color='#009999', z_index=4))
    layout.extend(create_pipe_div(left=188, top=288, height=16, color='#009999', z_index=4))
    layout.extend(create_pipe_div(left=342, top=248, height=41, color='#009999', z_index=4))
    layout.extend(create_pipe_div(left=436, top=248, height=41, color='#009999', z_index=4))
    layout.extend(create_pipe_div(left=530, top=248, height=41, color='#009999', z_index=4))
    layout.extend(create_pipe_div(left=624, top=248, height=41, color='#009999', z_index=4))

    # 5. シアンブルーの配管 (z-index: 5)
    layout.extend(create_pipe_div(left=16, top=96, width=173, color='deepskyblue', z_index=5))
    layout.extend(create_pipe_div(left=100, top=272, width=810, color='deepskyblue', z_index=5))
    layout.extend(create_pipe_div(left=100, top=96, height=209, color='deepskyblue', z_index=5))
    layout.extend(create_pipe_div(left=188, top=96, height=178, color='deepskyblue', z_index=5))
    layout.extend(create_pipe_div(left=718, top=248, height=27, color='deepskyblue', z_index=5))
    layout.extend(create_pipe_div(left=812, top=248, height=27, color='deepskyblue', z_index=5))
    layout.extend(create_pipe_div(left=906, top=248, height=27, color='deepskyblue', z_index=5))
    layout.extend(create_pipe_div(left=698, top=248, width=21, color='deepskyblue', z_index=5))
    layout.extend(create_pipe_div(left=792, top=248, width=21, color='deepskyblue', z_index=5))
    layout.extend(create_pipe_div(left=886, top=248, width=21, color='deepskyblue', z_index=5))

    # 6. 紫の配管 (z-index: 6)
    layout.extend(create_pipe_div(left=16, top=56, width=817, color='blueviolet', z_index=6))
    layout.extend(create_pipe_div(left=362, top=56, height=65, color='blueviolet', z_index=6))
    layout.extend(create_pipe_div(left=456, top=56, height=65, color='blueviolet', z_index=6))
    layout.extend(create_pipe_div(left=550, top=56, height=65, color='blueviolet', z_index=6))
    layout.extend(create_pipe_div(left=738, top=56, height=65, color='blueviolet', z_index=6))
    layout.extend(create_pipe_div(left=832, top=56, height=65, color='blueviolet', z_index=6))

    # 7. ピンクの配管 (z-index: 7)
    layout.extend(create_pipe_div(left=16, top=32, width=629, color='magenta', z_index=7))
    layout.extend(create_pipe_div(left=268, top=32, height=90, color='magenta', z_index=7))
    layout.extend(create_pipe_div(left=644, top=32, height=90, color='magenta', z_index=7))

    # 8. テキスト (z-index: 8)
    layout.extend(create_text(left=16, top=4, text="G02 上部電極シールド"))
    layout.extend(create_text(left=16, top=28, text="G01 プロセスガス"))
    layout.extend(create_text(left=16, top=68, text="チャンバパージ/ヒーター"))
    layout.extend(create_text(left=4, top=160, text="ポンプ/ガスパージ"))
    layout.extend(create_text(left=224, top=4, text="N2"))
    layout.extend(create_text(left=412, top=4, text="N2"))
    layout.extend(create_text(left=508, top=4, text="N2"))
    layout.extend(create_text(left=104, top=496, text="N2 IN"))
    layout.extend(create_text(left=300, top=496, text="H2 IN"))
    layout.extend(create_text(left=452, top=496, text="CH4 IN"))
    layout.extend(create_text(left=544, top=496, text="O2 IN"))
    layout.extend(create_text(left=720, top=496, text="Ar IN"))
    layout.extend(create_text(left=812, top=496, text="N2 IN"))

    # 9. マスフロー (z-index: 9)
    layout.extend(create_mfc(left=256, top=172, name="MFC G6"))
    layout.extend(create_mfc(left=350, top=172, name="MFC G1"))
    layout.extend(create_mfc(left=444, top=172, name="MFC G2"))
    layout.extend(create_mfc(left=538, top=172, name="MFC G3"))
    layout.extend(create_mfc(left=632, top=172, name="MFC G7"))
    layout.extend(create_mfc(left=726, top=172, name="MFC G4"))
    layout.extend(create_mfc(left=820, top=172, name="MFC G5"))

    # 10. レギュレータ (z-index: 10)
    layout.extend(create_regulator(left=88, top=396, name="N2BRG"))
    layout.extend(create_regulator(left=176, top=396, name="N2ARG"))
    layout.extend(create_regulator(left=256, top=396, name="G6 RG"))
    layout.extend(create_regulator(left=350, top=396, name="G1 RG"))
    layout.extend(create_regulator(left=444, top=396, name="G2 RG"))
    layout.extend(create_regulator(left=538, top=396, name="G3 RG"))
    layout.extend(create_regulator(left=632, top=396, name="G7 RG"))
    layout.extend(create_regulator(left=726, top=396, name="G4 RG"))
    layout.extend(create_regulator(left=820, top=396, name="G5 RG"))

    # 11. ゲージG (z-index: 11)
    layout.extend(create_gauge(left=88, top=356, name="N2BG1", color="#777777"))
    layout.extend(create_gauge(left=176, top=356, name="N2AG1", color="#777777"))

    # 12. ゲージPT (z-index: 12)
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

    _add_device_name(layout, sensor_list, offset_x=-42, offset_y=4, width='200px', color='black', z_index=8)

    # layout.extend(create_gauge(left=256, top=356, name="PT G6", color="Lime"))
    # layout.extend(create_gauge(left=350, top=356, name="PT G1", color="Lime"))
    # layout.extend(create_gauge(left=444, top=356, name="PT G2", color="Lime"))
    # layout.extend(create_gauge(left=538, top=356, name="PT G3", color="Lime"))
    # layout.extend(create_gauge(left=632, top=356, name="PT G7", color="Lime"))
    # layout.extend(create_gauge(left=726, top=356, name="PT G4", color="Lime"))
    # layout.extend(create_gauge(left=820, top=356, name="PT G5", color="Lime"))
    
    # バルブをモニターデータから動的に生成
    for data in monitor_data:
        if data['muki']:    # 縦向き
            layout.extend(create_vertical_valve(data['id'], data['left'], data['top'], data['name']))
        else:
            layout.extend(create_horizontal_valve(data['id'], data['left'], data['top'], data['name']))
            
    return layout