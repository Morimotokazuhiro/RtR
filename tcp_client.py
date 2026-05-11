import socket
import threading
import time
import struct

from typing import Optional, Dict, Any, List, Union
from data_queue import data_queue_handler
from error_log import error_log_handler
from constans import (
    DEVICE_DATA_EXTENDED,
    RECIPE_REAL_BYTES, # constans.pyから新たにインポート
    RECIPE_INT_BYTES,  # constans.pyから新たにインポート
    RECIPE_REAL_LENGTH, # constans.pyから新たにインポート
    RECIPE_INT_LENGTH,  # constans.pyから新たにインポート
)

# シングルトンパターンを実装するためのデコレータ
def singleton(cls):
    """クラスをシングルトンにするデコレータ"""
    _instances = {}
    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return get_instance

# ----------------------------------------------------
# クライアントソケットをバックグラウンドで管理するクラス
# ----------------------------------------------------

@singleton
class TcpClient:
    """
    C#サーバーとTCP通信を行うシングルトンクライアント。
    通信は専用のバックグラウンドスレッドで行う。
    """
    
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 8080

    SEND_SIZE = 500     # 送信データサイズを500バイトに定義
    RECEIVE_SIZE = 1400 # RDコマンドの受信データ

    INTERVAL = 0.2      # 通信の周期
    
    # 受信データ (サーバーのplc_data 1400バイト)
    # PLCデータとヘッダーを分離した形で格納することを想定
    plc_data: Optional[bytes] = None
    plc_header: Dict = {}

    # レシピデータ (REAL 60点, INT 10点) を格納することを想定
    # 20ステップ分のリストを確保
    RECIPE_STEPS = 20 # 新規追加
    recipe_data_cache: List[Optional[List[Union[float, int]]]] = [None] * RECIPE_STEPS

    # ★★★ 2. 初期値は通常読み取りリクエスト 'RD' + パディング (500バイト) ★★★
    python_data_to_send = b'RD' + b'\x00' * (SEND_SIZE - 2)
    
    # ★★★ 3. 送信用データバッファとロックを追加 ★★★
    # _send_buffer: bytes  <- 変更
    _send_buffer: List[bytes] = [] # 送信待ちリクエストのキュー
    _send_lock = threading.Lock()

    # 通信スレッド関連
    _thread: Optional[threading.Thread] = None
    _is_running = False
    _is_connected = False
    _is_server_stop = False
    
    # ソケット関連
    _socket: Optional[socket.socket] = None    
    _event = threading.Event()  # ボーリングの周期の可変用
    
    def __init__(self):
        """インスタンスの初期化。ソケットやスレッドはここでは起動しない。"""
        self.data_map = DEVICE_DATA_EXTENDED
        
        # ★★★ 4. 初期送信バッファの設定 ★★★
        # self._send_buffer = self.python_data_to_send # 初期リクエストはキューに追加
        self._send_buffer.append(self.python_data_to_send)

        print("TcpClient: 初期化完了。")
    
    def start_communication_thread(self):
        """通信スレッドを立ち上げる"""
        if self._is_running:
            print("TcpClient: スレッドは既に実行中です。")
            return
            
        self._is_running = True
        # daemon=True でメインプログラム終了時に強制終了される
        self._thread = threading.Thread(target=self._communication_loop, daemon=True)
        self._thread.start()
        print("TcpClient: 通信スレッドを起動しました。")

    def stop_communication_thread(self):
        """通信スレッドを停止する"""
        self._is_running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1) # 1秒待機して終了
            self.close_socket()
            error_log_handler.print_log("INFO", "TcpClient: 通信スレッドを停止しました。")
            
    def close_socket(self):
        """ソケットをクローズする"""
        if self._socket:
            try:
                self._socket.shutdown(socket.SHUT_RDWR)
                self._socket.close()
            except OSError as e:
                # 既に閉じている場合のエラーを無視
                if 'not connected' not in str(e):
                    error_log_handler.print_log("ERROR", f"TcpClient: ソケットクローズ時にエラーが発生しました: {e}")
            finally:
                self._socket = None
                self._is_connected = False
                error_log_handler.print_log("INFO", "TcpClient: ソケットをクローズしました。")

    def connect(self):
        """サーバーへの接続を試みる"""
        if self._is_connected:
            return True
        
        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # タイムアウトを設定
            self._socket.settimeout(5) 
            self._socket.connect((self.SERVER_IP, self.SERVER_PORT))
            self._is_connected = True
            self._is_server_stop = False
            print(f"TcpClient: サーバーに接続しました -> {self.SERVER_IP}:{self.SERVER_PORT}")
            return True
        except ConnectionRefusedError:
            if not self._is_server_stop:
                # メッセージは一度だけ出す
                print(f"TcpClient: 接続拒否: サーバー {self.SERVER_IP}:{self.SERVER_PORT} が起動していません。")
                self._is_server_stop = True
            return False
        except socket.timeout:
            error_log_handler.print_log("ERROR", "TcpClient: 接続タイムアウト。")
            return False
        except Exception as e:
            error_log_handler.print_log("ERROR", f"TcpClient: 接続エラーが発生しました: {e}")
            return False

    def _communication_loop(self):
        """バックグラウンドスレッドで実行される通信処理のメインループ"""
        while self._is_running:
            if not self._is_connected:
                # 接続がなければ、接続を試みる
                if not self.connect():
                    time.sleep(3) # 接続失敗時は3秒待機してリトライ
                    continue

            try:
                # ---------------------------------------------
                # 1. サーバーへデータを送信 (C#のpython_dataに格納される)
                # ---------------------------------------------
                # ロックを取得して送信データを読み出し
                data_to_send = None
                with self._send_lock:
                    if self._send_buffer:
                        # リストが空でないなら、キューの先頭からリクエストを取り出す
                        data_to_send = self._send_buffer.pop(0)
                    else:
                        # リストが空の場合は、'RD'コマンドを送信する
                        data_to_send = self.python_data_to_send

                if data_to_send:
                    # サーバーにデータ送信
                    self._socket.sendall(data_to_send)

                    # 'RD' コマンド以外の書き込みリクエストだった場合
                    if data_to_send[:2] != b'RD':
                        command = data_to_send[:2]
                        # デバッグ用
                        print(f'サーバーにコマンド{command}を送信しました')

                # ---------------------------------------------
                # 2. サーバーからの応答 (ヘッダー+plc_data) を受信
                # ---------------------------------------------
                
                # ヘッダー (12バイト) を受信
                header_bytes = self._receive_fixed_length(12)
                if not header_bytes:
                    raise ConnectionResetError("ヘッダー受信時に接続が閉じられました。")
                
                # ヘッダーを解析
                (data_len, plc_status, seq_num) = struct.unpack('<I B I 3x', header_bytes)
                # <I: 4バイト little-endian unsigned int (データ長)
                # B: 1バイト unsigned char (PLCステータス)
                # I: 4バイト little-endian unsigned int (シーケンス番号)
                # 3x: 3バイトパディング (予備)

                self.plc_header = {
                    'data_length': data_len,
                    'plc_status': plc_status,
                    'sequence_number': seq_num
                }
                
                # plc_data (データ長に基づいて受信)
                #print(f"TcpClient: < 受信ヘッダー: データ長={data_len}, ステータス={plc_status}, Seq={seq_num}")
                
                plc_data_bytes = self._receive_fixed_length(data_len)
                if not plc_data_bytes:
                    raise ConnectionResetError("データ受信時に接続が閉じられました。")

                # ---------------------------------------------
                # 3. 共有変数に格納
                # ---------------------------------------------
                # self.plc_data = plc_data_bytes
                #print(f"TcpClient: < {len(self.plc_data)}バイトのPLCデータを受信し、格納しました。")

                # 4. キャッシュを更新
                self._update_cache(plc_data_bytes)

            except ConnectionResetError:
                error_log_handler.print_log("INFO", "TcpClient: サーバーによって接続がリセットされました。再接続を試みます。")
                self.close_socket()
            except socket.timeout:
                error_log_handler.print_log("INFO", "TcpClient: ソケット操作がタイムアウトしました。")
                self.close_socket()
            except OSError as e:
                error_log_handler.print_log("ERROR", f"TcpClient: ソケットエラーが発生しました: {e}。再接続を試みます。")
                self.close_socket()
            except Exception as e:
                # その他の予期せぬエラー
                error_log_handler.print_log("ERROR", f"TcpClient: 致命的なエラー: {e}")
                self.close_socket()
                
            # 通信間隔を調整（サーバーの受信待機ループと連動）
            self._event.clear() # 次の待機のためにイベントをクリア
            self._event.wait(self.INTERVAL)

    def _receive_fixed_length(self, length: int) -> Optional[bytes]:
        """指定されたバイト数を受信するまでループする (TCPストリーム問題対策)"""
        data = b''
        bytes_recd = 0
        while bytes_recd < length:
            chunk = self._socket.recv(length - bytes_recd)
            if not chunk:
                # サーバーが切断
                return None
            data += chunk
            bytes_recd += len(chunk)
        return data
    
    def _parse_mixed_data(self, payload: bytes, structure: List[Dict[str, Any]]) -> List[Any]:
        """MIX型（REALとUINT/INTの混在）の解析"""
        # (既存の実装のまま、省略)
        results = []
        current_offset = 0
        
        for item in structure:
            byte_count = item['count'] * item['word_size'] * 2 # word_size * 2 はワード数からバイトへの変換
            data_slice = payload[current_offset : current_offset + byte_count]
            
            if item['type'] == 'REAL':
                num_points = item['count']
                format_string = f'<{num_points}f'
                results.extend(struct.unpack(format_string, data_slice))
                
            elif item['type'] == 'UINT': # 1ワード = 2バイト (unsigned short)
                num_points = item['count']
                format_string = f'<{num_points}H' 
                results.extend(struct.unpack(format_string, data_slice))
                
            elif item['type'] == 'INT': # 1ワード = 2バイト (signed short)
                num_points = item['count']
                format_string = f'<{num_points}h' 
                results.extend(struct.unpack(format_string, data_slice))
                
            current_offset += byte_count
            
        return results
    
    def _parse_real_data(self, payload: bytes, count: int) -> List[float]:
        """REAL型 (4バイト浮動小数点数) の解析"""
        # REALは4バイトで、1ワード = 2バイトなので、word_size=2 として扱われています。
        # countはREAL値の点数です。
        format_string = f'<{count}f'
        return list(struct.unpack(format_string, payload))

    def _parse_bit_data(self, payload: bytes, count: int) -> List[int]:
        """BIT型 (1ビットデータ) の解析。バイトをビットのリストに展開"""
        # BITデータはワード (2バイト) 単位で送られてきますが、index_sizeはビット数です。
        # M600の場合、30ワード = 60バイトで480ビット (480点) が格納されています。
        
        results = []
        for byte in payload:
            # 1バイト (8ビット) をビット列に展開
            for i in range(8):
                # ビットマスクで i 番目のビットを抽出し、0/1に変換
                bit_value = (byte >> i) & 0x01
                results.append(bit_value)
                # index_size (ビット数) に達したら終了 (安全のため)
                if len(results) >= count:
                    return results
        return results
    
    def _parse_int_data(self, payload: bytes, count: int) -> List[int]:
        """INT型 (2バイト符号付き整数) の解析"""
        format_string = f'<{count}h'
        return list(struct.unpack(format_string, payload))
    
    def _update_cache(self, received_bytes: bytes): # 引数名を変更: payload -> received_bytes
        """
        受信したバイナリデータを解析し、キャッシュを更新
        
        Args:
            received_bytes (bytes): サーバーから受信したPLCデータ本体のバイナリ（ヘッダーを含む）
        """
        # ★★★ 1. ヘッダーの分離 ★★★
        if len(received_bytes) < 2:
            error_log_handler.print_log("ERROR", "TcpClient: 受信データが短すぎます (ヘッダーなし)。")
            return
            
        header = received_bytes[:2]
        payload = received_bytes[2:] # ヘッダー以降の本体データ
        
        if header == b'RD':
            # ★★★ 2. 'RD' コマンドの場合: 通常のPLCデータキャッシュ更新 ★★★
            self._update_plc_cache(payload)
            
        elif header == b'FR':
            # ★★★ 3. 'FR' コマンドの場合: レシピデータキャッシュ更新 ★★★
            self._update_recipe_cache(payload)
            
        elif header != b'OK':
            # 未知のヘッダーを無視またはログ
            error_log_handler.print_log("WARNING", f"TcpClient: 未知の受信ヘッダー: {header}")

    def _update_plc_cache(self, payload: bytes):
        """
        受信したバイナリデータを解析し、キャッシュを更新
        
        Args:
            payload (bytes): サーバーから受信したPLCデータ本体のバイナリ
        """
        new_data = []
        current_offset = 0 # バイナリデータ全体の現在処理中のオフセット
        
        # DEVICE_DATA_EXTENDED の定義順に処理
        for device in self.data_map:
            d_type = device['data_type']
            b_size = device['byte_size'] # デバイスの全データが占めるバイトサイズ
            
            # バイナリデータからこのデバイスに対応するスライスを取得
            data_slice = payload[current_offset : current_offset + b_size]
            
            parsed_data = []

            # --- バイナリ解析ロジック ---
            if d_type == 'MIX':
                # REALとUINT/INTの混在型
                if 'structure' in device:
                    parsed_data = self._parse_mixed_data(data_slice, device['structure'])
            
            elif d_type == 'REAL':
                # REALのみの型 (D6000)
                num_points = device['index_size'] # index_sizeはREALの点数 (60点)
                parsed_data = self._parse_real_data(data_slice, num_points)
            
            elif d_type == 'BIT':
                # BITのみの型 (M600)
                num_points = device['index_size'] # index_sizeはBITの点数 (480点)
                parsed_data = self._parse_bit_data(data_slice, num_points)

            # データを追加
            # デバイス定義の順序と DeviceEnum の value が一致している前提
            new_data.append(parsed_data)
            
            # オフセットを進める
            current_offset += b_size
        
        # データを解析した後、ロック取得前に確認
        #print(f"DEBUG: new_dataの長さ={len(new_data)}, 最初のデバイスのデータ点数={first_data_len}")

        if len(new_data) == len(DEVICE_DATA_EXTENDED):
            data_queue_handler.set_data(new_data)
            #print(f"update_cache: 更新 LEN={len(new_data)}, D4000点数={len(new_data[0])}")

    def _update_recipe_cache(self, payload: bytes):
        """
        レシピデータ (60点REAL + 10点INT) を解析し、指定ステップのキャッシュを更新
        
        Args:
            payload (bytes): サーバーから受信した、[ステップ番号 (2B) + レシピデータ本体 (260B)] のバイナリ
        """
        # レシピデータの期待される合計バイトサイズ: 240B (REAL) + 20B (INT) = 260B
        RECIPE_STEPS = 20 # 20ステップを想定
        RECIPE_HEADER_SIZE = 2 # ステップ番号 (2バイト)
        expected_recipe_body_size = RECIPE_REAL_BYTES + RECIPE_INT_BYTES # 260B
        expected_total_payload_size = expected_recipe_body_size + RECIPE_HEADER_SIZE # 262B

        if len(payload) < expected_total_payload_size:
            error_log_handler.print_log("ERROR", f"TcpClient: レシピデータ ({len(payload)}バイト) が期待される合計サイズ ({expected_total_payload_size}バイト) より短い。")
            return
            
        # 1. ステップ番号の読み取り (最初の2バイト)
        # 2バイト unsigned short (H) をリトルエンディアン (<) でアンパック
        step_bytes = payload[:RECIPE_HEADER_SIZE]
        (step_number,) = struct.unpack('<H', step_bytes) 
        
        # ステップ番号の検証
        if not (0 <= step_number < RECIPE_STEPS):
            error_log_handler.print_log("ERROR", f"TcpClient: 受信したステップ番号 ({step_number}) が無効範囲 (0〜{RECIPE_STEPS-1}) です。")
            return

        # 2. レシピデータ本体の抽出 (ステップ番号以降の260バイト)
        recipe_body = payload[RECIPE_HEADER_SIZE:]
        current_offset = 0
        all_recipe_data: List[Union[float, int]] = []

        # 3. REALデータ (60点, 240バイト) の解析
        real_slice = recipe_body[current_offset : current_offset + RECIPE_REAL_BYTES]
        real_data = self._parse_real_data(real_slice, RECIPE_REAL_LENGTH)
        all_recipe_data.extend(real_data)
        current_offset += RECIPE_REAL_BYTES

        # 4. INTデータ (10点, 20バイト) の解析
        int_slice = recipe_body[current_offset : current_offset + RECIPE_INT_BYTES]
        int_data = self._parse_int_data(int_slice, RECIPE_INT_LENGTH)
        all_recipe_data.extend(int_data)
        # current_offset += RECIPE_INT_BYTES # これ以降は不要だが、処理を完了させる

        # 5. キャッシュの更新
        if len(all_recipe_data) == (RECIPE_REAL_LENGTH + RECIPE_INT_LENGTH):
            # 20ステップのリストのうち、該当するステップ位置に格納
            self.recipe_data_cache[step_number] = all_recipe_data
            # print(f"TcpClient: レシピデータ (ステップ {step_number}, {len(all_recipe_data)}点) を更新しました。")
        else:
            error_log_handler.print_log("ERROR", f"TcpClient: レシピデータの解析結果 ({len(all_recipe_data)}点) が不整合。ステップ: {step_number}")

        from recipe_manager import recipe_handler
        # 6. 最終ステップの場合、照合要求の通知
        if step_number == RECIPE_STEPS - 1:
            recipe_handler.check_recipe_data()

    def _find_device_type_and_size(self, address: int) -> Optional[Dict[str, Any]]:
        """
        アドレスに基づいてデバイスタイプとstructのフォーマットを検索するヘルパー関数。
        
        Args:
            address: 検索するデバイスアドレス (Dxxxx)
        
        Returns:
            {'type': 'REAL'/'INT'/'UINT', 'byte_size': 2/4, 'struct_format': '<f'/'<h'/'<H'} の辞書、または None
        """
        from constans import DEVICE_DATA_EXTENDED # constans.pyから構造定義をインポート
        
        # アドレスはワード単位 (2バイト単位) のPLCアドレスを想定
        for device in DEVICE_DATA_EXTENDED:
            start_addr = device['offset']
            # (device['byte_size'] / 2)はワード数。アドレスの範囲をワード単位で確認
            end_addr = start_addr + int(device['byte_size'] / 2) - 1 
            
            if start_addr <= address <= end_addr:
                # 範囲内に見つかった
                if device['data_type'] == 'REAL':
                    # D6000などREAL型のみのブロック
                    # headerキーを追加し、4バイト書き込みであることを明示
                    return {'type': 'REAL', 'header': 'WD', 'byte_size': 4, 'struct_format': '<f'} 
                    
                elif device['data_type'] == 'MIX':
                    current_addr = start_addr
                    for item in device['structure']:
                        word_size = item['word_size'] # REAL(2ワード) or INT/UINT(1ワード)
                        count = item['count']
                        
                        # 終了アドレス (このブロックの最終ワードアドレス)
                        word_count = count * word_size # ブロック内のワード数
                        end_word_addr = current_addr + word_count - 1
                        
                        if current_addr <= address <= end_word_addr:
                            # このアイテムの中にアドレスが含まれている
                            if item['type'] == 'REAL':
                                # REALは4バイト (float) をリトルエンディアン '<f' でパック
                                # PLCとの通信時に"WD..."(8バイト)に変換されます。
                                return {'type': 'REAL', 'header': 'WD', 'byte_size': 4, 'struct_format': '<f'}
                            elif item['type'] == 'UINT':
                                # UINTは2バイト (unsigned short) をリトルエンディアン '<H' でパック
                                # PLCとの通信時に"WI..."(6バイト)に変換されます。
                                return {'type': 'UINT', 'header': 'WI', 'byte_size': 2, 'struct_format': '<H'} 
                            elif item['type'] == 'INT':
                                # INTは2バイト (signed short) をリトルエンディアン '<h' でパック
                                # PLCとの通信時に"WI..."(6バイト)に変換されます。
                                return {'type': 'INT', 'header': 'WI', 'byte_size': 2, 'struct_format': '<h'}
                        
                        # 次のブロックへ
                        # 【修正点】ブロックの最終アドレスの「次」から開始するように修正 (word_sizeの加算は不要)
                        current_addr = end_word_addr + 1 # 次のブロックの開始ワードアドレス
                        
                break
                
        return None

    # --- 公開メソッド ---
            
    def write_device_bit(self, device_data: Dict[str, Any]):
        """
        特定のビットアドレスに書き込みリクエストを準備し、送信バッファにセットする。
        
        Args:
            device_data: manual_operation2_layout.pyのbutton_dataから渡される辞書。
                         'sw_address' (書き込みアドレス) を含む。
        """
        # 'manual_operation2_layout.py'のbutton_dataから 'sw_address' を取得
        sw_address = device_data['sw_address']
        if sw_address == 0:
            print(f'アドレス{sw_address}の操作は無効です')
            return
        
        value = 1 # 指定のアドレスのM番地のビットをオンにするため、値は「1」

        # ★★★ 構造: WB (2B) + sw_address (2B) + value (2B) + パディング ★★★
        
        # sw_addressとvalueをLittle-Endian (H: unsigned short) でパック (4バイト)
        # Hは2バイト (1ワード) に対応します
        command_bytes = struct.pack('<H H', sw_address, value)
        
        header_bytes = b'WB' # ヘッダー 'WB' (2バイト)
        
        send_data = header_bytes + command_bytes # 合計6バイト

        # SEND_SIZE (500バイト) にパディング
        padding_size = self.SEND_SIZE - len(send_data)
        if padding_size > 0:
            send_data += b'\x00' * padding_size
            
        # ロックを使用して安全に送信バッファを更新
        with self._send_lock:
            self._send_buffer.append(send_data)

        # イベントをセットして通信ループを即座に再開させる
        self._event.set()
            
        #print(f"TcpClient: 送信バッファを書き込みリクエスト 'WB' (Addr: {sw_address}, Val: {value}) に更新しました。")
        return
    
    def write_device_word(self, address: int, value: Union[float, int]):
        """
        ワードアドレスに書き込みリクエストを準備し、送信バッファにセットする。
        ヘッダーは 'WD' (2B)、アドレス (2B)、値 (2Bまたは4B) で構成する。
        
        Args:
            address: 書き込みアドレス (Dxxxx)
            value: 書き込む値 (float または int)
        """
        # 1. データタイプの特定とバイナリ変換の準備
        device_info = self._find_device_type_and_size(address)
        
        if not device_info:
            print(f"TcpClient: 警告: アドレス {address} のデータタイプを特定できませんでした。書き込みをスキップします。")
            return
        
        self.write_device_main(address, value, device_info)

    # def write_Rdevice_word(self, address: int, value: Union[float, int]):
    #     """
    #     レシピ用ファイルレジスタの書き込み
    #     """
    #     RECIPE_LENGTH = 100
    #     REAL_LENGTH = 60
    #     address_index = address % RECIPE_LENGTH

    #     if address_index < REAL_LENGTH:
    #         # REALは4バイト (float) をリトルエンディアン '<f'
    #         device_info = {'type': 'REAL', 'header': 'FD', 'byte_size': 4, 'struct_format': '<f'}
    #     else:
    #         # INTは2バイト (signed short) をリトルエンディアン '<h' でパック
    #         device_info = {'type': 'INT', 'header': 'FI', 'byte_size': 2, 'struct_format': '<h'}
        
    #     self.write_device_main(address, value, device_info)
        
    def write_device_main(self, address: int, value: Union[float, int], device_info):
        data_type = device_info['type']
        header:str = device_info['header']
        struct_format = device_info['struct_format']
        byte_size = device_info['byte_size']
        
        # 2. ヘッダーとアドレスのバイナリ化
        # 構造: WD (2B) + address (2B) + value (2B or 4B) + パディング
        header_bytes = header.encode('utf-8') # ヘッダー 'NN' (2バイト)

        # アドレスをLittle-Endian (H: unsigned short) でパック (2バイト)
        address_bytes = struct.pack('<H', address)
        
        # 3. 値のバイナリ化
        try:
            if data_type == 'REAL':
                value_bytes = struct.pack(struct_format, value)
            else:
                value_bytes = struct.pack(struct_format, int(value))
        except struct.error as e:
            error_log_handler.print_log("ERROR", f"TcpClient: エラー: 値 {value} をフォーマット '{struct_format}' ({data_type}, {byte_size}B) でパックできません: {e}")
            return
            
        # 4. 送信データの結合とパディング
        send_data = header_bytes + address_bytes + value_bytes 

        # SEND_SIZE (500バイト) にパディング
        padding_size = self.SEND_SIZE - len(send_data)
        if padding_size < 0:
            error_log_handler.print_log("ERROR", f"TcpClient: エラー: 送信データサイズ ({len(send_data)}バイト) が最大サイズ ({self.SEND_SIZE}バイト) を超えています。")
            return
            
        send_data += b'\x00' * padding_size
            
        # 5. ロックを使用して安全に送信バッファを更新
        with self._send_lock:
            self._send_buffer.append(send_data)

                # イベントをセットして通信ループを即座に再開させる
        self._event.set()
            
        #print(f"TcpClient: 送信バッファを書き込みリクエスト 'WD' (Addr: {address}, Val: {value} as {data_type}, Size: {byte_size}B) に更新しました。")
        return
    
    def write_Rdevice_word_bulk(self, addresses: List[int], values: List[Union[float, int]], step_num: int):
        """
        レシピ用ファイルレジスタの一括書き込みリクエストを準備し、送信バッファにセットする。

        Args:
            addresses: 書き込みアドレスのリスト (70デバイス分を想定)
            values: 書き込む値のリスト (70デバイス分を想定)
        """
        RECIPE_LENGTH = 100
        REAL_LENGTH = 60
        # DEVICE_LENGTH [REAL型]28点／[INT型]9点、デバイスアドレス：R0～R55／R60～R69
        DEVICE_LENGTH = 32
        
        if len(addresses) != DEVICE_LENGTH or len(values) != DEVICE_LENGTH:
            error_log_handler.print_log("ERROR", f"TcpClient: エラー: 一括書き込みには {DEVICE_LENGTH} 点のアドレスと値が必要です。 (現在: {len(addresses)}/{len(values)})")
            return

        # 構造: ヘッダー (2B) + アドレス1 (2B) + 値1 (2B/4B) + アドレス2 + 値2 + ... + パディング
        # ヘッダーは 'WD' や 'FD' ではなく、一括書き込み用の新しいヘッダー 'FB' (File Bulk) を想定
        header_bytes = b'FB' 
        send_data = header_bytes

        # 1. 先頭のアドレスのバイナリ化:2バイト
        address_bytes = struct.pack('<H', addresses[0])
        # 結合
        send_data += address_bytes
        
        # 2. 70デバイス分のデータをバイナリ化
        dev_index:int = 0
        adr_index:int = 0
        while dev_index < RECIPE_LENGTH:

            # 実際のアドレス範囲の判定ロジック
            if 0 <= adr_index < len(addresses):
                address_index = addresses[adr_index] % RECIPE_LENGTH
                value = values[adr_index]
            else:
                # すべてのデバイスの走査が終われば、空バイトで埋める
                address_index = -1
                value = -1
            
            print(f"address_index {address_index} / dev_index {dev_index} / adr_index {adr_index}")
            # 値のバイナリ化
            try:
                if address_index == dev_index:
                    if dev_index < REAL_LENGTH:
                        value_bytes = struct.pack('<f', value)
                        dev_index += 2                    
                    else:
                        value_bytes = struct.pack('<h', int(value))
                        dev_index += 1

                    adr_index += 1
                else:
                    if dev_index < REAL_LENGTH:
                        value_bytes = struct.pack('<f', 0)
                        dev_index += 2
                    elif dev_index == 99:
                        # 3. ステップ番号の付与
                        value_bytes = struct.pack('<h', int(step_num))
                        dev_index += 1
                    else:
                        value_bytes = struct.pack('<h', 0)
                        dev_index += 1

            except struct.error as e:
                error_log_handler.print_log("ERROR", f"TcpClient: エラー: 値 {value} をパックできません: {e}。この書き込みをスキップします。")
                continue # この値だけスキップし、次のデバイスに進む
                
            # 結合
            send_data += value_bytes


        # 4. パディング
        padding_size = self.SEND_SIZE - len(send_data)
        if padding_size < 0:
            error_log_handler.print_log("ERROR", f"TcpClient: エラー: 送信データサイズ ({len(send_data)}バイト) が最大サイズ ({self.SEND_SIZE}バイト) を超えています。")
            return
            
        send_data += b'\x00' * padding_size
            
        # 3. ロックを使用して安全に送信バッファを更新
        with self._send_lock:
            self._send_buffer.append(send_data)

        # イベントをセットして通信ループを即座に再開させる
        self._event.set()
            
        print(f"TcpClient: 送信バッファをレシピ一括書き込みリクエスト 'FB' ({len(addresses)}デバイス) に更新しました。")
        return
    
    # def read_recipe_data(self):
    #     # レシピデータ受信のコマンド
    #     header_bytes = b'FR' 
    #     send_data = header_bytes

    #     # 2. パディング
    #     padding_size = self.SEND_SIZE - len(send_data)
    #     if padding_size < 0:
    #         error_log_handler.print_log("ERROR", f"TcpClient: エラー: 送信データサイズ ({len(send_data)}バイト) が最大サイズ ({self.SEND_SIZE}バイト) を超えています。")
    #         return
            
    #     send_data += b'\x00' * padding_size
            
    #     # 3. ロックを使用して安全に送信バッファを更新
    #     with self._send_lock:
    #         self._send_buffer.append(send_data)

    #     # イベントをセットして通信ループを即座に再開させる
    #     self._event.set()
            
    #     print(f"TcpClient: 送信バッファをレシピ読み込みリクエスト 'FR' に更新しました。")
    #     return


# --- シングルトンインスタンスの作成 ---   
tcp_client_handler = TcpClient()
