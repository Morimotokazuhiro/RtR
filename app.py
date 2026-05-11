import dash
from dash import Dash, dcc, html
from dash import Input, Output, State
import time # <- 追加: time.sleepを使用するため
import sys  # <- 追加: プロセス終了のため
import logging # <- 追加: ロガー制御のため
import atexit # <- 追加: プログラム終了時処理用
import dash_mantine_components as dmc

# 各ページのレイアウトをインポート
from auto_page_layout import create_auto_layout
from manual_page_layout import create_manual_layout
from graph_page_layout import create_graph_layout
from setting_page_layout import create_setting_layout
from recipe_page_layout import create_recipe_layout

# 新しいコールバックモジュールをインポート
from auto_callbacks import (
    register_auto_callbacks, get_component_id
)
from manual_callbacks import register_manual_callbacks
from graph_callbacks import register_graph_callbacks
from setting_callbacks import register_setting_callbacks
from recipe_callbacks import register_recipe_callback
from common_modal_callbacks import register_modal_callbacks
# TCP通信用
from tcp_client import tcp_client_handler
# 通信データ管理用
from data_queue import data_queue_handler
# アラーム監視用 (コンストラクタでのファイル読み込み用 ※ 削除しても他所でインポートしているので問題ない)
from alarm_monitoring import alm_handler
# 操作ログ用
from act_log_task import act_log_handler
# エラーログ用
from error_log import error_log_handler
# ロギング用
from logging_task import logging_handler
# レシピ設定ファイル (コンストラクタでのファイル読み込み用)
from recipe_manager import recipe_handler
# レシピ管理用 (コンストラクタでのファイル読み込み用)
from config_manager import config_handler
# 画面管理用
from page_manager import Page_Name, page_handler

# ----------------------------------------------------
# 実行制御フラグ
# False に設定すると、Dash UIを起動せず、通信スレッドのみを動作させます
# ----------------------------------------------------
LAUNCH_DASH_UI = True # True or False

# CSSファイルを明示的に読み込む
external_stylesheets = ['01_page_auto.css', '02_page_manual.css']



# suppress_callback_exceptions=True を追加します
app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

APP_PAGE_MODE_ID = 'page-mode-store'


# メインのレイアウトに URLコンポーネントとコンテンツ表示エリアを追加
# dmc.MantineProvider で全体を囲みます
app.layout = dmc.MantineProvider(
    children=[
        html.Div([
            dcc.Location(id='url', refresh=False),
            dcc.Store(id=APP_PAGE_MODE_ID, data=Page_Name.CURRENT_URL_AUTO.value),
            
            dcc.Store(id='plc-graph-data-store', data=None),
            html.Div(id='page-content'),
            # 3. ダミーコンポーネント (操作ボタンのOutコールバック用)
            html.Div(id='dummy_div'),#, children=[]),#, style={'display': 'none'}),
            html.Footer(className='footer-navigation', children=[
                html.Button('自動', id='btn-auto'),
                html.Button('グラフ', id='btn-graph'),
                html.Button('手動', id='btn-manual'),
                html.Button('設定', id='btn-setting'),
                html.Button('レシピ', id='btn-recipe', className='margin-right-md'),
                html.Button('<', id='btn-prev', className='btn-narrow1'),
                html.Button('>', id='btn-next', className='btn-narrow2'),
            ]),
            # 1秒ごとにコールバックをトリガーするインターバルコンポーネントを追加
            dcc.Interval(
                id='interval-component',
                interval=5*100,
                n_intervals=0,
            )
        ])
    ])

act_log_interval = 0
@app.callback(
    Output('dummy_div', 'children'), # ダミーのOutput
    Input('interval-component', 'n_intervals') # 定期実行するdcc.Interval
)
def update_global_data(n):
    global act_log_interval
    #print(f"queue updata_dataのコールバック開始")
    data_queue_handler.updata_data()
    #print(f"queue updata_dataのコールバック終わり")

    # インターバルトリガーのロギング
    if act_log_interval >= 10:
        act_log_handler.logging_trigger("interval_trigger")
        act_log_interval = 0
    else:
        act_log_interval += 1

    return "" # ダミー

