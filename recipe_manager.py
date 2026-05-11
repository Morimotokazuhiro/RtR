import csv, os
from typing import List, Dict, Any

from config_manager import config_handler

# クラスの外にユーティリティ関数として定義 (または Recipe_Manager クラスのstatic/privateメソッドとして)
def generate_recipe_display_values(
    csv_recipe_data: List[Dict[str, Any]], 
    step_data: List[List[Dict[str, str]]], 
    setting_data: List[Dict[str, Any]]
) -> List[str]:
    """
    レシピデータと設定データに基づいて、画面に表示する値のリストを生成する。
    
    Args:
        csv_recipe_data: recipe_handler.get_recipe_data() が返すデータ
        step_data: recipe_edit_layout.py の step_data (表示コンポーネント構造)
        setting_data: recipe_edit_layout.py の setting_data (フォーマット情報など)
        
    Returns:
        すべてのステップの表示値（文字列）を平坦化したリスト
    """
    display_values_list = []

    for k in range(len(step_data)):
        item_list = step_data[k] # k番目のステップの設定項目リスト
        
        recipe_step_data = []
        if csv_recipe_data and k < len(csv_recipe_data):
            recipe_step_data = csv_recipe_data[k] # 該当ステップの辞書データ

        for i, data in enumerate(item_list):
            # item_setting は、step_data の i番目の項目に対応する setting_data の項目
            item_setting = setting_data[i] 
            
            display_value = "N/A"
            if recipe_step_data:
                # 1. 辞書の値（value）のみをリストとして取得する
                recipe_values = list(recipe_step_data.values())
                
                if i < len(recipe_values):
                    value_raw = recipe_values[i]
                    # format指定がない場合は、文字列として扱う
                    str_format = item_setting.get('format', 's') 
                    
                    try:
                        # 's' 以外で、数値として扱えるならフォーマットを適用
                        if str_format != 's':
                            value_to_format = float(value_raw)
                            display_value = f'{value_to_format:{str_format}}'
                        else:
                            display_value = str(value_raw)
                            
                    except (ValueError, TypeError):
                        display_value = str(value_raw) # 変換エラー時はそのまま表示
                else:
                    display_value = "N/A (値不足)"
            
            display_values_list.append(display_value)

    return display_values_list

