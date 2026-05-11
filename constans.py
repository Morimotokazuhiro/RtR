from enum import Enum

# 数値表示のフォーマット(列挙型)
class FormatSpecifier(Enum):
    """
    Pythonのf-stringで使用する書式設定文字列をカプセル化する列挙型。
    (Width.Precision Type)
    """
    # value = f-stringの書式文字列
    D = '^d'
    F1_3 = '^5.3f'
    F3_1 = '^5.1f'
    F3_1_SIGNED = '^+6.1f'
    F3_2 = '^6.2f'
    F3_2_SIGNED = '^+7.2f'
    F3_3 = '^7.3f'
    F4_1 = '^6.1f'
    FE_NOTATION = '.2E'

# デバイス定義の列挙型 (アクセスするデバイスをここで指定)
class DeviceEnum(Enum):
    MIX_D4000 = 0       # D4000 (REAL,UINT)
    MIX_D5000 = 1       # D5000 (REAL,INT)
    REAL_D6000 = 2      # D6000 (REAL)
    BITS_M600 = 3       # M600 (BIT)
    BITS_M3400 = 4      # M3400 (BIT)
    BITS_X0 = 5         # X0 (XBIT)
    DUMMY_DINT = 6      # D9100 (DINT) - テスト用ダミー

# --- デバイスデータ構造定義 (ユーザー指定) ---
# NOTE: 構造体内のword_sizeはバイトに変換して計算します。1ワード = 2バイト
DEVICE_DATA_EXTENDED = [
    # D4000 (300ワード = 600バイト)
    {'device': DeviceEnum.MIX_D4000, 'data_type': 'MIX', 'index_size': 190, 'offset': 4000, 'byte_size': 600,
     'structure': [
         {'type': 'REAL', 'count': 30, 'word_size': 2}, # 30点 * 4バイト = 120バイト #D4000
         {'type': 'UINT', 'count': 40, 'word_size': 1}, # 40点 * 2バイト = 80バイト
         {'type': 'REAL', 'count': 50, 'word_size': 2}, # 50点 * 4バイト = 200バイト #D4100
         {'type': 'UINT', 'count': 40, 'word_size': 1}, # 40点 * 2バイト = 80バイト  #D4200
         {'type': 'REAL', 'count': 30, 'word_size': 2}  # 30点 * 4バイト = 120バイト #D4240
     ]},
    # D5000 (70ワード = 140バイト)
    {'device': DeviceEnum.MIX_D5000, 'data_type': 'MIX', 'index_size': 40, 'offset': 5000, 'byte_size': 140,
     'structure': [
         {'type': 'REAL', 'count': 30, 'word_size': 2}, # 30点 * 4バイト = 120バイト
         {'type': 'INT', 'count': 10, 'word_size': 1}   # 10点 * 2バイト = 20バイト
     ]},
    # D6000 (150ワード = 300バイト、1点4バイト)
    {'device': DeviceEnum.REAL_D6000, 'data_type': 'REAL', 'index_size': 75, 'offset': 6000, 'byte_size': 300}, 
    # M600 (30ワード = 60バイト)
    {'device': DeviceEnum.BITS_M600, 'data_type': 'BIT', 'index_size': 480, 'offset': 600, 'byte_size': 60},
    # M3400 (14ワード = 28バイト)
    {'device': DeviceEnum.BITS_M3400, 'data_type': 'BIT', 'index_size': 224, 'offset': 3400, 'byte_size': 28},
    # X0 (6ワード = 12バイト) # 32番目～ (リモートIO) #64～79番目 (フリー) #80～ (M122 流量圧力計)
    {'device': DeviceEnum.BITS_X0, 'data_type': 'BIT', 'index_size': 96, 'offset': 0, 'byte_size': 12},
]

# --- レシピデータ構造定義 ---
RECIPE_REAL_LENGTH = 60 # REAL点の数
RECIPE_INT_LENGTH = 10  # INT点の数

# REALは4バイト/点 (2ワード)
RECIPE_REAL_BYTES = RECIPE_REAL_LENGTH * 4 # 60 * 4 = 240 バイト

# INTは2バイト/点 (1ワード)
RECIPE_INT_BYTES = RECIPE_INT_LENGTH * 2 # 10 * 2 = 20 バイト

# センサー表示用のベースのスタイル
# 48px: ポンプ用
BASE_48px_CIRCLE = {
    'position': 'absolute',
    'width': '48px', 'height': '48px',
    'borderRadius': '50%',
    'backgroundColor': 'lime',  # 仮の初期色
    'border': '1px solid white',
    'zIndex': 15,
}
# 36px: ポンプ用
BASE_36px_CIRCLE = {
    'position': 'absolute',
    'width': '36px', 'height': '36px',
    'borderRadius': '50%',
    'backgroundColor': 'lime',  # 仮の初期色
    'border': '1px solid white',
    'zIndex': 15,
}
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
    'BASE_48px': BASE_48px_CIRCLE,
    'BASE_36px': BASE_36px_CIRCLE,
    'BASE_24px': BASE_24px_CIRCLE,
    'BASE_16px': BASE_16px_CIRCLE,
}