# URLのパスに応じて表示する画面を切り替えるコールバック
# @app.callback(Output('page-content', 'children'),
#               Input('url', 'pathname'))
# def display_page(p_name):
#     print("page" + page_handler.url2)
#     if page_handler.url2 == "":
#         # デフォルトで自動運転画面を表示
#         page_handler.Update_Page('/', 'auto')
#         return create_auto_layout()
#     else:
#         return dash.no_update
    
# ボタンクリックでURLを更新するコールバック
@app.callback(
        Output('url', 'pathname'),
        Output('page-content', 'children'),
        Output('btn-prev', 'style'),
        Output('btn-next', 'style'),
        Input('url', 'pathname'),
        Input('btn-auto', 'n_clicks'),
        Input('btn-graph', 'n_clicks'),
        Input('btn-manual', 'n_clicks'),
        Input('btn-setting', 'n_clicks'),
        Input('btn-recipe', 'n_clicks'),
        Input('btn-prev', 'n_clicks'),
        Input('btn-next', 'n_clicks'),
    )

def navigate_page(p_name, btn_auto_clicks, btn_graph_clicks, btn_manual_clicks, 
                  btn_setting_clicks, btn_recipe_clicks, btn_prev_clicks, btn_next_clicks):
    
    # ボタンのデフォルトスタイル（非表示）
    hide_style = {'visibility': 'hidden'}#{'display': 'none'}
    show_style = {'visibility': 'visible'}#{'display': 'inline-block'} # または 'block'
    
    # 戻り値の初期化（デフォルトは非表示）
    prev_style = hide_style
    next_style = hide_style

    ctx = dash.callback_context
    button_id = get_component_id(ctx)

    # --- 1. 遷移先とコンテンツの決定 ---
    if page_handler.url == Page_Name.CURRENT_URL_INIT:
        page_handler.Update_Page(Page_Name.CURRENT_URL_AUTO)
        content = create_auto_layout()
    
    elif button_id == 'btn-auto':
        page_handler.Update_Page(Page_Name.CURRENT_URL_AUTO)
        content = create_auto_layout()
    elif button_id == 'btn-graph':
        page_handler.Update_Page(Page_Name.CURRENT_URL_GRAPH)
        content = create_graph_layout()
    elif button_id == 'btn-manual':
        page_handler.Update_Page(Page_Name.CURRENT_URL_MANU_1)
        content = create_manual_layout(1)
    elif button_id == 'btn-setting':
        page_handler.Update_Page(Page_Name.CURRENT_URL_SET_1)
        content = create_setting_layout(1)
    elif button_id == 'btn-recipe':
        page_handler.Update_Page(Page_Name.CURRENT_URL_RECI_1)
        content = create_recipe_layout(1)
    
    elif button_id == 'btn-prev':
        if page_handler.url == Page_Name.CURRENT_URL_SET_2:
            page_handler.Update_Page(Page_Name.CURRENT_URL_SET_1)
            content = create_setting_layout(1)
        elif page_handler.url == Page_Name.CURRENT_URL_SET_3:
            page_handler.Update_Page(Page_Name.CURRENT_URL_SET_2)
            content = create_setting_layout(2)
        elif page_handler.url == Page_Name.CURRENT_URL_MANU_2:
            page_handler.Update_Page(Page_Name.CURRENT_URL_MANU_1)
            content = create_manual_layout(1)
        elif page_handler.url == Page_Name.CURRENT_URL_MANU_3:
            page_handler.Update_Page(Page_Name.CURRENT_URL_MANU_2)
            content = create_manual_layout(2)
        elif page_handler.url == Page_Name.CURRENT_URL_MANU_4:
            page_handler.Update_Page(Page_Name.CURRENT_URL_MANU_3)
            content = create_manual_layout(3)
        elif page_handler.url == Page_Name.CURRENT_URL_MANU_5:
            page_handler.Update_Page(Page_Name.CURRENT_URL_MANU_4)
            content = create_manual_layout(4)
        elif page_handler.url == Page_Name.CURRENT_URL_RECI_2:
            page_handler.Update_Page(Page_Name.CURRENT_URL_RECI_1)
            content = create_recipe_layout(1)
        elif page_handler.url == Page_Name.CURRENT_URL_RECI_3:
            page_handler.Update_Page(Page_Name.CURRENT_URL_RECI_2)
            content = create_recipe_layout(2)
        elif page_handler.url == Page_Name.CURRENT_URL_RECI_4:
            page_handler.Update_Page(Page_Name.CURRENT_URL_RECI_3)
            content = create_recipe_layout(3)
        else:
            content = dash.no_update
            
    elif button_id == 'btn-next':
        if page_handler.url == Page_Name.CURRENT_URL_SET_1:
            page_handler.Update_Page(Page_Name.CURRENT_URL_SET_2)
            content = create_setting_layout(2)
        elif page_handler.url == Page_Name.CURRENT_URL_SET_2:
            page_handler.Update_Page(Page_Name.CURRENT_URL_SET_3)
            content = create_setting_layout(3)
        elif page_handler.url == Page_Name.CURRENT_URL_MANU_1:
            page_handler.Update_Page(Page_Name.CURRENT_URL_MANU_2)
            content = create_manual_layout(2)
        elif page_handler.url == Page_Name.CURRENT_URL_MANU_2:
            page_handler.Update_Page(Page_Name.CURRENT_URL_MANU_3)
            content = create_manual_layout(3)
        elif page_handler.url == Page_Name.CURRENT_URL_MANU_3:
            page_handler.Update_Page(Page_Name.CURRENT_URL_MANU_4)
            content = create_manual_layout(4)
        elif page_handler.url == Page_Name.CURRENT_URL_MANU_4:
            page_handler.Update_Page(Page_Name.CURRENT_URL_MANU_5)
            content = create_manual_layout(5)
        elif page_handler.url == Page_Name.CURRENT_URL_RECI_1:
            page_handler.Update_Page(Page_Name.CURRENT_URL_RECI_2)
            content = create_recipe_layout(2)
        elif page_handler.url == Page_Name.CURRENT_URL_RECI_2:
            page_handler.Update_Page(Page_Name.CURRENT_URL_RECI_3)
            content = create_recipe_layout(3)
        elif page_handler.url == Page_Name.CURRENT_URL_RECI_3:
            page_handler.Update_Page(Page_Name.CURRENT_URL_RECI_4)
            content = create_recipe_layout(4)
        else:
            content = dash.no_update
    else:
        # 初期読み込み時など
        content = dash.no_update

    # --- 2. ボタンの表示・非表示判定 (現在のページ情報に基づき決定) ---
    # 設定画面1：Nextのみ表示
    if page_handler.url == Page_Name.CURRENT_URL_SET_1:
        prev_style = hide_style
        next_style = show_style
    # 設定画面2：PrevもNextも表示
    elif page_handler.url == Page_Name.CURRENT_URL_SET_2:
        prev_style = show_style
        next_style = show_style
    # 設定画面3：Prevのみ表示
    elif page_handler.url == Page_Name.CURRENT_URL_SET_3:
        prev_style = show_style
        next_style = hide_style
    # 手動画面1：Nextのみ表示
    elif page_handler.url == Page_Name.CURRENT_URL_MANU_1:
        prev_style = hide_style
        next_style = show_style
    # 手動画面2：PrevもNextも表示
    elif page_handler.url == Page_Name.CURRENT_URL_MANU_2:
        prev_style = show_style
        next_style = show_style
    # 手動画面3：PrevもNextも表示
    elif page_handler.url == Page_Name.CURRENT_URL_MANU_3:
        prev_style = show_style
        next_style = show_style
    # 手動画面4：PrevもNextも表示
    elif page_handler.url == Page_Name.CURRENT_URL_MANU_4:
        prev_style = show_style
        next_style = show_style
    # 手動画面5：Prevのみ表示
    elif page_handler.url == Page_Name.CURRENT_URL_MANU_5:
        prev_style = show_style
        next_style = hide_style
    # レシピ画面1：Nextのみ表示
    elif page_handler.url == Page_Name.CURRENT_URL_RECI_1:
        prev_style = hide_style
        next_style = show_style
    # レシピ画面2：PrevもNextも表示
    elif page_handler.url == Page_Name.CURRENT_URL_RECI_2:
        prev_style = show_style
        next_style = show_style
    # レシピ画面3：PrevもNextも表示
    elif page_handler.url == Page_Name.CURRENT_URL_RECI_3:
        prev_style = show_style
        next_style = show_style
    # レシピ画面4：PrevもNextも表示
    elif page_handler.url == Page_Name.CURRENT_URL_RECI_4:
        prev_style = show_style
        next_style = hide_style
    # それ以外の画面：両方非表示
    else:
        prev_style = hide_style
        next_style = hide_style

    return page_handler.url_str, content, prev_style, next_style

