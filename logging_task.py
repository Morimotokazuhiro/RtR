import threading
import time
import datetime
import csv

from typing import Optional
from data_queue import data_queue_handler
from constans import FormatSpecifier, DeviceEnum

# D6000 グループの属するロギングの割り付け
logging_monitor_data = [
    # 既存の項目 (list_index 0-3)
    {'name': 'IG チャンバー内圧(Pa)', 'format': FormatSpecifier.FE_NOTATION, 'list_index': 0,
     'device': 'D6000'},
    {'name': 'CM チャンバー内圧(Pa)', 'format': FormatSpecifier.FE_NOTATION, 'list_index': 1,
     'device': 'D6000'},
    {'name': 'RF 伝送出力(W)', 'format': FormatSpecifier.F4_1, 'list_index': 2,
     'device': 'D6000'},
    {'name': 'RF 反射出力(W)', 'format': FormatSpecifier.F4_1, 'list_index': 3,
     'device': 'D6000'},
    {'name': 'マッチャー C1(%)', 'format': FormatSpecifier.F3_1, 'list_index': 4,
     'device': 'D6000'},
    {'name': 'マッチャー C2(%)', 'format': FormatSpecifier.F3_1, 'list_index': 5,
     'device': 'D6000'},
    {'name': 'マッチャー VDC(V)', 'format': FormatSpecifier.F3_2_SIGNED, 'list_index': 6,
     'device': 'D6000'},
    {'name': '整合器温度センサ(℃)', 'format': FormatSpecifier.F3_1, 'list_index': 7,
     'device': 'D6000'},
    {'name': 'VI1 RF電圧(Vpp)', 'format': FormatSpecifier.F4_1, 'list_index': 8,
     'device': 'D6000'},
    {'name': 'VI1 RF電流(Arms)', 'format': FormatSpecifier.F3_2, 'list_index': 9,
     'device': 'D6000'},
    {'name': 'H1 ヒーター温度(℃)', 'format': FormatSpecifier.F3_1, 'list_index': 10,
     'device': 'D6000'},
    {'name': 'H2 ヒーター温度(℃)', 'format': FormatSpecifier.F3_1, 'list_index': 11,
     'device': 'D6000'},
    {'name': 'ヒーター温度過昇温(℃)', 'format': FormatSpecifier.F3_1, 'list_index': 12,
     'device': 'D6000'},
    {'name': 'EC1 A室角度(°)', 'format': FormatSpecifier.F3_2, 'list_index': 13,
     'device': 'D6000'},
    {'name': 'EC2 B室角度(°)', 'format': FormatSpecifier.F3_2, 'list_index': 14,
     'device': 'D6000'},
    {'name': 'LAMP1 A室厚み(mm)', 'format': FormatSpecifier.F3_2_SIGNED, 'list_index': 15,
     'device': 'D6000'},
    {'name': 'LAMP2 B室厚み(mm)', 'format': FormatSpecifier.F3_2_SIGNED, 'list_index': 16,
     'device': 'D6000'},
    {'name': 'MFCG1 H2 マスフロー(sccm)', 'format': FormatSpecifier.F3_1, 'list_index': 17,
     'device': 'D6000'},
    {'name': 'MFCG2 CH4 マスフロー(sccm)', 'format': FormatSpecifier.F3_1, 'list_index': 18,
     'device': 'D6000'},
    {'name': 'MFCG3 O2 マスフロー(sccm)', 'format': FormatSpecifier.F3_1, 'list_index': 19,
     'device': 'D6000'},
    {'name': 'MFCG4 Ar マスフロー(sccm)', 'format': FormatSpecifier.F3_1, 'list_index': 20,
     'device': 'D6000'},
    {'name': 'MFCG5 N2 マスフロー(sccm)', 'format': FormatSpecifier.F3_1, 'list_index': 21,
     'device': 'D6000'},
    {'name': 'MFCG6 H2 マスフロー(sccm)', 'format': FormatSpecifier.F3_1, 'list_index': 22,
     'device': 'D6000'},
    {'name': 'MFCG7 Ar マスフロー(sccm)', 'format': FormatSpecifier.F3_1, 'list_index': 23,
     'device': 'D6000'},
    {'name': 'GASD1 H2 (ppm)', 'format': FormatSpecifier.F3_1, 'list_index': 24,
     'device': 'D6000'},
    {'name': 'GASD2 CH4 (ppm)', 'format': FormatSpecifier.F3_1, 'list_index': 25,
     'device': 'D6000'},
    {'name': 'GASD3 O2 (%)', 'format': FormatSpecifier.F3_1, 'list_index': 26,
     'device': 'D6000'},
    {'name': 'RP1 N2パージ (L/min)', 'format': FormatSpecifier.F3_2, 'list_index': 27,
     'device': 'D6000'},
    {'name': 'TMP1 N2パージ (L/min)', 'format': FormatSpecifier.F3_2, 'list_index': 28,
     'device': 'D6000'},
    {'name': 'FLM1 RF電源 (L/min)', 'format': FormatSpecifier.F3_1, 'list_index': 29,
     'device': 'D6000'},
    {'name': 'FLM2 自動整合器 (L/min)', 'format': FormatSpecifier.F3_1, 'list_index': 30,
     'device': 'D6000'},
    {'name': 'FLM3 上部電極 (L/min)', 'format': FormatSpecifier.F3_1, 'list_index': 31,
     'device': 'D6000'},
    {'name': 'FLM4 チャンバ1 (L/min)', 'format': FormatSpecifier.F3_1, 'list_index': 32,
     'device': 'D6000'},
    {'name': 'FLM5 チャンバ2 (L/min)', 'format': FormatSpecifier.F3_1, 'list_index': 33,
     'device': 'D6000'},
    {'name': 'FLM6 ヒーターステージ (L/min)', 'format': FormatSpecifier.F3_1, 'list_index': 34,
    'device': 'D6000'},
    {'name': 'PS1 エア元圧 (kPa)', 'format': FormatSpecifier.F3_1, 'list_index': 35,
     'device': 'D6000'},
    {'name': 'PS2 フォアライン圧力 (kPa)', 'format': FormatSpecifier.F3_1, 'list_index': 36,
     'device': 'D6000'},
    {'name': 'PS3 チャンバー内圧 (kPa)', 'format': FormatSpecifier.F3_1, 'list_index': 37,
     'device': 'D6000'},
    {'name': 'PS4 ヒーター内圧 (kPa)', 'format': FormatSpecifier.F3_1, 'list_index': 38,
     'device': 'D6000'},
    {'name': 'PT1 H2ガスレギュレーター (kPa)', 'format': FormatSpecifier.F3_1, 'list_index': 39,
     'device': 'D6000'},
    {'name': 'PT2 CH4ガスレギュレーター (kPa)', 'format': FormatSpecifier.F3_1, 'list_index': 40,
     'device': 'D6000'},
    {'name': 'PT3 O2ガスレギュレーター (kPa)', 'format': FormatSpecifier.F3_1, 'list_index': 41,
     'device': 'D6000'},
    {'name': 'PT4 Arガスレギュレーター (kPa)', 'format': FormatSpecifier.F3_1, 'list_index': 42,
     'device': 'D6000'},
    {'name': 'PT5 N2ガスレギュレーター (kPa)', 'format': FormatSpecifier.F3_1, 'list_index': 43,
     'device': 'D6000'},
    {'name': 'PT6 H2ガスレギュレーター (kPa)', 'format': FormatSpecifier.F3_1, 'list_index': 44,
     'device': 'D6000'},
    {'name': 'PT7 Arガスレギュレーター (kPa)', 'format': FormatSpecifier.F3_1, 'list_index': 45,
     'device': 'D6000'},
    #{'name': 'ヒーター昇降', 'format': FormatSpecifier.F3_2, 'list_index': 46},           # D6092 (100.00 -> F3_2と推定)
    {'name': 'SVM2 開度調整弁 %)', 'format': FormatSpecifier.F3_2, 'list_index': 47,
     'device': 'D6000'},
    {'name': 'SVM3 フォイル搬送速度 (cm/min)', 'format': FormatSpecifier.F3_2, 'list_index': 48,
     'device': 'D6000'},
    {'name': 'SVM3 モーター回転数 (rpm)', 'format': FormatSpecifier.F3_3, 'list_index': 49,
     'device': 'D6000'},
    {'name': 'SVM3 加速度 (sec)', 'format': FormatSpecifier.F3_3, 'list_index': 50,
     'device': 'D6000'},
    {'name': 'SVM3 減速度 (sec)', 'format': FormatSpecifier.F3_3, 'list_index': 51,
     'device': 'D6000'},
    {'name': 'SVM4 フォイル搬送速度 (cm/min)', 'format': FormatSpecifier.F3_2, 'list_index': 52,
     'device': 'D6000'},
    {'name': 'SVM4 モーター回転数 (rpm)', 'format': FormatSpecifier.F3_3, 'list_index': 53,
     'device': 'D6000'},
    {'name': 'SVM4 加速度 (sec)', 'format': FormatSpecifier.F3_3, 'list_index': 54,
     'device': 'D6000'},
    {'name': 'SVM4 減速度 (sec)', 'format': FormatSpecifier.F3_3, 'list_index': 55,
     'device': 'D6000'},
    {'name': 'CH1 冷却水 (℃)', 'format': FormatSpecifier.F3_1, 'list_index': 56,
     'device': 'D6000'},
    {'name': 'SCR1 実行電流 (A)', 'format': FormatSpecifier.F3_2, 'list_index': 57,
     'device': 'D6000'},
    {'name': 'SCR2 実行電流 (A)', 'format': FormatSpecifier.F3_2, 'list_index': 58,
     'device': 'D6000'},
    {'name': 'A室 ロール径', 'format': FormatSpecifier.F3_2, 'list_index': 59,
     'device': 'D6000'},
    {'name': 'B室 ロール径', 'format': FormatSpecifier.F3_2, 'list_index': 60,
     'device': 'D6000'},
    {'name': 'プラズマ点灯積算時間', 'format': 'date', 'list_index': 61},
    {'name': 'プロセスガスバルブポート1開', 'format': 'bit', 'list_index': 220,
     'device': 'M600'},
    {'name': 'プロセスガスバルブポート2開', 'format': 'bit', 'list_index': 221,
     'device': 'M600'},
    {'name': 'プロセスガスバルブポート3開', 'format': 'bit', 'list_index': 222,
     'device': 'M600'},
    {'name': 'プロセスガスバルブポート4開', 'format': 'bit', 'list_index': 223,
     'device': 'M600'},    
    {'name': 'G1G7P0ガス1次側開', 'format': 'bit', 'list_index': 248,
     'device': 'M600'},
    {'name': 'G1P1 プロセスH2一次側開', 'format': 'bit', 'list_index': 251,
     'device': 'M600'},  
    {'name': 'G1P2 プロセスH2二次側開', 'format': 'bit', 'list_index': 227,
     'device': 'M600'},
    {'name': 'G2P1 プロセスCH4一次側開', 'format': 'bit', 'list_index': 252,
     'device': 'M600'},
    {'name': 'G2P2 プロセスCH4二次側開', 'format': 'bit', 'list_index': 238,
     'device': 'M600'},
    {'name': 'G3P1 プロセスO2一次側開', 'format': 'bit', 'list_index': 253,
     'device': 'M600'},
    {'name': 'G3P2 プロセスO2二次側開', 'format': 'bit', 'list_index': 240,
     'device': 'M600'},
    {'name': 'G4P1 プロセスAr一次側開', 'format': 'bit', 'list_index': 255,
     'device': 'M600'},   
    {'name': 'G4P2 プロセスAr二次側開', 'format': 'bit', 'list_index': 244,
     'device': 'M600'},
    {'name': 'G5P1 プロセスN2一次側開', 'format': 'bit', 'list_index': 256,
     'device': 'M600'}, 
    {'name': 'G5P2 プロセスN2二次側開', 'format': 'bit', 'list_index': 246,
     'device': 'M600'},  
    {'name': 'G6P1 シールドH2一次側開', 'format': 'bit', 'list_index': 250,
     'device': 'M600'},   
    {'name': 'G6P2 シールドH2二次側開', 'format': 'bit', 'list_index': 228,
     'device': 'M600'},       
    {'name': 'G7P1 シールドAr一次側開', 'format': 'bit', 'list_index': 254,
     'device': 'M600'},
    {'name': 'G7P2 シールドAr二次側開', 'format': 'bit', 'list_index': 242,
     'device': 'M600'},
    {'name': 'G1P3 プロセスH2 N2パージ開', 'format': 'bit', 'list_index': 237,
     'device': 'M600'},   
    {'name': 'G2P3 プロセスCH4 N2パージ開', 'format': 'bit', 'list_index': 239,
     'device': 'M600'},   
    {'name': 'G3P3 プロセスO2 N2パージ開', 'format': 'bit', 'list_index': 241,
     'device': 'M600'},  
    {'name': 'G4P3 プロセスAr N2パージ開', 'format': 'bit', 'list_index': 245,
     'device': 'M600'},   
    {'name': 'G6P3 シールドH2 N2パージ開', 'format': 'bit', 'list_index': 236,
     'device': 'M600'}, 
    {'name': 'G7P3 シールドAr N2パージ開', 'format': 'bit', 'list_index': 243,
     'device': 'M600'},   
]
# デバッグ用
# logging_monitor_data = [
#     # 既存の項目 (list_index 0-3)
#     {'name': 'IG チャンバー内圧(Pa)', 'format': FormatSpecifier.FE_NOTATION, 'list_index': 0,
#      'device': 'D6000'},
#     {'name': 'CM チャンバー内圧(Pa)', 'format': FormatSpecifier.FE_NOTATION, 'list_index': 1,
#      'device': 'D6000'},
#     {'name': 'A室 オートチューニング入力閾値', 'format': FormatSpecifier.F3_1, 'list_index': 76,
#      'device': 'D4000'},
#     {'name': 'A室 サンプリング周期', 'format': FormatSpecifier.D, 'list_index': 120,
#      'device': 'D4000'},
#     {'name': 'M3018', 'format': 'bit', 'list_index': 18,
#      'device': 'M3400'},
#     {'name': 'M3019', 'format': 'bit', 'list_index': 19,
#      'device': 'M3400'},
#     {'name': 'レシピ R10 (step1)', 'format': FormatSpecifier.F3_1, 'list_index': 0,
#      'device': 'D4000'},
#     {'name': 'レシピ R80 (step2)', 'format': FormatSpecifier.F3_1, 'list_index': 1,
#      'device': 'D4000'},
#     {'name': 'レシピ R150 (step3)', 'format': FormatSpecifier.F3_1, 'list_index': 2,
#      'device': 'D4000'},
#     {'name': 'レシピ R220 (step4)', 'format': FormatSpecifier.F3_1, 'list_index': 3,
#      'device': 'D4000'},
#     {'name': 'レシピ R66 (step1)', 'format': FormatSpecifier.D, 'list_index': 30,
#      'device': 'D4000'},
#     {'name': 'レシピ R136 (step2)', 'format': FormatSpecifier.D, 'list_index': 31,
#      'device': 'D4000'},
#     {'name': 'レシピ R206 (step3)', 'format': FormatSpecifier.D, 'list_index': 32,
#      'device': 'D4000'},
#     {'name': 'レシピ R276 (step4)', 'format': FormatSpecifier.D, 'list_index': 33,
#      'device': 'D4000'},
# ]

