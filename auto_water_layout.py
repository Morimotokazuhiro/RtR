from dash import html, dcc


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
            'reverse': data.get('reverse',False),
            'style_type': style_type, # 関数引数で受け取ったスタイルタイプ
        }
        indicators.append(indicator)
    return indicators

# 24px: センサー用
BASE_24px_CIRCLE = {
    'position': 'absolute',
    'width': '24px', 'height': '24px',
    'borderRadius': '50%',
    'backgroundColor': 'lime',  # 仮の初期色
    'border': '1px solid white',
    'zIndex': 15,
}
# 16px: IO信号用
BASE_16px_CIRCLE = {
    'position': 'absolute',
    'width': '16px', 'height': '16px',
    'borderRadius': '50%',
    'backgroundColor': 'lime',  # 仮の初期色
    'border': '1px solid white',
    'zIndex': 15,
}
# ベーススタイル辞書を定義 (参照用)
BASE_STYLES_MAP = {
    'BASE_24px': BASE_24px_CIRCLE,
    'BASE_16px': BASE_16px_CIRCLE,
}
# 改行文字コード（自由に変更可）
NEWLINE = '<br>'
# 流量計
sensor_list = [
    #{'id': 'FLM1', 'left': '300px', 'top': '124px', 'address': 89, 'name': 'FLM1'},
    {'id': 'FLM2', 'left': '384px', 'top': '124px', 'address': 90, 'name': 'FLM2'},
    {'id': 'FLM3', 'left': '468px', 'top': '124px', 'address': 91, 'name': 'FLM3'},
    {'id': 'FLM4', 'left': '552px', 'top': '124px', 'address': 92, 'name': 'FLM4'},
    #{'id': 'FLM5', 'left': '636px', 'top': '124px', 'address': 93, 'name': 'FLM5'},
    {'id': 'FLM6', 'left': '720px', 'top': '124px', 'address': 94, 'name': 'FLM6'},
    {'id': 'CL1', 'left': '52px', 'top': '324px', 'address': 42, 'name': 'CL1' + NEWLINE + 'AMP', 'reverse': True},
]
# IO信号
signal_list = [
    {'id': 'CHL1_ON', 'left': '32px', 'top': '168px', 'address': 27, 'name': 'ON'},
   # {'id': 'CHL1_ALM', 'left': '84px', 'top': '168px', 'address': 626, 'name': 'ALM'},
]
# コールバック用のindicatorsを一括生成
water_style_indicators = (
    make_indicators(sensor_list, 'BASE_24px') +
    make_indicators(signal_list, 'BASE_16px')
)

# --------------------------------------------------------
# 図形描画用のヘルパー関数
# --------------------------------------------------------
def _add_shape(layout, x, y, width, height, color, z_index, border_style=None, border_radius=None, transform=None):
    """図形のためのスタイル付きDiv要素を作成するヘルパー関数。"""
    _style = {
        'position': 'absolute',
        'left': x,
        'top': y,
        'width': width,
        'height': height,
        'backgroundColor': color,
        'zIndex': z_index,
        'border': border_style,
        'borderRadius': border_radius,
        'transform': transform,
    }
    layout.append(html.Div(style=_style))

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

def _add_device_name(layout, item_list, text_align, offset_x: int, offset_y: int):
    """
    機器名を描画するヘルパー関数。
    - offset_x/offset_y: 元の left/top からのオフセット (px)
    - width: テキストボックスの幅 (px, 'auto'など)
    """
    for item in item_list:
        offset2_y = 0
        
        # children 変数に html.P の子要素リストを格納する
        children = None

        #    offset2_y の設定と children の内容を確定させる
        if item['name'].startswith('CL'):
            offset2_y = -8      # 改行で2段表示の場合は、更にy座標を下げる
            parts = item['name'].split(NEWLINE)
            # 複数要素（Span, Br, Span）のリストを作成
            children = [
                html.Span(parts[0]),
                html.Br(),
                html.Span(parts[1])
            ]
        else:
            # 'CL'で始まらない場合は、単なるテキストをリストの単一要素として格納
            children = [item['name']]

        # 'left'と'top'の値からpxを除去し、オフセットを適用
        left_val = int(item['left'].replace('px', '')) + offset_x
        top_val = int(item['top'].replace('px', '')) + offset_y + offset2_y

        style = {
            'position': 'absolute',
            'left': f'{left_val}px',
            'top': f'{top_val}px',
            'width': '44px',
            'text-align': text_align,
            'fontFamily': 'Meiryo UI',
            'fontSize': '12px',
            'fontWeight': 'bold',
            'zIndex': 8
        }

        layout.append(html.P(children=children, style=style))
        