# auto_callbacks.pyからコールバックを登録
register_auto_callbacks(app)
register_manual_callbacks(app)
register_graph_callbacks(app)
register_setting_callbacks(app)
register_recipe_callback(app)
register_modal_callbacks(app)

# デーモンスレッドのフラッシュ処理を atexit に登録
def cleanup_error_log():
    # デーモンスレッド（ErrorLog）の強制終了前にバッファをフラッシュ
    error_log_handler.memory_handler.flush()
    print("\n[atexit] ErrorLogバッファをフラッシュしました。")

if __name__ == '__main__':

    # ---------------------------------------
    # Flaskサーバーのアクセスログを抑制する設定を追加
    # ---------------------------------------
    log = logging.getLogger('werkzeug')
    # ERRORまたはCRITICALに設定すると、POST /_dash-update-component ログは表示されなくなります
    # WARNINGに設定すると、HTTP 4xx/5xx エラーログは表示されます
    log.setLevel(logging.ERROR)
    
    # ---------------------------------------
    # atexitの登録
    # ---------------------------------------
    atexit.register(cleanup_error_log)

    # ---------------------------------------
    # TCPクライアントの起動 (常に実行)
    # ---------------------------------------
    tcp_client_handler.start_communication_thread()

    # ---------------------------------------
    # エラーログの起動 (常に実行)
    # ---------------------------------------
    error_log_handler.start_error_log_thread()

    # ---------------------------------------
    # ロギングの起動 (常に実行)
    # ---------------------------------------
    logging_handler.start_logging_thread()
    
    if LAUNCH_DASH_UI:
        # ---------------------------------------
        # Dashアプリの実行
        # ---------------------------------------
        try:
            print("\nDash UIを起動しています...")
            app.run(debug=False)
        except KeyboardInterrupt:
            # DashサーバーがCtrl+Cで停止した場合
            pass
        finally:
            # アプリ終了時に通信スレッドを停止
            tcp_client_handler.stop_communication_thread()
            error_log_handler.stop_error_log_thread()
            logging_handler.stop_logging_thread()
            act_log_handler.stop_logging()
            
    else:
        # ---------------------------------------
        # UIを起動しない場合の通信テストループ
        # ---------------------------------------
        print("\nUIを起動しません。通信スレッドはバックグラウンドで動作しています。")
        print("Ctrl+Cで通信スレッドとプログラムを終了します...")
        try:
            # 通信スレッドが動作し続けるために、メインスレッドを維持
            while True:
                time.sleep(1) 
        except KeyboardInterrupt:
            print("Ctrl+Cを検出しました。プログラムを終了します。")
        finally:
            tcp_client_handler.stop_communication_thread()
            error_log_handler.stop_error_log_thread()
            logging_handler.stop_logging_thread()
            act_log_handler.stop_logging()
            sys.exit(0) # プロセスを終了
