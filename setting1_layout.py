from dash import html
from constans import FormatSpecifier

from common_modal_layout import create_setting_modal

# --------------------------------------------------------
# テキストとアドレスのリスト
# --------------------------------------------------------
# 改行文字コード（自由に変更可）
NEWLINE = '<br>'
label_text_data = [
    # 左の列
    {'left': '36px', 'top': '100px', 'text': 'PS01'+NEWLINE+'エア元圧'},
    {'left': '36px', 'top': '100px', 'text': 'RF'+NEWLINE+'整合器温度'},
    {'left': '36px', 'top': '100px', 'text': 'RF'+NEWLINE+'着火中圧力'},
    {'left': '36px', 'top': '100px', 'text': '----'+NEWLINE+'チャンバー昇温'},
    {'left': '36px', 'top': '100px', 'text': 'H1/H2'+NEWLINE+'加熱中圧力'},
    {'left': '36px', 'top': '100px', 'text': 'CH1'+NEWLINE+'冷却水温度'},
    {'left': '36px', 'top': '100px', 'text': 'SVM3'+NEWLINE+'A室基準ロール径'},
    {'left': '36px', 'top': '100px', 'text': 'SVM4'+NEWLINE+'B室基準ロール径'},
    {'left': '36px', 'top': '100px', 'text': 'COMON'+NEWLINE+'素材圧'},
    {'left': '36px', 'top': '100px', 'text': 'COMON'+NEWLINE+'最大巻径'},
    {'left': '36px', 'top': '100px', 'text': '----'+NEWLINE+'厚み測定適正値'},
    {'left': '36px', 'top': '100px', 'text': 'SVM2'+NEWLINE+'開度調整'},
    {'left': '36px', 'top': '100px', 'text': 'SVM3'+NEWLINE+'A室テンション制御'},
    {'left': '36px', 'top': '100px', 'text': 'SVM4'+NEWLINE+'B室テンション制御'},
    {'left': '36px', 'top': '100px', 'text': 'GASD1'+NEWLINE+'H2 ガスリーク'},
    {'left': '36px', 'top': '100px', 'text': 'GASD2'+NEWLINE+'CH4 ガスリーク'},
    {'left': '36px', 'top': '100px', 'text': 'GASD3'+NEWLINE+'O2 ガスリーク'},
    {'left': '36px', 'top': '100px', 'text': 'SVM2'+NEWLINE+'開度調整'},
    # 右の列
    {'left': '36px', 'top': '100px', 'text': 'FLU1'+NEWLINE+'TMP1 N2パージ'},
    {'left': '36px', 'top': '100px', 'text': 'FLU2'+NEWLINE+'RP1 N2パージ'},    
    {'left': '36px', 'top': '100px', 'text': 'FLM1'+NEWLINE+'RF電源'},
    {'left': '36px', 'top': '100px', 'text': 'FLM2'+NEWLINE+'自動整合器'},
    {'left': '36px', 'top': '100px', 'text': 'FLM3'+NEWLINE+'上部電極'},
    {'left': '36px', 'top': '100px', 'text': 'FLM4'+NEWLINE+'チャンバー1'},
    {'left': '36px', 'top': '100px', 'text': 'FLM5'+NEWLINE+'チャンバー2'},
    {'left': '36px', 'top': '100px', 'text': 'FLM6'+NEWLINE+'ヒーターステージ'},
    {'left': '36px', 'top': '100px', 'text': 'PT1 H2'+NEWLINE+'ガスレギュレーター'},
    {'left': '36px', 'top': '100px', 'text': 'PT2 CH4'+NEWLINE+'ガスレギュレーター'},
    {'left': '36px', 'top': '100px', 'text': 'PT3 O2'+NEWLINE+'ガスレギュレーター'},
    {'left': '36px', 'top': '100px', 'text': 'PT4 Ar'+NEWLINE+'ガスレギュレーター'},
    {'left': '36px', 'top': '100px', 'text': 'PT5 N2'+NEWLINE+'ガスレギュレーター'},
    {'left': '36px', 'top': '100px', 'text': 'PT6 H2'+NEWLINE+'ガスレギュレーター'},
    {'left': '36px', 'top': '100px', 'text': 'PT7 Ar'+NEWLINE+'ガスレギュレーター'},
]
unit_text_data = [
    # 左の列
    {'left': '256px', 'top': '100px', 'text': '圧力'+NEWLINE+'(kPa(G))'},
    {'left': '256px', 'top': '100px', 'text': '温度'+NEWLINE+'(℃)'},
    {'left': '256px', 'top': '100px', 'text': '圧力'+NEWLINE+'(Pa)'},
    {'left': '256px', 'top': '100px', 'text': '温度'+NEWLINE+'(℃)'},
    {'left': '256px', 'top': '100px', 'text': '圧力'+NEWLINE+'(Pa)'},
    {'left': '256px', 'top': '100px', 'text': '温度'+NEWLINE+'(℃)'},
    {'left': '256px', 'top': '100px', 'text': '距離'+NEWLINE+'(mm)'},
    {'left': '256px', 'top': '100px', 'text': '距離'+NEWLINE+'(mm)'},
    {'left': '256px', 'top': '100px', 'text': '厚み'+NEWLINE+'(mm)'},
    {'left': '256px', 'top': '100px', 'text': '厚み'+NEWLINE+'(mm)'},
    {'left': '256px', 'top': '100px', 'text': '厚み'+NEWLINE+'(mm)'},
    {'left': '256px', 'top': '100px', 'text': 'チューニング入力'+NEWLINE+'閾値 (Pa(Abs))'},
    {'left': '256px', 'top': '100px', 'text': 'チューニング入力'+NEWLINE+'閾値 (°)'},
    {'left': '256px', 'top': '100px', 'text': 'チューニング入力'+NEWLINE+'閾値 (°)'},
    {'left': '256px', 'top': '100px', 'text': '濃度'+NEWLINE+'(ppm)'},
    {'left': '256px', 'top': '100px', 'text': '濃度'+NEWLINE+'(ppm)'},
    {'left': '256px', 'top': '100px', 'text': 'リーク'+NEWLINE+'(%)'},
    {'left': '256px', 'top': '100px', 'text': '開度'+NEWLINE+'(%)'},
    # 右の列
    {'left': '256px', 'top': '100px', 'text': '流量'+NEWLINE+'(L/min)'},
    {'left': '256px', 'top': '100px', 'text': '流量'+NEWLINE+'(L/min)'},
    {'left': '256px', 'top': '100px', 'text': '流量'+NEWLINE+'(L/min)'},
    {'left': '256px', 'top': '100px', 'text': '流量'+NEWLINE+'(L/min)'},
    {'left': '256px', 'top': '100px', 'text': '流量'+NEWLINE+'(L/min)'},
    {'left': '256px', 'top': '100px', 'text': '流量'+NEWLINE+'(L/min)'},
    {'left': '256px', 'top': '100px', 'text': '流量'+NEWLINE+'(L/min)'},
    {'left': '256px', 'top': '100px', 'text': '流量'+NEWLINE+'(L/min)'},
    {'left': '256px', 'top': '100px', 'text': '圧力'+NEWLINE+'(kPa(G))'},
    {'left': '256px', 'top': '100px', 'text': '圧力'+NEWLINE+'(kPa(G))'},
    {'left': '256px', 'top': '100px', 'text': '圧力'+NEWLINE+'(kPa(G))'},
    {'left': '256px', 'top': '100px', 'text': '圧力'+NEWLINE+'(kPa(G))'},
    {'left': '256px', 'top': '100px', 'text': '圧力'+NEWLINE+'(kPa(G))'},
    {'left': '256px', 'top': '100px', 'text': '圧力'+NEWLINE+'(kPa(G))'},
    {'left': '256px', 'top': '100px', 'text': '圧力'+NEWLINE+'(kPa(G))'},
]
limit_text_data = [
    {'left': '376px', 'top': '8px', 'text': '上限'},
    {'left': '508px', 'top': '8px', 'text': '下限'},
    {'left': '1040px', 'top': '8px', 'text': '上限'},
    {'left': '1172px', 'top': '8px', 'text': '下限'},
]
# --------------------------------------------------------
# モニターと設定の入力ボックスのリスト
# コールバックで'children'を変更します
# --------------------------------------------------------
BASE_INDEX = 70 # D4100のインデックスは70番目と想定
setting_upper_data = [
    {'id': 'set1_PS01_pa1', 'left': '356px','top': '8px', 'address': 4160, 'data_index': BASE_INDEX + 30,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PS01_1_trigger',
        'name': 'PS01 エア元圧 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_RF1_tem', 'left': '356px','top': '80px', 'address': 4192, 'data_index': BASE_INDEX + 46,
        'format': FormatSpecifier.F3_2, 'trigger_id': 'set1_RF1_trigger',
        'name': 'RF 整合器温度 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_RF1_heatPa', 'left': '356px','top': '80px', 'address': 4194, 'data_index': BASE_INDEX + 47,
        'format': FormatSpecifier.F3_2, 'trigger_id': 'set1_RF1_heatPa_trigger',
        'name': 'RF 着火中圧力 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_cha_tem', 'left': '356px','top': '152px', 'address': 4118, 'data_index': BASE_INDEX + 9,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_cha_trigger',
        'name': 'チャンバー昇温', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_H1_heatPa', 'left': '356px','top': '80px', 'address': 4196, 'data_index': BASE_INDEX + 48,
        'format': FormatSpecifier.F3_2, 'trigger_id': 'set1_H1_heatPa_trigger',
        'name': 'RF 加熱中圧力 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_CH1_tem', 'left': '356px','top': '224px', 'address': 4120, 'data_index': BASE_INDEX + 10,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_CH1_trigger',
        'name': '冷却水温度', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_SVM3_kei', 'left': '356px','top': '296px', 'address': 4100, 'data_index': BASE_INDEX,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_SVM3_kei_trigger',
        'name': 'A室基準ロール径', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_SVM4_kei', 'left': '356px','top': '368px', 'address': 4102, 'data_index': BASE_INDEX + 1,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_SVM4_kei_trigger',
        'name': 'B室基準ロール径', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_COMON_atu', 'left': '356px','top': '440px', 'address': 4104, 'data_index': BASE_INDEX + 2,
        'format': FormatSpecifier.F3_2, 'trigger_id': 'set1_COMON_atu_trigger',
        'name': 'COMON 素材圧', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_COMON_kei', 'left': '356px','top': '440px', 'address': 4106, 'data_index': BASE_INDEX + 3,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_COMON_kei_trigger',
        'name': 'COMON 最大巻径', 'min_value': 0.0, 'max_value': 500.0},
    
    {'id': 'set1_atumi_tekisei1', 'left': '356px','top': '440px', 'address': 4110, 'data_index': BASE_INDEX + 5,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_atumi1_trigger',
        'name': '厚み測定適正値 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_SVM2_kaido', 'left': '356px','top': '440px', 'address': 4116, 'data_index': BASE_INDEX + 8,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_SVM2_kaido_trigger',
        'name': 'SVM2 開度調整', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_SVM3_Acon', 'left': '356px','top': '440px', 'address': 4112, 'data_index': BASE_INDEX + 6,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_SVM3_Acon_trigger',
        'name': 'SVM3 A室テンション制御', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_SVM4_Bcon', 'left': '356px','top': '440px', 'address': 4114, 'data_index': BASE_INDEX + 7,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_SVM4_Bcon_trigger',
        'name': 'SVM4 B室テンション制御', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_GASD1_H2', 'left': '356px','top': '440px', 'address': 4122, 'data_index': BASE_INDEX + 11,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_GASD1_trigger',
        'name': 'GASD1 H2ガスリーク', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_GASD2_CH4', 'left': '356px','top': '440px', 'address': 4124, 'data_index': BASE_INDEX + 12,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_GASD2_trigger',
        'name': 'GASD2 CH4ガスリーク', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_GASD3_O2', 'left': '356px','top': '440px', 'address': 4126, 'data_index': BASE_INDEX + 13,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_GASD3_trigger',
        'name': 'GASD3 O2ガスリーク', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_SVM2_limit1', 'left': '356px','top': '440px', 'address': 4052, 'data_index': 26,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_SVM2_limit1_trigger',
        'name': 'SVM2 開度調整 上限', 'min_value': 0.0, 'max_value': 500.0},

    {'id': 'set1_TMP1_N2', 'left': '356px','top': '440px', 'address': 4132, 'data_index': BASE_INDEX + 16,
        'format': FormatSpecifier.F3_3, 'trigger_id': 'set1_TMP1_1_trigger',
        'name': 'TMP1 N2パージ 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_RP1_N2', 'left': '356px','top': '440px', 'address': 4128, 'data_index': BASE_INDEX + 14,
        'format': FormatSpecifier.F3_3, 'trigger_id': 'set1_RP1_1_trigger',
        'name': 'RP1 N2パージ 上限', 'min_value': 0.0, 'max_value': 500.0},    
    {'id': 'set1_FLM1', 'left': '356px','top': '440px', 'address': 4136, 'data_index': BASE_INDEX + 18,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_FLM1_1_trigger',
        'name': 'FLM1 RF電源 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_FLM2', 'left': '356px','top': '440px', 'address': 4140, 'data_index': BASE_INDEX + 20,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_FLM2_1_trigger',
        'name': 'FLM2 自動整合器 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_FLM3', 'left': '356px','top': '440px', 'address': 4144, 'data_index': BASE_INDEX + 22,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_FLM3_1_trigger',
        'name': 'FLM3 上部電極 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_FLM4', 'left': '356px','top': '440px', 'address': 4148, 'data_index': BASE_INDEX + 24,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_FLM4_1_trigger',
        'name': 'FLM4 チャンバー1 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_FLM5', 'left': '356px','top': '440px', 'address': 4152, 'data_index': BASE_INDEX + 26,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_FLM5_1_trigger',
        'name': 'FLM5 チャンバー2 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_FLM6', 'left': '356px','top': '440px', 'address': 4156, 'data_index': BASE_INDEX + 28,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_FLM6_1_trigger',
        'name': 'FLM6 ヒーターステージ 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT1', 'left': '356px','top': '440px', 'address': 4164, 'data_index': BASE_INDEX + 32,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT1_1_trigger',
        'name': 'PT1 H2ガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT2', 'left': '356px','top': '440px', 'address': 4168, 'data_index': BASE_INDEX + 34,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT2_1_trigger',
        'name': 'PT2 CH4ガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT3', 'left': '356px','top': '440px', 'address': 4172, 'data_index': BASE_INDEX + 36,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT3_1_trigger',
        'name': 'PT3 O2ガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT4', 'left': '356px','top': '440px', 'address': 4176, 'data_index': BASE_INDEX + 38,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT4_1_trigger',
        'name': 'PT4 Arガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT5', 'left': '356px','top': '440px', 'address': 4180, 'data_index': BASE_INDEX + 40,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT5_1_trigger',
        'name': 'PT5 N2ガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT6', 'left': '356px','top': '440px', 'address': 4184, 'data_index': BASE_INDEX + 42,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT6_1_trigger',
        'name': 'PT6 H2ガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT7', 'left': '356px','top': '440px', 'address': 4188, 'data_index': BASE_INDEX + 44,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT7_1_trigger',
        'name': 'PT7 Arガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
]
setting_low_data = [
    {'id': 'set1_PS01_pa2', 'left': '356px','top': '8px', 'address': 4162, 'data_index': BASE_INDEX + 31,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PS01_2_trigger',
        'name': 'PS01 エア元圧 下限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'set1_atumi_tekisei2', 'left': '356px','top': '440px', 'address': 4108, 'data_index': BASE_INDEX + 4,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_atumi2_trigger',
        'name': '厚み測定適正値 下限', 'min_value': 0.0, 'max_value': 500.0},    
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'N/A'},
    {'id': 'set1_SVM2_limit2', 'left': '356px','top': '440px', 'address': 4054, 'data_index': 27,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_SVM2_limit2_trigger',
        'name': 'SVM2 開度調整 下限', 'min_value': 0.0, 'max_value': 500.0},

    {'id': 'set1_TMP1_N2_2', 'left': '356px','top': '440px', 'address': 4134, 'data_index': BASE_INDEX + 17,
        'format': FormatSpecifier.F3_3, 'trigger_id': 'set1_TMP1_2_trigger',
        'name': 'TMP1 N2パージ 下限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_RP1_N2_2', 'left': '356px','top': '440px', 'address': 4130, 'data_index': BASE_INDEX + 15,
        'format': FormatSpecifier.F3_3, 'trigger_id': 'set1_RP1_2_trigger',
        'name': 'RP1 N2パージ 下限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_FLM1_2', 'left': '356px','top': '440px', 'address': 4138, 'data_index': BASE_INDEX + 19,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_FLM1_2_trigger',
        'name': 'FLM1 RF電源 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_FLM2_2', 'left': '356px','top': '440px', 'address': 4142, 'data_index': BASE_INDEX + 21,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_FLM2_2_trigger',
        'name': 'FLM2 自動整合器 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_FLM3_2', 'left': '356px','top': '440px', 'address': 4146, 'data_index': BASE_INDEX + 23,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_FLM3_2_trigger',
        'name': 'FLM3 上部電極 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_FLM4_2', 'left': '356px','top': '440px', 'address': 4150, 'data_index': BASE_INDEX + 25,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_FLM4_2_trigger',
        'name': 'FLM4 チャンバー1 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_FLM5_2', 'left': '356px','top': '440px', 'address': 4154, 'data_index': BASE_INDEX + 27,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_FLM5_2_trigger',
        'name': 'FLM5 チャンバー2 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_FLM6_2', 'left': '356px','top': '440px', 'address': 4158, 'data_index': BASE_INDEX + 29,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_FLM6_2_trigger',
        'name': 'FLM6 ヒーターステージ 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT1_2', 'left': '356px','top': '440px', 'address': 4166, 'data_index': BASE_INDEX + 33,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT1_2_trigger',
        'name': 'PT1 H2ガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT2_2', 'left': '356px','top': '440px', 'address': 4170, 'data_index': BASE_INDEX + 35,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT2_2_trigger',
        'name': 'PT2 CH4ガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT3_2', 'left': '356px','top': '440px', 'address': 4174, 'data_index': BASE_INDEX + 37,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT3_2_trigger',
        'name': 'PT3 O2ガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT4_2', 'left': '356px','top': '440px', 'address': 4178, 'data_index': BASE_INDEX + 39,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT4_2_trigger',
        'name': 'PT4 Arガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT5_2', 'left': '356px','top': '440px', 'address': 4182, 'data_index': BASE_INDEX + 41,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT5_2_trigger',
        'name': 'PT5 N2ガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT6_2', 'left': '356px','top': '440px', 'address': 4186, 'data_index': BASE_INDEX + 43,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT6_2_trigger',
        'name': 'PT6 H2ガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
    {'id': 'set1_PT7_2', 'left': '356px','top': '440px', 'address': 4190, 'data_index': BASE_INDEX + 45,
        'format': FormatSpecifier.F3_1, 'trigger_id': 'set1_PT7_2_trigger',
        'name': 'PT7 Arガスレギュレーター 上限', 'min_value': 0.0, 'max_value': 500.0},
]

BASE_LABEL_LEFT = 36
BASE_TOP = 40
ROW_COUNT = 18
# ラベルの座標の再割り当て
for i, item in enumerate(label_text_data):
    x_index =  i // ROW_COUNT
    y_index = i % ROW_COUNT
    item['left'] = f'{BASE_LABEL_LEFT + x_index*664}px'
    item['top'] = f'{BASE_TOP + y_index*72}px'

BASE_UNIT_LEFT = 216
for i, item in enumerate(unit_text_data):
    x_index =  i // ROW_COUNT
    y_index = i % ROW_COUNT
    item['left'] = f'{BASE_UNIT_LEFT + x_index*664}px'
    item['top'] = f'{BASE_TOP + y_index*72}px'

BASE_UPPER_LEFT = 376
for i, item in enumerate(setting_upper_data):
    x_index =  i // ROW_COUNT
    y_index = i % ROW_COUNT
    item['left'] = f'{BASE_UPPER_LEFT + x_index*664}px'
    item['top'] = f'{BASE_TOP + y_index*72}px'

BASE_LOW_LEFT = 508
for i, item in enumerate(setting_low_data):
    x_index =  i // ROW_COUNT
    y_index = i % ROW_COUNT
    item['left'] = f'{BASE_LOW_LEFT + x_index*664}px'
    item['top'] = f'{BASE_TOP + y_index*72}px'

# N/Aを除いたリストで結合する
setting_low_data_filtered = [data for data in setting_low_data if data.get('id') != 'N/A']
setting_data = setting_upper_data + setting_low_data_filtered

def create_setting1_layout():
    layout = []
    text_data = label_text_data + unit_text_data

    # 1. テキスト (z-index: 5)
    for data in text_data:
        # # 'left'と'top'の値からpxを除去し、オフセットを適用
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
            'color': 'black',
            'fontFamily': 'Meiryo UI',
            'zIndex': 5,
        }
        layout.append(html.P(children=children, style=style))

    # 2. テキスト (z-index: 5)
    for data in limit_text_data:
        # # 'left'と'top'の値からpxを除去し、オフセットを適用
        left_val = int(data['left'].replace('px', ''))
        top_val = int(data['top'].replace('px', '')) - 12
        children = data['text']
        
        style={
            'position': 'absolute',
            'left': f'{left_val}px',
            'top': f'{top_val}px',
            'width': f'128px',
            'textAlign': 'center',
            'fontSize': '20px',
            'color': 'black',
            'fontFamily': 'Meiryo UI',
            'zIndex': 5,
        }
        layout.append(html.P(children=children, style=style))

    # 5. ダミーコンポーネント (テキストボックスのOutコールバック用)
    layout.append(
        html.Div(id='dummy-button-set1', style={'display': 'none'})
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
    create_setting_modal(layout, '-set1')

    return layout