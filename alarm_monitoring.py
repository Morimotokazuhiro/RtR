import csv
from datetime import datetime
from error_log import error_log_handler

from manual_alarm_layout import ALM_NUM_ROWS, ALARM_COLUMN_IDS
# C#通信用
from constans import DeviceEnum
from data_queue import data_queue_handler

class AlarmMonitoring:
    # 定義を宣言
    CSV_FILE = 'assets\\setting\\alarm_list_dect.csv'
    REQUIRED_HEADERS = ['address', 'level', 'type', 'message']
    ENCODING = 'utf-8'
    ALARM_LENGTH = 40

    def __init__(self):
        """インスタンスの初期化"""
        self.alarm_list_dect = {}
        # TODO:タイムスタンプ機能は将来実装予定
        self.timestamp = -1

        # 前回のM600_listの状態を保持 (立ち上がり検知用)
        # 初期状態は「全てアラームOFF」として扱う (pythonはbit/intの区別はあまりないので0or1でOK)
        self._prev_m600_list = [0] * (5+self.ALARM_LENGTH) # M600からM644までのビット数 (45ビット)
        
        # 各アラームアドレスの発生時刻を保持
        # 例: {'M605': '12:00:00', 'M606': '12:00:01', ...}
        self._alarm_timestamps = {}

        # ファイルの読み込み
        self.Load_AlarmList()

    # --- 公開メソッド ---

    # ソフト起動時にアラームリストを読み込みます
    def Load_AlarmList(self):
        try:
            with open(self.CSV_FILE, 'r', encoding=self.ENCODING, newline='') as csvfile:
                # 1. 最初の行にコメント行がある場合は、next()で読み飛ばす (ファイルポインタの更新)
                # 使用例：
                # comment_line = next(CSV_FILE)
                # print(f"スキップされた行: {comment_line.strip()}")
                
                # 2. 次の行（2行目）がヘッダーとして認識される
                reader = csv.DictReader(csvfile)
                
                actual_headers = reader.fieldnames
                
                # 3. ヘッダーの存在を確認
                if set(self.REQUIRED_HEADERS).issubset(set(actual_headers)):
                    # ヘッダーの確認OK
                    self.alarm_list_dect = [row for row in reader]

                    if len(self.alarm_list_dect) != self.ALARM_LENGTH:
                        #error_log_handler.print_log("WARNING", f"AlarmMonitoring: アラームリストの長さが異なります。確認して下さい。")
                        self.ALARM_LENGTH = len(self.alarm_list_dect)
                        self._prev_m600_list = [0] * (5+self.ALARM_LENGTH) # アラーム監視リストの拡張
                else:
                    error_log_handler.print_log("ERROR", f"AlarmMonitoring: 必須ヘッダーが不足しています。")                    

        except Exception as e:
            error_log_handler.print_log("ERROR", f"AlarmMonitoring: エラーが発生しました: {e}")

    # Dash (UI側) から定期的に呼ばれる。(スレッドを立てる程ではないので、dcc.intervalで呼んでください)
    def Check_Alarm(self):        
        # PLCから送られてきたタイムスタンプ
        # 値-1は初期値なので、PLCの受信データのタイムスタンプは「0～50000」までで設定してください (65535はダメ)
        new_timestamp = -1
        # PLCのデータを元に作成するリスト
        alarm_list = []
        # 空の場合のリスト
        empty_row_dict = {col_id: '' for col_id in ALARM_COLUMN_IDS}

        # データ取得
        # safe_plc_data_accessの第2引数は、取得失敗時のコールバック用のno_updateの長さなので、ここでは"1"でも問題はない
        M600_list, offset_m = data_queue_handler.safe_plc_data_access(
            DeviceEnum.BITS_M600, 1
        )
        D6000_list, offset_d = data_queue_handler.safe_plc_data_access(
            DeviceEnum.REAL_D6000, 1
        )
        
        # データが未準備の場合（deviceがNoneの場合）は 空のリストを返す(タイムスタンプは-1なので、アラームリストは更新しない)
        if (offset_m is None) or (offset_d is None):
            return [empty_row_dict] * ALM_NUM_ROWS
        
        # PLCから送られてきたタイムスタンプ (仮)
        # new_timestamp = D6000_list[0]
        # if self.timestamp != new_timestamp:
        #     print("AlarmMonitoring: 異常が発生しました")
        # self.timestamp = new_timestamp

        # アラームが出ているか？ "M600"(インデックス0)はアラーム発生のビットです
        # "M601"(インデックス1)はアラーム表示用のビットです。26年1月30日に表示のみの場合も出来るように拡張しました。
        alarm = M600_list[1]

        # 🚨 アラームビットの立ち上がりを検知し、発生時刻を記録
        # PLCのデータはM605から始まるため、alarm_list_dectのインデックスと合わせる
        offset = 600
        if self.alarm_list_dect:
            for i, data in enumerate(self.alarm_list_dect):
                M_address = self.alarm_list_dect[i]['address']
                address = int(M_address.lstrip('M'))
                current_state = M600_list[address - offset]
                prev_state = self._prev_m600_list[address - offset]
                # 立ち上がり検知 (OFF -> ON)
                if current_state == 1 and prev_state == 0:
                    # 発生時刻を記録 (時:分:秒のフォーマット)
                    self._alarm_timestamps[M_address] = datetime.now().strftime('%H:%M:%S')
                    
                # 立ち下がり検知 (ON -> OFF)
                elif current_state == 0 and prev_state == 1:
                    # アラームが解除されたら時刻をクリア
                    if M_address in self._alarm_timestamps:
                        del self._alarm_timestamps[M_address]

        # 🚨 今回のM600_listの状態を次回のために保存
        self._prev_m600_list = M600_list[:]

        if alarm:
            for i, data in enumerate(self.alarm_list_dect):
                alarm_info = self.alarm_list_dect[i]
                M_address = alarm_info['address']
                address = int(M_address.lstrip('M'))
                current_state = M600_list[address - offset]
                
                if current_state == 1:                    
                    # 発生時刻を取得。存在しない場合は空文字列 (異常時を想定し、原則存在するはず)
                    timestamp = self._alarm_timestamps.get(M_address, '')
                    
                    # UI表示用の辞書を作成
                    alarm_row = {
                        ALARM_COLUMN_IDS[0]: timestamp,                      # 時刻
                        ALARM_COLUMN_IDS[1]: alarm_info['level'],            # レベル
                        ALARM_COLUMN_IDS[2]: alarm_info['type'],             # 種別
                        ALARM_COLUMN_IDS[3]: alarm_info['message'],          # メッセージ
                    }
                    alarm_list.append(alarm_row)

            if ALM_NUM_ROWS >= len(alarm_list):
                return alarm_list + [empty_row_dict] * (ALM_NUM_ROWS - len(alarm_list))
            else:
                return alarm_list
        else:
            return [empty_row_dict] * ALM_NUM_ROWS
    
# --- シングルトンインスタンスの作成 ---   
alm_handler = AlarmMonitoring()