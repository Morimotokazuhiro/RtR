from dash import html, dcc

MODAL_STYLE = {
    'display': 'none',
    'position': 'fixed',
    'top': 0, 'left': 0, 'right': 0, 'bottom': 0,
    'backgroundColor': 'rgba(0,0,0,0.5)', # 背景を暗くする
    'display': 'none', # 初期状態は非表示
    'justifyContent': 'center',
    'alignItems': 'center',
    'zIndex': 1000, # 他の要素より手前に表示
}

def create_setting_modal(layout, op_id):
    """
    設定値入力用のモーダルウィンドウとデータを保持するdcc.Storeを共通定義する。
    """
    id = f'setting-modal{op_id}'
    store_id = f'modal-data-store{op_id}'
    display_id = f'modal-current-display{op_id}'
    input_id = f'modal-input{op_id}'
    ok_button_id = f'modal-ok-button{op_id}'
    cancel_button_id = f'modal-cancel-button{op_id}'

    # ポップアップ用のレイアウト
    layout.extend([
        # どの設定値がクリックされたか、現在の表示値を保持するStore
        dcc.Store(id=store_id, data={'id': None, 'value': None}),
        
        # モーダルウィンドウ本体
        html.Div(
            id=id,
            children=[
                html.Div([
                    html.H4('設定値入力', style={'textAlign': 'center'}),
                    html.Div(id=display_id, style={'textAlign': 'center', 'marginBottom': '10px'}), # 現在値表示
                    dcc.Input(id=input_id, type='text', value='', style={'width': '80%', 'margin': '10px auto', 'display': 'block'}),
                    html.Button('設定', id=ok_button_id, n_clicks=0, style={'marginRight': '10px'}),
                    html.Button('キャンセル', id=cancel_button_id, n_clicks=0),
                ], style={
                    'backgroundColor': 'white', 
                    'padding': '20px', 
                    'borderRadius': '5px',
                    'width': '300px',
                    'boxShadow': '0 4px 8px rgba(0,0,0,0.2)',
                })
            ],
            style = MODAL_STYLE
        )
    ])