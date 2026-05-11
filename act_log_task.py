import logging
from logging.handlers import RotatingFileHandler
import os

class Act_Logging_Task:
    LOG_DIR = 'assets\\log'
    LOG_BASE_NAME = 'act_log.log'

    def __init__(self):
        # ログディレクトリがない場合は作成
        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)

        self.act_logger = logging.getLogger("act_log")
        self.act_logger.setLevel(logging.INFO)
        self.act_logger.propagate = False
        
        # 二重登録防止
        if not self.act_logger.handlers:
            log_path = os.path.join(self.LOG_DIR, self.LOG_BASE_NAME)
            
            # RotatingFileHandlerの設定: 1MBごとにローテーション、最大5ファイル保持
            # encoding='utf-8-sig' でExcel対応を維持
            handler = RotatingFileHandler(
                log_path, 
                maxBytes=1 * 1024 * 1024, # 1MB
                backupCount=5, 
                encoding='utf-8-sig'
            )
            
            # CSV形式に合わせてフォーマットを設定（時刻, メッセージ）
            formatter = logging.Formatter('%(asctime)s.%(msecs)03d,%(message)s', 
                                          datefmt='%Y/%m/%d %H:%M:%S')
            handler.setFormatter(formatter)
            self.act_logger.addHandler(handler)

    def logging_trigger(self, message_str):
        """ロギング実行"""
        # loggingモジュールが内部でロックを持つため、自前のlockは不要
        self.act_logger.info(message_str)

    def stop_logging(self):
        """終了処理（ハンドラのクローズ）"""
        for handler in self.act_logger.handlers:
            handler.close()
            self.act_logger.removeHandler(handler)

# シングルトンインスタンス
act_log_handler = Act_Logging_Task()