class Logging_Task:
    # 設定
    LOG_PATH = 'assets\\log\\log_'    
    LOGGING_ADDRESS = 3601
    RECIPE_STEP_ADDRESS = 4098
    TIMESTAMP_ADDRESS = 4099

    # スレッド関連
    _thread: Optional[threading.Thread] = None
    _is_running = False

    # ファイルI/O関連のインスタンス変数
    _log_file_obj: Optional[object] = None # 開いたファイルオブジェクト
    _csv_writer: Optional[csv.writer] = None # csv.writerオブジェクト

    def __init__(self):
            """インスタンスの初期化。ソケットやスレッドはここでは起動しない。"""
            # タイムスタンプ (ロギングトリガー用) を初期化
            self.timestamp = 0
            # ロギングフラグ (立ち上がりの検知用)
            self.logging_flag = False
            # ファイルI/O関連の変数を初期化
            self._log_file_obj = None
            self._csv_writer = None

            print("Logging_Task: 初期化完了。")

    def start_logging_thread(self):
            """スレッドを立ち上げる"""
            if self._is_running:
                print("Logging_Task: スレッドは既に実行中です。")
                return
                
            self._is_running = True
            # daemon=True でメインプログラム終了時に強制終了される
            self._thread = threading.Thread(target=self._logging_loop, daemon=False)
            self._thread.start()
            print("Logging_Task: スレッドを起動しました。")

    def _logging_loop(self):
        """バックグラウンドスレッドで実行されるロギング監視のメインループ"""
        while self._is_running:
            # PLCのロギングフラグを取得
            plc_logging_flag:bool = data_queue_handler.get_bit_device(self.LOGGING_ADDRESS)
            # ロギング開始
            if (not self.logging_flag) and (plc_logging_flag):
                self._logging_start()

            # ロギングトリガー
            plc_timestamp = data_queue_handler.get_word_device(self.TIMESTAMP_ADDRESS)
            if (self.logging_flag) and (self.timestamp != plc_timestamp):                 
                self._logging_trigger(plc_timestamp)

            # ロギングの終了
            if (self.logging_flag) and (not plc_logging_flag):
                self._logging_stop()

            time.sleep(0.1) # 1秒待機

    def _logging_start(self):
        """ロギング開始時の処理（ファイルを開き、ヘッダーを書き込む）"""
        # Logging_Taskのロギングフラグ ON
        self.logging_flag = True
        # 現在の日時を取得
        now = datetime.datetime.now()

        # 日時を「YYYYMMDD_HHMMSS」形式の文字列にフォーマット
        timestamp_str = now.strftime("%Y%m%d_%H%M%S")

        # ログファイルのファイル名を生成
        log_file_path = self.LOG_PATH + f"{timestamp_str}.csv" # <--- 拡張子を.csvに変更
        print(f"Logging_Task: ロギング開始 -> {log_file_path}")

        try:
            # ファイルを追記モード ('a') で開く
            # newline='' はCSVファイルでは必須 (空行の挿入を防ぐため)
            #self._log_file_obj = open(log_file_path, 'a', newline='', encoding='utf-8')
            self._log_file_obj = open(log_file_path, 'a', newline='', encoding='Shift-JIS') #shift_jis
            self._csv_writer = csv.writer(self._log_file_obj)

            # ヘッダーの作成と書き込み
            header = ['id', '時刻', 'レシピステップ']
            for data in logging_monitor_data:
                header.append(data['name'])
            
            self._csv_writer.writerow(header)
            # ファイルにすぐに書き出す (バッファリングさせない)
            self._log_file_obj.flush() 

        except IOError as e:
            print(f"Logging_Task: ファイルオープンエラー: {e}")
            self.logging_flag = False # 失敗した場合はフラグをオフに戻す
            if self._log_file_obj:
                self._log_file_obj.close()
            self._log_file_obj = None
            self._csv_writer = None


    def _logging_trigger(self, new_timestamp):
        """ロギングデータ取得時の処理（ファイルにデータ行を書き込む）"""
        if not self._csv_writer:
            # ライターがない場合は処理をスキップ
            return

        # タイムスタンプの更新
        self.timestamp = new_timestamp
        
        # D6000のデータ取得と安全チェック
        D6000_list, success = data_queue_handler.safe_plc_data_access(DeviceEnum.REAL_D6000)
        # デバッグ用
        D4000_list, success1 = data_queue_handler.safe_plc_data_access(DeviceEnum.MIX_D4000)
        M3400_list, success2 = data_queue_handler.safe_plc_data_access(DeviceEnum.BITS_M3400)
        M600_list, success3 = data_queue_handler.safe_plc_data_access(DeviceEnum.BITS_M600)

        if success is None:
             # 通信に失敗している場合はスキップ
             return
        if self.timestamp == 0:
             # タイムスタンプ0はスキップ (ロギング終了時に拾った場合)
             return
        
        # ログデータ行の作成
        logdata = []
        # 1. id (タイムスタンプ)
        logdata.append(str(self.timestamp))
        # 2. 時刻
        now = datetime.datetime.now()
        logdata.append(now.strftime("%Y/%m/%d %H:%M:%S.%f")[:-3]) # ミリ秒まで追加
        # 3. レシピステップ
        run_status = data_queue_handler.get_word_device(self.RECIPE_STEP_ADDRESS) 
        logdata.append(str(run_status))
        
        # 4. 監視データ
        for data in logging_monitor_data:
            index = data['list_index']
            dev_type = data.get('device', 'D6000')

            try:
                if data['format'] == 'date':
                    # 時間の場合はfloat型（秒）から変換する
                    value = int(D6000_list[index]) # 秒数
                    time_delta = datetime.timedelta(seconds=value)
                    # オブジェクトを文字列に変換
                    time_str = str(time_delta)                
                    logdata.append(time_str)
                elif dev_type == 'D4000':
                    format_spec = data['format'].value # Enumから値を取り出す
                    logdata.append(f'{D4000_list[index]:{format_spec}}')
                elif dev_type == 'M3400':
                    if M3400_list[index]:
                        logdata.append(f'1')
                    else:
                        logdata.append(f'0')
                elif dev_type == 'M600':
                    if M600_list[index]:
                        logdata.append(f'1')
                    else:
                        logdata.append(f'0')
                else:
                    format_spec = data['format'].value # Enumから値を取り出す
                    logdata.append(f'{D6000_list[index]:{format_spec}}')
            except Exception as e:
                logdata.append(f'N/A')

        # ファイルに書き込む
        try:
            self._csv_writer.writerow(logdata)
            # ファイルにすぐに書き出す
            self._log_file_obj.flush() 
        except Exception as e:
            print(f"Logging_Task: データ書き込みエラー: {e}")
            # エラー発生時はロギングを停止し、ファイルを閉じる
            self._logging_stop()
        
        return
    
    def _logging_stop(self):
        """ロギング終了時の処理（ファイルオブジェクトを閉じる）"""
        # ロギングフラグ OFF
        self.logging_flag = False
        # タイムスタンプのリセット
        self.timestamp = 0
        
        if self._log_file_obj:
            print("Logging_Task: ロギング終了（ファイルをクローズ）")
            self._log_file_obj.close()
            self._log_file_obj = None
            self._csv_writer = None

    def stop_logging_thread(self):
        """スレッドを停止し、終了を待機する"""
        self._logging_stop() # <--- stop時にファイルを閉じる

        if self._is_running:
            self._is_running = False # ループを終了させる
            if self._thread and self._thread.is_alive():
                self._thread.join()
            print("Logging_Task: スレッドを停止しました。")

    # --- 公開メソッド ---
    

    

# --- シングルトンインスタンスの作成 ---   
logging_handler = Logging_Task()