class Recipe_Manager:
    EDIT_STEP_LENGTH = 6
    FILE_PATH_EXAMPLE = 'assets\\setting\\recipe_format.csv'
    FILE_PATH_RECIPE = 'assets\\recipe\\'
    
    def __init__(self):
        """インスタンスの初期化"""
        
        """ ファイルの構造
        # レシピ名
        項目,ステップ番号1,ステップ番号2,ステップ番号3
        項目1,1.0,11.0,21.0
        項目2,2.0,12.0,22.0
        項目3,3.0,13.0,23.0
        """
        self.recipe_data = []
        """ レシピデータの構造
        RECIPE_DATA = [
            # レシピ1
            {'name': 'レシピ1',
            'data': [
                {'項目1': 1.0, '項目2': 2.0, '項目3': 3.0},       # ステップ1 (インデックス 0)
                {'項目1': 11.0, '項目2': 12.0, '項目3': 13.0},      # ステップ2 (インデックス 1)
                {'項目1': 21.0, '項目2': 22.0, '項目3': 23.0},      # ステップ3 (インデックス 2)
                {'項目1': 31.0, '項目2': 32.0, '項目3': 33.0},      # ステップ4 (インデックス 3)
                {'項目1': 41.0, '項目2': 42.0, '項目3': 43.0},      # ステップ5 (インデックス 4)
                {'項目1': 51.0, '項目2': 52.0, '項目3': 53.0},      # ステップ6 (インデックス 5)
            ]},
            # レシピ2
            {'name': 'レシピ2',
            'data': [
                {'項目1': 101.0, '項目2': 102.0, '項目3': 103.0},
                {'項目1': 111.0, '項目2': 112.0, '項目3': 113.0},
                {'項目1': 121.0, '項目2': 122.0, '項目3': 123.0},
                {'項目1': 131.0, '項目2': 132.0, '項目3': 133.0},
                {'項目1': 141.0, '項目2': 142.0, '項目3': 143.0},
                {'項目1': 151.0, '項目2': 152.0, '項目3': 153.0},
            ]},
        ]
        """

        # iniファイルの内容の取得
        self.setting = config_handler.get_recipe_setting()
        self.setting_list = config_handler.get_recipe_setting_list()
        # レシピファイル
        self.file_path = ""

        try:
            # 正常の場合は、レシピ番号1から
            recipe_num = self.setting['recipenum']
            recipe_max = self.setting['recipemax'] + 1
        except:
            # iniファイの内容に誤り
            print('Recipe_Manager: 設定ファイルの内容に誤りがあります')
            recipe_num = 0
            recipe_max = 1

        self.edit_recipe_num = recipe_num   # レシピ編集画面で編集するレシピの番号
        self.edit_step_offset = 0           # レシピ編集画面で編集するステップのオフセット

        self.checked = False            # 照合済み
        self.mismatch = False           # 照合不一致

        # 各ファイルの内容を取得する
        
        for i in range(recipe_max):
            # 0番目のレシピはデバッグ用です。
            _file_path = ""
            name = ""
            DEFAULT_NAME = 'デフォルトレシピ'

            if i == 0:
                _file_path = self.FILE_PATH_EXAMPLE
                name = DEFAULT_NAME
            else:
                try:
                    index = i - 1
                    name = self.setting_list[index]['name']
                    _file_path = self.FILE_PATH_RECIPE + self.setting_list[index]['file']
                except:
                    # iniファイの内容に誤り
                    print('Recipe_Manager: 設定ファイルの内容に誤りがあります')
                    recipe_num = 0
                    recipe_max = 1
                    break

            if os.path.exists(_file_path):
                self.file_path = _file_path
                # 3行目からデータが始まり、1列目が項目名（ヘッダー）の場合
                _, datas = self.read_and_transpose_csv_to_dict(
                    file_path=_file_path, 
                    skip_rows=2       # 1行目と2行目をスキップ
                )
            
                recipe = {'name': name, 'data': datas}
                self.recipe_data.append(recipe)
            else:
                print("recipe_Manager: レシピファイルが見つかりません。デフォルト値で初期化します。")
                # ファイルが見つからない場合も、空のデータを持つレシピを初期化に追加
                self.recipe_data.append({'name': 'デフォルトレシピ名', 'data': []})

        print("recipe_Manager: 初期化完了。")

    def read_and_transpose_csv_to_dict(
        self,
        file_path: str, 
        encoding: str = 'Shift-JIS', 
        skip_rows: int = 2
    ) -> List[Dict[str, Any]]: # 関数の型ヒントを (name, datas) のタプルに変更
        """
        CSVファイルを読み込み、指定行数スキップした後、データ領域を行列入れ替え(転置)し、
        辞書のリストとして返す。

        Args:
# ... (省略)
        Returns:
            Tuple[str, List[Dict[str, Any]]]: レシピ名と、転置後のヘッダーをキーとする辞書のリスト。
        """
        
        # 全データを格納するリスト
        original_data = []
        name = ''

        try:
            # ファイルを開き、スキップ処理と全データ読み込みを行う
            with open(file_path, 'r', encoding=encoding, newline='') as f:
                reader = csv.reader(f)
                
                # 1. 指定された行数をスキップ
                # for i, data in enumerate(skip_rows): # 変更前: skip_rows は int なので反復できない
                for i in range(skip_rows):
                    data = next(reader, None)
                    if data is None:
                         # スキップ中にファイルの終端に達した場合
                        return name, []
                    if i == 0:
                        name = data[0]

                # 2. 残りの全データを読み込み
                original_data = list(reader)

                # 空行（要素がゼロまたはすべて空文字列の行）を除去する
                # 要素数がゼロのリスト、またはすべての要素が空文字列''のリストを除外する
                filtered_data = []
                for row in original_data:
                    # strip()して空文字列かどうかをチェックし、1つでも非空要素があれば残す
                    if any(cell.strip() for cell in row):
                        filtered_data.append(row)
                
                original_data = filtered_data


        except FileNotFoundError:
            print(f"recipe_Manager: [エラー] ファイルが見つかりません - {file_path}")
            # return [] # 変更前: 戻り値の型と合わない
            return '', []
        except UnicodeDecodeError:
            print(f"recipe_Manager: [エラー] エンコーディング '{encoding}' でファイルをデコードできませんでした。エンコーディングを確認してください。")
            # return [] # 変更前: 戻り値の型と合わない
            return name, []
            
        if not original_data:
            # スキップ後、データが残っていない場合
            # return [] # 変更前: 戻り値の型と合わない
            return name, []

        # 3. 行列の入れ替え（転置）
        # zip(*list_of_lists) を使う
        transposed_data = list(zip(*original_data))

        # 4. ヘッダーとデータに分離
        # 転置後のデータの1行目（インデックス0）がヘッダー
        headers = [str(h) for h in transposed_data[0]] # 文字列として処理
        # 2行目以降がデータ本体
        data_rows = transposed_data[1:]

        # 5. 辞書のリストに変換
        dict_list = []
        for row in data_rows:
            # ヘッダーとデータ行の要素を zip でペアにして dict() で辞書に変換
            record = dict(zip(headers, row))
            dict_list.append(record)

        _name = name if name else 'デフォルトレシピ名'
        _datas = dict_list if dict_list is not None else []
            
        return _name, _datas
    
    def save_current_recipe_to_file(self, file_path: str):
        """
        現在編集中のレシピデータを、指定されたファイルパスにCSV形式で保存する。

        Args:
            file_path: 保存先のファイルパス。
        """
        try:
            current_recipe = self.recipe_data[self.edit_recipe_num]
            recipe_name = current_recipe['name']
            data_list = current_recipe['data'] # 辞書のリスト [ {項目1: 値, 項目2: 値, ...}, ... ]

            if not data_list:
                print("recipe_Manager: 保存するデータがありません。")
                return

            # 項目名（ヘッダー）のリストを取得
            # data_list の最初の辞書のキーを項目名とする
            fieldnames = list(data_list[0].keys())
            
            # ステップ番号のリストを生成
            step_numbers = [str(i + 1) for i in range(len(data_list))]
            
            # データ領域を作成（行がステップ、列が項目）
            # データリストを転置した構造を作る
            data_matrix = []
            for item_name in fieldnames:
                row = [item_name]
                for step_data in data_list:
                    # 値を文字列に変換して追加
                    value = step_data.get(item_name, '')
                    row.append(str(value))
                data_matrix.append(row)

            # ファイルへの書き込み
            with open(file_path, 'w', encoding='Shift-JIS', newline='') as f:
                writer = csv.writer(f)
                
                # 1行目: レシピ名
                writer.writerow([recipe_name] + [''] * (len(step_numbers)))
                
                # 2行目: ステップ番号ヘッダー
                writer.writerow(['ステップ番号'] + step_numbers)
                
                # 3行目以降: 項目名と値のデータ
                writer.writerows(data_matrix)
                
            print(f"recipe_Manager: レシピ '{recipe_name}' をファイル '{file_path}' に保存しました。")

        except IndexError:
            print("recipe_Manager: [エラー] 編集中のレシピ番号が無効です。")
        except Exception as e:
            print(f"recipe_Manager: [エラー] ファイル保存中にエラーが発生しました: {e}")
    
    # 公開メソッド
    def get_recipe_data(self):
        # レシピの'data'リストを取得
        data_list = self.recipe_data[self.edit_recipe_num]['data']
        end_point = self.edit_step_offset + self.EDIT_STEP_LENGTH

        if data_list:
            if len(data_list) >= end_point:
                return data_list[self.edit_step_offset:end_point]
            elif len(data_list) > self.edit_step_offset:
                return data_list[self.edit_step_offset:len(data_list)]
        
        return []
    
    def get_recipe_name(self) -> str:
        """現在編集中のレシピ名を取得する"""
        try:
            return self.recipe_data[self.edit_recipe_num]['name']
        except IndexError:
            return 'エラー: レシピ名取得失敗' # 失敗時のフォールバック
    
    def update_edit_step_offset(self, offset:int = 0):
        self.edit_step_offset = offset

    def write_recipe_device(self, step, item_id, value):
        # データを受け取り、指定のステップ番号/項目番号の値を更新する
        data_list = self.recipe_data[self.edit_recipe_num]['data']

        # 1. キーのリストを取得する
        keys = list(data_list[step].keys())

        # 2. N番目のキーを特定する
        if 0 <= item_id < len(keys):
            target_key = keys[item_id]
            
            # 3. 値を書き換える
            data_list[step][target_key] = value

            print(f"step: {step}, name: {target_key} の値を {value} に書き換えました ")
        else:
            print("指定されたN番目の要素は存在しません。")

    def get_recipe_setting(self):
        # ini設定ファイルの内容を返す
        return self.setting, self.setting_list
    
    def get_recipe_file(self):
        return self.file_path
    
    def checked_reset(self):
        # 照合判定のリセット
        self.checked = False

    def check_recipe_data(self):

        return

# --- シングルトンインスタンスの作成 ---   
recipe_handler = Recipe_Manager()