def _add_text(layout, item_list, z_index):
    """テキストのためのスタイル付きP要素を作成するヘルパー関数。"""
    for item in item_list:
        style = {
            'position': 'absolute',
            'left':item['left'],
            'top': item['top'],
            'fontFamily': 'Meiryo UI',
            'fontSize': item['font_size'],
            'fontWeight': 'bold',
            'zIndex': z_index,
            'width': item['width'],
            'textAlign': item['text_align'],
        }
        if item['rotate']:
            style['transform'] = 'rotate(-90deg)'
            style['transformOrigin'] = 'left bottom'

        layout.append(html.P(item['text'], style=style))

def create_water_layout():
    """Dashアプリケーションの完全なレイアウトを生成します。"""
    layout = []

    # 1. 四角の線 (z-index: 1)
    _add_shape(layout, '8px', '304px', '853px', '13px', 'transparent', 1, '1px solid #999999')

    # 2. 紫の配管 (z-index: 2)
    purple_v_pipes = [
        {'left': '216px', 'top': '168px', 'height': '128px'},
        {'left': '248px', 'top': '168px', 'height': '13px'},
        {'left': '248px', 'top': '216px', 'height': '13px'},
        {'left': '184px', 'top': '228px', 'height': '17px'},
        {'left': '184px', 'top': '280px', 'height': '13px'},
    ]
    purple_h_pipes = [
        {'left': '184px', 'top': '292px', 'width': '33px'},
    ]
    _add_vertical_pipes(layout, purple_v_pipes, 'blueviolet', 2)
    _add_horizontal_pipes(layout, purple_h_pipes, 'blueviolet', 2)

    # 3. 黒の配管 (z-index: 3)
    black_h_pipes = [
        {'left': '152px', 'top': '168px', 'width': '665px'},
        {'left': '152px', 'top': '228px', 'width': '705px'},
        {'left': '892px', 'top': '228px', 'width': '17px'},
    ]
    black_v_pipes = [
        #{'left': '312px', 'top': '16px', 'height': '153px'},
        {'left': '396px', 'top': '16px', 'height': '153px'},
        {'left': '480px', 'top': '16px', 'height': '153px'},
        {'left': '564px', 'top': '16px', 'height': '153px'},
        #{'left': '648px', 'top': '16px', 'height': '153px'},
        {'left': '732px', 'top': '16px', 'height': '153px'},
        {'left': '816px', 'top': '16px', 'height': '101px'},
        {'left': '816px', 'top': '152px', 'height': '20px'},
        #{'left': '312px', 'top': '228px', 'height': '17px'},
        #{'left': '312px', 'top': '280px', 'height': '57px'},
        {'left': '396px', 'top': '228px', 'height': '17px'},
        {'left': '396px', 'top': '280px', 'height': '57px'},
        {'left': '480px', 'top': '228px', 'height': '17px'},
        {'left': '480px', 'top': '280px', 'height': '57px'},
        {'left': '564px', 'top': '228px', 'height': '17px'},
        {'left': '564px', 'top': '280px', 'height': '57px'},
        #{'left': '648px', 'top': '228px', 'height': '17px'},
        #{'left': '648px', 'top': '280px', 'height': '57px'},
        {'left': '732px', 'top': '228px', 'height': '17px'},
        {'left': '732px', 'top': '280px', 'height': '57px'},
        {'left': '816px', 'top': '228px', 'height': '17px'},
        {'left': '816px', 'top': '280px', 'height': '57px'},
    ]
    _add_horizontal_pipes(layout, black_h_pipes, 'black', 3)
    _add_vertical_pipes(layout, black_v_pipes, 'black', 3)

    # 4. ハンドバルブの画像 (z-index: 4)
    handvalve_h = [
        {'left': '856px', 'top': '204px'},
    ]
    handvalve_v = [
        {'left': '804px', 'top': '116px'},
        {'left': '236px', 'top': '180px'},
        {'left': '172px', 'top': '244px'},
        #{'left': '300px', 'top': '244px'},
        {'left': '384px', 'top': '244px'},
        {'left': '468px', 'top': '244px'},
        {'left': '552px', 'top': '244px'},
        #{'left': '636px', 'top': '244px'},
        {'left': '720px', 'top': '244px'},
        {'left': '804px', 'top': '244px'},
    ]
    _add_image(layout, handvalve_h, '/assets/images/hand_valve.png', '36px', '36px', 4)
    _add_image(layout, handvalve_v, '/assets/images/hand_valve_tate.png', '36px', '36px', 4)

    # 5. 濃いグレーの背景 (z-index: 5)
    _add_shape(layout, '8px', '144px', '145px', '157px', '#777777', 5, '1px solid white')

    # 6. 薄いグレーの背景 (z-index: 6)
    _add_shape(layout, '20px', '148px', '121px', '149px', '#DDE0E4', 6, '1px solid #999999')

    # 7. センサー (z-index: 15)
    # 8. ON/ALM信号 (z-index: 15)

    # センサー、ポンプ等のマークの生成 
    for item in water_style_indicators:        
        # 1. ベーススタイルを取得
        base_style = BASE_STYLES_MAP[item['style_type']].copy()
        
        # 2. 座標情報で上書き
        base_style['left'] = item['left']
        base_style['top'] = item['top']
        
        # 3. 初期色を設定 (例: 初期状態は灰色)
        base_style['backgroundColor'] = 'gray'
        
        # コンポーネントの初期スタイルとして設定
        layout.append(html.Div(id=item['id'], style=base_style))

    # 8. 機器名 (z-index: 8)
    _add_device_name(layout, sensor_list, 'right', offset_x=-46, offset_y=-8)   # センサー名
    _add_device_name(layout, signal_list, 'left', offset_x=20, offset_y=-12)    # IO信号名
    
    # 9. テキスト (z-index: 9) - 静的なテキストは変更なし
    text_list = [
        {'left': '32px', 'top': '138px', 'text': 'CHL1 チラー', 'font_size': '12px', 'rotate': False, 'width': '80px', 'text_align': 'right'},
        #{'left': '308px', 'top': '116px', 'text': 'RF電源', 'font_size': '14px', 'rotate': True, 'width': '130px', 'text_align': 'right'},
        {'left': '392px', 'top': '116px', 'text': '自動整合器', 'font_size': '14px', 'rotate': True, 'width': '130px', 'text_align': 'right'},
        {'left': '476px', 'top': '116px', 'text': '上部電源', 'font_size': '14px', 'rotate': True, 'width': '130px', 'text_align': 'right'},
        {'left': '560px', 'top': '116px', 'text': 'チャンバ', 'font_size': '14px', 'rotate': True, 'width': '130px', 'text_align': 'right'},
        #{'left': '644px', 'top': '116px', 'text': 'チャンバ2', 'font_size': '14px', 'rotate': True, 'width': '130px', 'text_align': 'right'},
        {'left': '728px', 'top': '116px', 'text': 'ヒーターステージ', 'font_size': '14px', 'rotate': True, 'width': '130px', 'text_align': 'right'},
        {'left': '804px', 'top': '116px', 'text': 'チラーオーバーフロー', 'font_size': '14px', 'rotate': True, 'width': '130px', 'text_align': 'right'},
    ]
    _add_text(layout, text_list, 9)
        

    return layout