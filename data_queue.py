import queue

from dash import no_update
from typing import Optional, Union
from constans import (
    DeviceEnum,
    DEVICE_DATA_EXTENDED
)
from error_log import error_log_handler

# スレッド間で共有するキューを作成
data_queue = queue.Queue(maxsize=1) # サイズ制限も設定可能



class Data_Queue:

    def __init__(self):
        # 連続エラーの数
        self.error_count = 0
        # 通信データの実体
        self.current_data = []

    # --- プロデューサー（通信スレッド）の処理 ---
    def set_data(self, received_data):
        try:
            data_queue.get_nowait()
        except queue.Empty:
            # キューがすでに空であれば何もしない
            pass

        # 最新のデータを投入する
        data_queue.put(received_data)
        # print(f"データ投入完了 len={data_queue.qsize()}")

    # --- コンシューマー（Dash UI側）の処理 ---
    def updata_data(self):
        # 循環インポートを避けるため、ローカルインポートする
        from tcp_client import tcp_client_handler

        try:
            # print(f"UIでデータ取得開始 len={data_queue.qsize()}")
            # データを取得（または、タイムアウトまで待つ）
            data = data_queue.get(timeout=0.05)
            
            self.current_data = data
            self.error_count = 0
            
        except queue.Empty:
            # timeoutまで待ってもデータがなかった場合
            # UIスレッドはブロックされずに次の処理に進める
            if tcp_client_handler._is_connected:    # 接続時
                if self.error_count < 20:
                    self.error_count = self.error_count + 1

                if self.error_count == 10:
                    # 連続でデータが空だった場合は、一度だけメッセージを残す
                    error_log_handler.print_log("ERROR","Data_Queue: データが連続して空になっています。")
                pass

        return None
    
    # --- 公開メソッド ---
    def get_device_data(self, device_name: DeviceEnum):
        """
        指定されたデバイスの変換済みキャッシュデータを返す。
        Dashコールバックはこのメソッドを呼び出す。
        """
        # 循環インポートを避けるため、ローカルインポートする
        from tcp_client import tcp_client_handler

        current_len = len(self.current_data)
        # 実際にデータ点数が出ているか確認
        if current_len > 0 and device_name.value < current_len:            
            return self.current_data[device_name.value]
        else:
            if tcp_client_handler._is_connected:    # 接続時
                # 接続状態で、取得データの点数が不一致だった場合は、メッセージを残す
                if current_len != 0:
                    error_log_handler.print_log("ERROR",f'Data_Queue: 取得データの点数が不一致です。[{device_name.name}]')

            return None
        
    def safe_plc_data_access(self, device_enum, output_count:int = 1):
        """
        PLCキャッシュからデータを安全に取得するユーティリティ。
        データが未準備の場合は、output_count の数だけ no_update のリストを返す。
        データが準備できている場合は、(データリスト, オフセット, デバイス名) のタプルを返す。
        """
        
        # データを取得するためのデバイス名とオフセットを取得
        device_info = DEVICE_DATA_EXTENDED[device_enum.value]
        device = device_info['device']
        offset = device_info.get('offset', 0) # オフセットがない場合は0を取得
        
        data_list = data_queue_handler.get_device_data(device)
        
        if not data_list:
            # データが準備できていない場合は、必要な出力数分の no_update のリストを返す
            # このリストは、呼び出し元のコールバックがそのまま return すればよい
            return [no_update] * output_count, None
        
        return data_list, offset
        
    def get_bit_device(self, address:int)-> bool:
        """
        指定されたアドレスのビットを返す。
        アドレス固定のハードコードなので良くはないが、手間をかける程でもないのでこのまま
        """
        m600 = 600      # アラーム-アドレス以降のアドレス
        m3400 = 3400    # ランプ-アドレス以降のアドレス
        list_index = -1
        offset = 0
        if m600 <= address < m3400:
            list_index = DeviceEnum.BITS_M600.value
            offset = m600
        elif m3400 <= address:
            list_index = DeviceEnum.BITS_M3400.value
            offset = m3400

        if list_index < 0:
            error_log_handler.print_log("WARNING",f'Data_Queue: アドレスの割り当てが間違っています。アドレス:{address}')
            return False
        elif len(self.current_data) == 0:
            # データ受信前は何もしない
            return False
        else:
            data = self.current_data[list_index]
            data_index = address - offset

            if (data_index < 0) or (data_index >= len(data)):
                error_log_handler.print_log("WARNING",f'Data_Queue: アドレスの割り当てが間違っています。アドレス:{address}')
                return False

            return data[data_index]
        
    def get_word_device(self, address: int) -> Optional[Union[float, int]]:
        """
        指定されたワードアドレス (Dxxxx) に対応するキャッシュデータ (current_data) の値を返す。
        ビットデバイス (M, X) は対象外。

        Args:
            address: 検索するデバイスアドレス (Dxxxx)

        Returns:
            対応する値 (float または int)、または None
        """
        # 循環インポートを避けるため、必要な定義をインポート
        from constans import DEVICE_DATA_EXTENDED, DeviceEnum
        from tcp_client import tcp_client_handler # エラーログ用
        
        # アドレスはワード単位 (2バイト単位) のPLCアドレスを想定
        for device_enum_value, device in enumerate(DEVICE_DATA_EXTENDED):
            
            # ビットデバイスはスキップ
            if device['data_type'] in ('BIT', 'XBIT'):
                continue
                
            start_addr = device['offset']
            # (device['byte_size'] / 2)はワード数。アドレスの範囲をワード単位で確認
            end_addr = start_addr + int(device['byte_size'] / 2) - 1 
            
            if start_addr <= address <= end_addr:
                # 範囲内に見つかった
                
                # 1. デバイスのインデックスを取得 (DeviceEnumのvalueと一致する前提)
                device_index = device_enum_value # device_enum_valueはリストのインデックス 
                
                # 2. キャッシュデータの点数を確認
                current_len = len(self.current_data)
                if current_len == 0 or device_index >= current_len:
                    if (tcp_client_handler._is_connected) and (current_len != 0):
                        error_log_handler.print_log("ERROR", f'Data_Queue: get_word_device: 取得データの点数が不一致です。enam={device_enum_value},len={current_len}')
                    return None
                    
                # 3. デバイスごとのオフセット計算
                current_addr = start_addr
                data_point_index = 0 # current_data[device_index] 内のデータ点のインデックス

                if device['data_type'] == 'REAL':
                    # REALのみの型 (D6000など)
                    # REALは1点あたり2ワード (4バイト)
                    offset_words = address - start_addr
                    # データ点のインデックスはワードオフセットを2で割る
                    # 例: D6000 (0点目), D6002 (1点目), D6004 (2点目)...
                    data_point_index = offset_words // 2
                    
                    data = self.current_data[device_index]
                    if data_point_index < len(data):
                        return data[data_point_index]
                    
                elif device['data_type'] == 'MIX':
                    # REALとUINT/INTの混在型 (D4000, D5000)
                    for item in device['structure']:
                        word_size = item['word_size'] # REAL(2ワード) or INT/UINT(1ワード)
                        count = item['count'] # このアイテムのデータ点数
                        
                        # 終了アドレス (このブロックの最終ワードアドレス)
                        word_count = count * word_size
                        end_word_addr = current_addr + word_count - 1
                        
                        if current_addr <= address <= end_word_addr:
                            # このアイテムの中にアドレスが含まれている
                            offset_in_item = address - current_addr
                            
                            if item['type'] == 'REAL':
                                # REALは1点あたり2ワード (4バイト)
                                index_in_item = offset_in_item // 2
                            elif item['type'] in ('UINT', 'INT'):
                                # UINT/INTは1点あたり1ワード (2バイト)
                                index_in_item = offset_in_item
                            else:
                                # 予期せぬタイプ
                                index_in_item = 0 # 念のため
                                
                            final_index = data_point_index + index_in_item
                            
                            data = self.current_data[device_index]
                            if final_index < len(data):
                                return data[final_index]
                            
                        # 次のブロックへ
                        current_addr = end_word_addr + 1 
                        data_point_index += count # データ点のインデックスも進める (REAL=30, UINT=40, ...)
                        
                # データが見つからなかった場合（アドレスは範囲内だが、構造解析でヒットしなかった）
                break
                
        # デバイスアドレスの範囲外の場合
        error_log_handler.print_log("WARNING", f'Data_Queue: get_word_device: アドレスの割り当てが間違っているか、データが見つかりません。アドレス:{address}')
        return None

# --- シングルトンインスタンスの作成 ---   
data_queue_handler = Data_Queue()