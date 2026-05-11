import threading
import time
import logging
import logging.handlers

from typing import Optional

# @singleton
class ErrorLog:
    # ログ設定
    LOG_FILENAME = 'assets\\log\\error_log.log'

    # スレッド関連
    _thread: Optional[threading.Thread] = None
    _is_running = False

    def __init__(self):
            """インスタンスの初期化。ソケットやスレッドはここでは起動しない。"""
            # 現在の時刻を取得
            self.last_execution_time_seconds = time.time()

            # 1. ファイル書き込みを行うハンドラー (ターゲット)
            # 50MB = 50 * 1024 * 1024 バイト
            MAX_BYTES = 50 * 1024 * 1024 
            BACKUP_COUNT = 2

            file_handler = logging.handlers.RotatingFileHandler(
                ErrorLog.LOG_FILENAME, 
                maxBytes=MAX_BYTES, 
                backupCount=BACKUP_COUNT, 
                encoding='utf-8'
            )
            file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            
            # 2. バッファリングを行うハンドラー
            self.memory_handler = logging.handlers.MemoryHandler(
                capacity=100, 
                flushLevel=logging.CRITICAL + 1, # 特定のフラッシュレベルでは出力させない
                target=file_handler
            )

            # 3. ルートロガーに MemoryHandler を設定
            self.logger = logging.getLogger() # 名前付きロガーインスタンスを取得
            self.logger.setLevel(logging.WARNING) # INFO以上のログを扱う
            self.logger.addHandler(self.memory_handler)
            # 伝播を止める（念のため。ルートより上に流さない設定）
            self.logger.propagate = False
            # 表示させるエラー
            self.error_view:str = None

            print("ErrorLog: 初期化完了。")

    def start_error_log_thread(self):
            """スレッドを立ち上げる"""
            if self._is_running:
                print("ErrorLog: スレッドは既に実行中です。")
                return
                
            self._is_running = True
            # daemon=True でメインプログラム終了時に強制終了される
            self._thread = threading.Thread(target=self._error_log_loop, daemon=False)
            self._thread.start()
            print("ErrorLog: スレッドを起動しました。")

    def _error_log_loop(self):
        """バックグラウンドスレッドで実行されるエラー監視のメインループ"""
        try:
            while self._is_running:
                if self.error_view is not None:
                    # エラーメッセージがあるなら表示する。(1秒に1回まで)
                    print(self.error_view)
                    self.error_view = None

                current_time_seconds = time.time()
                # 前回の実行時間からの経過時間を計算（単純な秒数の差）
                time_difference = current_time_seconds - self.last_execution_time_seconds
                # 経過時間が10秒以上かチェック
                if time_difference >= 10.0:
                    if self.memory_handler.buffer:
                        # バッファにログがある場合のみフラッシュ
                        self.memory_handler.flush()
                        print(f"[{time.strftime('%H:%M:%S')}] エラーメッセージを出力しました.") # 確認用出力
                    # 前回の実行時刻を現在の時刻に更新
                    self.last_execution_time_seconds = current_time_seconds

                else:
                    pass # 何もしない

                time.sleep(1) # 1秒待機
        finally:
            # スレッド終了時に確実にフラッシュ
            if self.memory_handler.buffer:
                 self.memory_handler.flush()
                 print("ErrorLog: スレッド終了時にバッファをフラッシュしました。")

    def stop_error_log_thread(self): # <--- 追加
        """スレッドを停止し、終了を待機する"""
        if self._is_running:
            self._is_running = False # ループを終了させる
            if self._thread and self._thread.is_alive():
                self._thread.join()
            print("ErrorLog: スレッドを停止しました。")

    # --- 公開メソッド ---
    # 使い方：print_log('ERROR', 'メッセージ')
    def print_log(self, error_level: str, message: str):
        """
        指定されたレベルとメッセージでログを出力する。
        例: error_log_handler.print_log('ERROR', 'PLC通信がタイムアウトしました')
        """
        # ロギングレベルを大文字文字列から実際のレベル定数に変換
        # 例えば 'ERROR' -> logging.ERROR
        level = getattr(logging, error_level.upper(), logging.INFO)
        
        # ログを出力
        self.logger.log(level, message)

        # コンソールに表示 (全てのエラーをコンソールに表示しない)
        self.error_view = f'{error_level} {message}'

# --- シングルトンインスタンスの作成 ---   
error_log_handler = ErrorLog()