from dash import html, dcc
from enum import Enum
from constans import FormatSpecifier

from common_modal_layout import create_setting_modal

# --------------------------------------------------------
# テキストとアドレスのリスト
# --------------------------------------------------------
# 改行文字コード（自由に変更可）
NEWLINE = '<br>'
text_data = [
    # 左の列
    {'left': '36px', 'top': '100px', 'text': 'AV1'+NEWLINE+'高真空計測'},
    {'left': '36px', 'top': '100px', 'text': 'AV2'+NEWLINE+'隔膜式圧力計'},
    {'left': '36px', 'top': '100px', 'text': 'AV3'+NEWLINE+'P_GAS1バルブ'},
    {'left': '36px', 'top': '100px', 'text': 'AV4'+NEWLINE+'P_GAS3バルブ'},
    {'left': '36px', 'top': '100px', 'text': 'AV5'+NEWLINE+'P_GAS2バルブ'},
    {'left': '36px', 'top': '100px', 'text': 'AV6'+NEWLINE+'P_GAS4バルブ'},
    {'left': '36px', 'top': '100px', 'text': 'AV7'+NEWLINE+'N2パージバルブ'},
    {'left': '36px', 'top': '100px', 'text': 'AV8'+NEWLINE+'電極シールドガス'},
    {'left': '36px', 'top': '100px', 'text': 'AV01'+NEWLINE+'粗引ラインスロー'},
    {'left': '36px', 'top': '100px', 'text': 'AV01'+NEWLINE+'粗引ライン全開'},
    # 真ん中の列
    {'left': '496px', 'top': '100px', 'text': 'AV02'+NEWLINE+'TMPフォア'},
    {'left': '496px', 'top': '100px', 'text': 'AV09'+NEWLINE+'TMP1 N2パージ'},
    {'left': '496px', 'top': '100px', 'text': 'AV10'+NEWLINE+'RP1 N2パージ'},
    {'left': '496px', 'top': '100px', 'text': 'AV11'+NEWLINE+'ヒーター 真空引き'},
    {'left': '496px', 'top': '100px', 'text': 'AV12'+NEWLINE+'ヒーター N2パージ'},
    {'left': '496px', 'top': '100px', 'text': 'RP1'+NEWLINE+'ポンプ起動'},
    {'left': '496px', 'top': '100px', 'text': 'TMP1'+NEWLINE+'ターボポンプ起動'},
    #{'left': '496px', 'top': '100px', 'text': '自動'+NEWLINE+'真空引き粗びき'},
    #{'left': '496px', 'top': '100px', 'text': '自動'+NEWLINE+'高真空真空引き'},
    #{'left': '496px', 'top': '100px', 'text': '自動 チャンバー'+NEWLINE+'N2パージ'},
]
text_data2 = [
    # 右の列
    {'left': '956px', 'top': '8px', 'text': 'SVM2 FULL'+NEWLINE+'OPEN/CLOSE'},
    {'left': '956px', 'top': '80px', 'text': '開度調整'},
    {'left': '956px', 'top': '152px', 'text': '開度設定値'+NEWLINE+'(%)'},
    {'left': '956px', 'top': '224px', 'text': '圧力制御'},
    {'left': '956px', 'top': '368px', 'text': '圧力制御'+NEWLINE+'設定値(Pa)'},
    #{'left': '956px', 'top': '440px', 'text': 'SVM1'+NEWLINE+'サーボオン'},
    {'left': '956px', 'top': '512px', 'text': 'ロギング'},
    {'left': '956px', 'top': '584px', 'text': 'プラズマ点灯'+NEWLINE+'積算時間'},
]
# --------------------------------------------------------
# ボタンのリスト
# コールバックで'src'を変更し、押下時のアドレス参照にも使います
# --------------------------------------------------------
button_data = [
    # 左の列 ONスイッチ
    {'id': 'op1_AV1_1', 'img_id': 'op1_AV1_img1', 'left': '204px','top': '100px', 'sw_address': 3018, 'address': 818, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV2_1', 'img_id': 'op1_AV2_img1','left': '204px','top': '100px', 'sw_address': 3019, 'address': 819, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV3_1', 'img_id': 'op1_AV3_img1','left': '204px','top': '100px', 'sw_address': 3020, 'address': 820, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV4_1', 'img_id': 'op1_AV4_img1','left': '204px','top': '100px', 'sw_address': 3022, 'address': 822, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV5_1', 'img_id': 'op1_AV5_img1','left': '204px','top': '100px', 'sw_address': 3021, 'address': 821, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV6_1', 'img_id': 'op1_AV6_img1','left': '204px','top': '100px', 'sw_address': 3023, 'address': 823, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV7_1', 'img_id': 'op1_AV7_img1','left': '204px','top': '100px', 'sw_address': 3017, 'address': 817, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV8_1', 'img_id': 'op1_AV8_img1','left': '204px','top': '100px', 'sw_address': 3029, 'address': 829, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV01_1', 'img_id': 'op1_AV01_img1','left': '204px','top': '100px', 'sw_address': 3015, 'address': 815, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV01F_1', 'img_id': 'op1_AV01F_img1','left': '204px','top': '100px', 'sw_address': 3016, 'address': 816, 'type':'ON', 'name':'OPEN', 'reverse': False},
    # 左の列 OFFスイッチ
    {'id': 'op1_AV1_2', 'img_id': 'op1_AV1_img2', 'left': '336px','top': '100px', 'sw_address': 3218, 'address': 818, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV2_2', 'img_id': 'op1_AV2_img2','left': '336px','top': '100px', 'sw_address': 3219, 'address': 819, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV3_2', 'img_id': 'op1_AV3_img2','left': '336px','top': '100px', 'sw_address': 3220, 'address': 820, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV4_2', 'img_id': 'op1_AV4_img2','left': '336px','top': '100px', 'sw_address': 3222, 'address': 822, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV5_2', 'img_id': 'op1_AV5_img2','left': '336px','top': '100px', 'sw_address': 3221, 'address': 821, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV6_2', 'img_id': 'op1_AV6_img2','left': '336px','top': '100px', 'sw_address': 3223, 'address': 823, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV7_2', 'img_id': 'op1_AV7_img2','left': '336px','top': '100px', 'sw_address': 3217, 'address': 817, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV8_2', 'img_id': 'op1_AV8_img2','left': '336px','top': '100px', 'sw_address': 3229, 'address': 829, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV01_2', 'img_id': 'op1_AV01_img2','left': '336px','top': '100px', 'sw_address': 3215, 'address': 815, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV01F_2', 'img_id': 'op1_AV01F_img2','left': '336px','top': '100px', 'sw_address': 3216, 'address': 816, 'type':'OFF', 'name':'CLOSE', 'reverse': True},

    # 真ん中の列 ONスイッチ
    {'id': 'op1_AV02_1', 'img_id': 'op1_AV02_img1', 'left': '664px','top': '100px', 'sw_address': 3014, 'address': 814, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV09_1', 'img_id': 'op1_AV09_img1', 'left': '664px','top': '100px', 'sw_address': 3030, 'address': 830, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV10_1', 'img_id': 'op1_AV10_img1','left': '664px','top': '100px', 'sw_address': 3031, 'address': 831, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV11_1', 'img_id': 'op1_AV11_img1','left': '664px','top': '100px', 'sw_address': 3032, 'address': 832, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_AV12_1', 'img_id': 'op1_AV12_img1','left': '664px','top': '100px', 'sw_address': 3033, 'address': 833, 'type':'ON', 'name':'OPEN', 'reverse': False},
    {'id': 'op1_RP1_1', 'img_id': 'op1_RP1_img1','left': '664px','top': '100px', 'sw_address': 3061, 'address': 861, 'type':'ON', 'name':'ON', 'reverse': False},
    {'id': 'op1_TMP1_1', 'img_id': 'op1_TMP1_img1','left': '664px','top': '100px', 'sw_address': 3062, 'address': 862, 'type':'ON', 'name':'ON', 'reverse': False},
    #{'id': 'op1_auto1_1', 'img_id': 'op1_auto1_img1','left': '664px','top': '100px', 'sw_address': 3097, 'address': 897, 'type':'ON', 'name':'ON', 'reverse': False},
    #{'id': 'op1_auto2_1', 'img_id': 'op1_auto2_img1','left': '664px','top': '100px', 'sw_address': 3098, 'address': 898, 'type':'ON', 'name':'ON', 'reverse': False},
    #{'id': 'op1_auto3_1', 'img_id': 'op1_auto3_img1','left': '664px','top': '100px', 'sw_address': 3099, 'address': 899, 'type':'ON', 'name':'ON', 'reverse': False},
    # 真ん中の列 OFFスイッチ
    {'id': 'op1_AV02_2', 'img_id': 'op1_AV02_img2', 'left': '796px','top': '100px', 'sw_address': 3214, 'address': 814, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV09_2', 'img_id': 'op1_AV09_img2', 'left': '796px','top': '100px', 'sw_address': 3230, 'address': 830, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV10_2', 'img_id': 'op1_AV10_img2','left': '796px','top': '100px', 'sw_address': 3231, 'address': 831, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV11_2', 'img_id': 'op1_AV11_img2','left': '796px','top': '100px', 'sw_address': 3232, 'address': 832, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_AV12_2', 'img_id': 'op1_AV12_img2','left': '796px','top': '100px', 'sw_address': 3233, 'address': 833, 'type':'OFF', 'name':'CLOSE', 'reverse': True},
    {'id': 'op1_RP1_2', 'img_id': 'op1_RP1_img2','left': '796px','top': '100px', 'sw_address': 3261, 'address': 861, 'type':'OFF', 'name':'OFF', 'reverse': True},
    {'id': 'op1_TMP1_2', 'img_id': 'op1_TMP1_img2','left': '796px','top': '100px', 'sw_address': 3262, 'address': 862, 'type':'OFF', 'name':'OFF', 'reverse': True},
    #{'id': 'op1_auto1_2', 'img_id': 'op1_auto1_img2','left': '796px','top': '100px', 'sw_address': 3297, 'address': 908, 'type':'OFF', 'name':'OFF', 'reverse': True},
    #{'id': 'op1_auto2_2', 'img_id': 'op1_auto2_img2','left': '796px','top': '100px', 'sw_address': 3298, 'address': 909, 'type':'OFF', 'name':'OFF', 'reverse': True},
    #{'id': 'op1_auto3_2', 'img_id': 'op1_auto3_img2','left': '796px','top': '100px', 'sw_address': 3299, 'address': 910, 'type':'OFF', 'name':'OFF', 'reverse': True},
]
button2_data = [
    # 右の列 ONスイッチ
    {'id': 'op1_SVM2_OP', 'img_id': 'op1_SVM2_op_img', 'left': '1124px','top': '8px', 'sw_address': 3068, 'address': 904, 'type':'ON', 'name':'OPEN', 'reverse': False,
    'font_size':'20px'},
    {'id': 'op1_SVM2_Dg_1', 'img_id': 'op1_SVM2_dg_1_img','left': '1124px','top': '80px', 'sw_address': 3069, 'address': 869, 'type':'ON', 'name':'START', 'reverse': False,
     'font_size':'20px'},
    {'id': 'op1_SVM2_PaE_1', 'img_id': 'op1_SVM2_PaE_1_img','left': '1124px','top': '224px', 'sw_address': 3095, 'address': 895, 'type':'ON', 'name':'有効', 'reverse': False,
    'font_size':'20px'},
    {'id': 'op1_SVM2_PaC_1', 'img_id': 'op1_SVM2_PaC_1_img','left': '1124px','top': '296px', 'sw_address': 3070, 'address': 907, 'type':'ON', 'name':'START', 'reverse': False,
    'font_size':'20px'},
    #{'id': 'op1_SVM1_SV_1', 'img_id': 'op1_SVM1_SV_1_img','left': '1124px','top': '440px', 'sw_address': 3096, 'address': 896, 'type':'ON', 'name':'ON', 'reverse': False,
    #'font_size':'20px'},

    {'id': 'op1_SVM2_CL', 'img_id': 'op1_SVM2_cl_img', 'left': '1256px','top': '8px', 'sw_address': 3268, 'address': 905, 'type':'OFF', 'name':'CLOSE', 'reverse': False,
     'font_size':'20px'},
    {'id': 'op1_SVM2_Dg_2', 'img_id': 'op1_SVM2_dg_2_img','left': '1256px','top': '80px', 'sw_address': 3269, 'address': 869, 'type':'OFF', 'name':'STOP', 'reverse': True,
     'font_size':'20px'},
    {'id': 'op1_SVM2_PaE_2', 'img_id': 'op1_SVM2_PaE_2_img', 'left': '1256px','top': '224px', 'sw_address': 3295, 'address': 895, 'type':'OFF', 'name':'無効', 'reverse': True,
     'font_size':'20px'},
    {'id': 'op1_SVM2_PaC_2', 'img_id': 'op1_SVM2_PaC_2_img','left': '1256px','top': '296px', 'sw_address': 3270, 'address': 907, 'type':'OFF', 'name':'STOP', 'reverse': True,
     'font_size':'20px'},
    #{'id': 'op1_SVM1_SV_2', 'img_id': 'op1_SVM1_SV_2_img','left': '1256px','top': '440px', 'sw_address': 3296, 'address': 896, 'type':'OFF', 'name':'OFF', 'reverse': True,
    #'font_size':'20px'},
]
# ロギングボタン
log_button_data = [
    {'id': 'op1_log_bt', 'img_id': 'op1_log_bt_img1', 'left': '1124px','top': '512px', 'sw_address': 3600, 'address': 3601, 'type':'ON', 'name':'ロギング', 'reverse': False,
     'src': '/assets/images/PlasticSquare_G.png'},
]
# 積算リセットボタン
reset_button_data2 = [
    {'id': 'op1-plas-reset', 'left': '1124px', 'top': '584px', 'sw_address': 510, 'name': 'リセット'},
]
# ダミーボタン (なぜか画面表示時にボタンクリックイベントが起こるので、ダミーを用意する)
dummy_button_data = [
    # 左の列 ONスイッチ
    {'id': 'op1_dummy', 'img_id': 'op1_dummy_img1', 'left': '204px','top': '100px', 'sw_address': 0, 'address': 818, 'type':'ON', 'name':'OPEN', 'reverse': False},
]


BASE_TOP = 8
# ラベルのy座標の再割り当て
for i, item in enumerate(text_data):
    index = i % 10
    item['top'] = f'{index*72+BASE_TOP}px'  # itemはtext_list[i]と同じ辞書への参照なので、itemを更新すれば元のリストも更新される

# ボタンのy座標の再割り当て（レイアウトの表示を見て、新たなBASE_TOPを作るか確認すること）
COLUM5_RAW6 = 20+7 #20 + 8     # 3列目は8行目まで
for i, item in enumerate(button_data):
    index = 0
    if i >= COLUM5_RAW6:
        index = i - COLUM5_RAW6
    else:
        index = i % 10
    item['top'] = f'{index*72+BASE_TOP}px'

ope1button_src_indicators = (
    dummy_button_data +
    button_data +
    button2_data
)
ope1_buttons = ope1button_src_indicators + log_button_data + reset_button_data2

# --------------------------------------------------------
# モニターと設定の入力ボックスのリスト
# コールバックで'children'を変更します
# --------------------------------------------------------
setting_data = [
    {'id': 'op1_SVM2_Dg_SV', 'left': '1124px','top': '152px', 'address': 4028, 'data_index': 14,
     'format': FormatSpecifier.F3_2, 'trigger_id': 'op1_SVM2_Dg_trigger',
     'name': 'SVM2 開度設定値SV', 'min_value': 0.0, 'max_value': 100.0},
    {'id': 'op1_SVM2_Pa_SV', 'left': '1124px','top': '368px', 'address': 4030, 'data_index': 15,
     'format': FormatSpecifier.FE_NOTATION, 'trigger_id': 'op1_SVM2_Pa_trigger',
     'name': 'SVM2 圧力制御SV', 'min_value': 0.01, 'max_value': 100.0},
]

# インターロックランプ
lamp_data = [
    # 左の列 ランプ
    {'id': 'op1_AV1LP_1', 'img_id': 'op1_AV1LP_img1', 'left': '176px','top': '100px', 'address': 3418},
    {'id': 'op1_AV2LP_1', 'img_id': 'op1_AV2LP_img1','left': '176px','top': '100px', 'address': 3419},
    {'id': 'op1_AV3LP_1', 'img_id': 'op1_AV3LP_img1','left': '176px','top': '100px', 'address': 3420},
    {'id': 'op1_AV4LP_1', 'img_id': 'op1_AV4LP_img1','left': '176px','top': '100px', 'address': 3422},
    {'id': 'op1_AV5LP_1', 'img_id': 'op1_AV5LP_img1','left': '176px','top': '100px', 'address': 3421},
    {'id': 'op1_AV6LP_1', 'img_id': 'op1_AV6LP_img1','left': '176px','top': '100px', 'address': 3423},
    {'id': 'op1_AV7LP_1', 'img_id': 'op1_AV7LP_img1','left': '176px','top': '100px', 'address': 3417},
    {'id': 'op1_AV8LP_1', 'img_id': 'op1_AV8LP_img1','left': '176px','top': '100px', 'address': 3429},
    {'id': 'op1_AV01LP_1', 'img_id': 'op1_AV01LP_img1','left': '176px','top': '100px', 'address': 3415},
    {'id': 'op1_AV01FLP_1', 'img_id': 'op1_AV01FLP_img1','left': '176px','top': '100px', 'address': 3416},
    # 真ん中の列 ランプ
    {'id': 'op1_AV02LP_1', 'img_id': 'op1_AV02LP_img1', 'left': '636px','top': '100px', 'address': 3414},
    {'id': 'op1_AV09LP_1', 'img_id': 'op1_AV09LP_img1', 'left': '636px','top': '100px', 'address': 3430},
    {'id': 'op1_AV10LP_1', 'img_id': 'op1_AV10LP_img1','left': '636px','top': '100px', 'address': 3431},
    {'id': 'op1_AV11LP_1', 'img_id': 'op1_AV11LP_img1','left': '636px','top': '100px', 'address': 3432},
    {'id': 'op1_AV12LP_1', 'img_id': 'op1_AV12LP_img1','left': '636px','top': '100px', 'address': 3433},
    {'id': 'op1_RP1LP_1', 'img_id': 'op1_RP1LP_img1','left': '636px','top': '100px', 'address': 3461},
    {'id': 'op1_TMP1LP_1', 'img_id': 'op1_TMP1LP_img1','left': '636px','top': '100px', 'address': 3462},
    #{'id': 'op1_auto1LP_1', 'img_id': 'op1_auto1LP_img1','left': '636px','top': '100px', 'address': 3497},
    #{'id': 'op1_auto2LP_1', 'img_id': 'op1_auto2LP_img1','left': '636px','top': '100px', 'address': 3498},
    #{'id': 'op1_auto3LP_1', 'img_id': 'op1_auto3LP_img1','left': '636px','top': '100px', 'address': 3499},
    # 右の列 ランプ
    #
]
lamp2_data = [
    # 左の列 ランプ
    {'id': 'op1_RP1LP_2', 'img_id': 'op1_RP1LP_img2', 'left': '636px','top': '400px', 'address': 3413},
    # 右の列 ランプ     
    {'id': 'op1_SVM2_OPLP_1', 'img_id': 'op1_SVM2_OPLP_img1','left': '1096px','top': '12px', 'address': 3468},
    {'id': 'op1_SVM2_DgLP_1', 'img_id': 'op1_SVM2_DgLP_img1','left': '1096px','top': '84px', 'address': 3469},
    {'id': 'op1_SVM2_PaLP_1', 'img_id': 'op1_SVM2_PaLP_img1','left': '1096px','top': '300px', 'address': 3470},
]

LP_BASE_TOP = 12
# ランプのy座標の再割り当て（レイアウトの表示を見て、新たなBASE_TOPを作るか確認すること）
LP_COLUM5_RAW6 = 1000 #10 + 7     # 2列目は7行目まで
for i, item in enumerate(lamp_data):
    index = 0
    if i >= LP_COLUM5_RAW6:
        index = i - LP_COLUM5_RAW6
    else:
        index = i % 10
    item['top'] = f'{index*72+LP_BASE_TOP}px'

ope1lamp_src_indicators = (
    lamp_data +
    lamp2_data
)

# 四角い線を定義する関数
def _add_rectangle(layout, left, top, width, height, color, z_index=1):
    style = {
        'position': 'absolute',
        'left': f'{left}px',
        'top': f'{top}px',
        'width': f'{width}px',
        'height': f'{height}px',
        'border': f'1px solid {color}',
        'z-index': z_index
    }
    layout.append(html.Div(style=style))

def _add_button(layout, button_list):
    font_size = '20px'
    for data in button_list:
        children=[
            # 1. 画像 (背景または状態表示)
            html.Img(
                id=data['img_id'], # Img ID をコールバックの Output に使う
                src='/assets/images/PlasticSquare_G.png',
                style={'width': '100%', 'height': '100%',
                        'position': 'absolute', # ボタン内に配置
                        'left': '0', 'top': '0',
                        'zIndex': 1 # テキストより下
                    }
            ),
            # 2. テキスト (「ON」または「OFF」の文字)
            html.Div(
                data['name'],
                style={
                    'position': 'absolute',
                    # ボタンの中央に配置
                    'top': '50%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)', # CSSで完全な中央揃え
                    'fontSize': f'{font_size}',
                    'whiteSpace': 'nowrap',  # 折り返しを無効にする
                    'fontFamily': 'Meiryo UI',
                    'fontWeight': 'bold',
                    'color': 'black', # 文字色
                    'zIndex': 2 # 画像より上
                }
            )
        ]
        style={
            'position': 'absolute',
            'left': data['left'], 'top': data['top'],
            'width': '128px', 'height': '64px',
            'zIndex': 5,
            # children の absolute 配置を基準にするため、position: relative は必須
            #'position': 'relative', 
            'padding': '0', # Paddingを除去して画像を表示
            'border': 'none', # ボーダーを除去
            'background': 'none',# 背景を除去
            #'overflow': 'hidden' # 子要素がはみ出さないように
        }
        # ダミーは表示しない
        if data['id'] == 'op1_dummy':
            style['display'] = 'none'

        layout.append(html.Button(id=data['id'], n_clicks=0, children=children, style=style))

def _add_lamp(layout, data):
    children=[
        # 1. 画像 (背景または状態表示)
        html.Img(
            id=data['img_id'], # Img ID をコールバックの Output に使う
            src='/assets/images/RealCircle2_R.png',
            style={'width': '100%', 'height': '100%',
                    'position': 'absolute', # ボタン内に配置
                    'left': '0', 'top': '0',
                    'zIndex': 1 # テキストより下
                }
        ),
    ]
    style={
        'position': 'absolute',
        'left': data['left'], 'top': data['top'],
        'width': '24px', 'height': '24px',
        'zIndex': 5,
        'padding': '0', # Paddingを除去して画像を表示
        'border': 'none', # ボーダーを除去
        'background': 'none',# 背景を除去
    }
    
    layout.append(html.Div(id=data['id'], children=children, style=style))

def _add_backgrounds(layout, bg_list, color, border_style, z_index):
    """汎用的な背景Div要素をレイアウトに追加するヘルパー関数"""
    for bg in bg_list:
        layout.append(html.Div(style={
            'position': 'absolute',
            'left': bg['left'],
            'top': bg['top'],
            'width': bg['width'],
            'height': bg['height'],
            'backgroundColor': color,
            'border': border_style,
            'zIndex': z_index,
        }))

def _add_text(layout, label_list):
    for i,data in enumerate(label_list):
        # # 'left'と'top'の値からpxを除去し、オフセットを適用
        id = f'op1_text{i}'
        left_val = int(data['left'].replace('px', '')) + 16
        top_val = int(data['top'].replace('px', '')) - 12
        parts = data['text'].split(NEWLINE)
        if len(parts) >= 2:
            # 改行で2段に分ける（3段表示は考慮しない）
            children = [
                html.Span(parts[0]),
                html.Br(),
                html.Span(parts[1])
            ]
        else:
            children = data['text']
        
        style={
            'position': 'absolute',
            'left': f'{left_val}px',
            'top': f'{top_val}px',
            'fontSize': '20px',
            #'fontWeight': 'bold',
            'color': 'black',
            'fontFamily': 'Meiryo UI',
            'zIndex': 5,
        }
        layout.append(html.P(id=id, children=children, style=style))

def create_operation1_layout():
    # Content-3 (操作エリア) のモード 1 用レイアウト
    layout = []

    # 1. 四角の線 (z-index: 1)
    _add_rectangle(layout, left=950, top=4, width=447, height=435, color='#999999', z_index=1)

    # 2. テキスト (z-index: 5)
    text_data_set = text_data + text_data2
    _add_text(layout, text_data_set)

    # 3. 操作ボタン (z-index: 5)
    _add_button(layout, ope1button_src_indicators)
    _add_button(layout, log_button_data)

    # 3.リセットボタン
    data = reset_button_data2[0]
    layout.append(html.Button(
        id=data['id'],
        n_clicks=0,
        children=[
            # 1. 画像 (背景または状態表示)
            html.Img(
                src='/assets/images/PlasticRect_Y.png',
                style={'width': '100%', 'height': '100%',
                        'position': 'absolute', # ボタン内に配置
                        'left': '0', 'top': '0',
                        'zIndex': 1 # テキストより下
                    }
            ),
            # 2. テキスト (「ON」または「OFF」の文字)
            html.Div(
                data['name'],
                style={
                    'position': 'absolute',
                    # ボタンの中央に配置
                    'top': '50%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)', # CSSで完全な中央揃え
                    'fontSize': '20px',
                    'fontFamily': 'Meiryo UI',
                    'fontWeight': 'bold',
                    'color': 'black', # 文字色
                    'zIndex': 2 # 画像より上
                }
            )
        ],
        style={
            'position': 'absolute',
            'left': data['left'], 'top': data['top'],
            'width': '128px', 'height': '64px',
            'fontSize': '18px',
            'zIndex': 5,
            
            'padding': '0', # Paddingを除去して画像を表示
            'border': 'none', # ボーダーを除去
            'background': 'none',# 背景を除去
            'overflow': 'hidden' # 子要素がはみ出さないように
        }
    ))

    # 4. インターロックランプの追加
    for data in ope1lamp_src_indicators:
        _add_lamp(layout, data)

        
    # 5. ダミーコンポーネント (操作ボタンのOutコールバック用)
    layout.append(
        html.Div(id='dummy-button-op1', style={'display': 'none'})
    )

    # 7. 設定値 (z-index: 5)
    for data in setting_data:
        top_value = int(data['top'].replace('px', '')) + 4
        className='operation_setting-style clickable-setting' # 新しいCSSクラスを追加
        style = {
            'position': 'absolute',
            'left': data['left'],
            'top': f'{top_value}px',
            'zIndex': 5,
        }
        # この html.Div がクリックされたら、隠された dcc.Store を更新する
        layout.append(html.Div(
            data['id'], 
            id=data['id'], 
            n_clicks=0, # クリックを監視
            className=className, 
            style=style
        ))

    # 8. ポップアップ用のレイアウト
    create_setting_modal(layout, '-op1')

    return layout