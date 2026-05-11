import configparser

class ConfigManager:
    # 設定ファイル
    FILENAME = 'assets\\setting\\recipe_setting.ini'
    SETTINGS_SECTION = 'Settings'

    """設定の読み書き操作を担うクラス（厳密なシングルトンではない）"""
    def __init__(self, config_file=FILENAME):
        self.recipe_settings = {}   # レシピ設定の辞書
        self.recipe_dicts = []      # 各レシピ設定の辞書

        self.config_file = config_file
        self.parser = configparser.ConfigParser()
        self.load()

    def load(self):
        """INIファイルを読み込む"""
        self.parser.read(self.config_file, encoding='utf-8')

        # 特定のセクションを辞書として取得
        setting_section_name = self.SETTINGS_SECTION
        self.recipe_settings = dict(self.parser.items(setting_section_name))

        recipe_max = int(self.recipe_settings['recipemax'])
        for i in range(recipe_max):
            number = i + 1
            recipr_section_name = f'Recipe{number}'
            self.recipe_dicts.append(dict(self.parser.items(recipr_section_name)))

    def get_recipe_setting(self):
        # 設定ファイルの内容を返す
        """
        [Settings]
        RecipeMAX = 4
        RecipeNum = 1        
        """
        # 値をコピーして、数値として扱いたいものをintに変換
        settings = self.recipe_settings.copy()
        try:
            settings['recipemax'] = int(settings.get('recipemax', 0))
            settings['recipenum'] = int(settings.get('recipenum', 0))
        except (ValueError, TypeError):
            # 変換エラー時の処理
            pass 
        return settings
    
    def get_recipe_setting_list(self):
        # 設定ファイルの内容を返す
        """
        [Recipe1]
        Name = レシピ1
        File = recipe1.csv
        Comment = ※ Comment

        [Recipe2]
        Name = レシピ2
        File = recipe2.csv
        Comment = ※ Comment

        -----------

        [Recipe4]
        Name = レシピ4
        File = recipe4.csv
        Comment = ※ Comment
        """
        return self.recipe_dicts

    # def get_value(self, section, key, default=None):
    #     """設定値を取得する"""
    #     return self.parser.get(section, key, fallback=default)

    # def set_value(self, section, key, value):
    #     """設定値を設定する"""
    #     if section not in self.parser.sections():
    #         self.parser.add_section(section)
    #     self.parser.set(section, key, str(value))
    #     self.save()

    # def save(self):
    #     """設定ファイルを保存する"""
    #     with open(self.config_file, 'w') as f:
    #         self.parser.write(f)

    

# --- シングルトンインスタンスの作成 ---   
config_handler = ConfigManager()