from enum import Enum

# 画面名(url、列挙型)
class Page_Name(Enum):

    CURRENT_URL_INIT = ''
    CURRENT_URL_AUTO = '/'
    CURRENT_URL_GRAPH = '/graph'
    CURRENT_URL_MANU_1 = '/manual1'
    CURRENT_URL_MANU_2 = '/manual2'
    CURRENT_URL_MANU_3 = '/manual3'
    CURRENT_URL_MANU_4 = '/manual4'
    CURRENT_URL_MANU_5 = '/manual5'
    CURRENT_URL_SET_1 = '/setting1'
    CURRENT_URL_SET_2 = '/setting2'
    CURRENT_URL_SET_3 = '/setting3'
    CURRENT_URL_RECI_1 = '/recipe1'
    CURRENT_URL_RECI_2 = '/recipe2'
    CURRENT_URL_RECI_3 = '/recipe3'
    CURRENT_URL_RECI_4 = '/recipe4'

class Page_Manager:
    # URL（Enum値）と図番号のマッピングを定義
    _DIAGRAM_MAP = {
        Page_Name.CURRENT_URL_MANU_1: 1,
        Page_Name.CURRENT_URL_MANU_2: 1,
        Page_Name.CURRENT_URL_MANU_3: 2,
        Page_Name.CURRENT_URL_MANU_4: 3,
        Page_Name.CURRENT_URL_MANU_5: 3,
    }
    _OPERATION_MAP = {
        Page_Name.CURRENT_URL_MANU_1: 1,
        Page_Name.CURRENT_URL_MANU_2: 2,
        Page_Name.CURRENT_URL_MANU_3: 3,
        Page_Name.CURRENT_URL_MANU_4: 4,
        Page_Name.CURRENT_URL_MANU_5: 5,
    }
    _SETTING_MAP = {
        Page_Name.CURRENT_URL_SET_1: 1,
        Page_Name.CURRENT_URL_SET_2: 2,
        Page_Name.CURRENT_URL_SET_3: 3,
    }

    _RECIPE_MAP = {
        Page_Name.CURRENT_URL_RECI_1: 1,
        Page_Name.CURRENT_URL_RECI_2: 2,
        Page_Name.CURRENT_URL_RECI_3: 3,
        Page_Name.CURRENT_URL_RECI_4: 4,
    }

    def __init__(self):
        # dashに送るurl
        self._url = Page_Name.CURRENT_URL_INIT    
    
    # URLを返す
    @property
    def url_str(self):
        return self._url.value
    
    @property
    def url(self):
        return self._url

    # 手動画面で模式図を表示するか？
    def is_manual_diagram(self, num):
        # 該当しない場合は0 (コールバックを発生させない)
        _num = self._DIAGRAM_MAP.get(self._url, 0)
        return _num == num
    
    # 手動画面で操作画面を表示するか？
    def is_manual_operation(self, num):
        # 該当しない場合は0 (コールバックを発生させない)
        _num = self._OPERATION_MAP.get(self._url, 0)
        return _num == num
    
    # 自動画面か？
    def is_auto_mode(self):
        return self._url == Page_Name.CURRENT_URL_AUTO
    
    # グラフ画面か？
    def is_graph_mode(self):
        return self._url == Page_Name.CURRENT_URL_GRAPH
    
    # 手動画面か？
    def is_manual_mode(self):
        # 該当しない場合は0 (コールバックを発生させない)
        _num = self._OPERATION_MAP.get(self._url, 0)
        return _num != 0
    
    # 設定画面のうち、どれかか？
    def is_setting_current(self, num):
        # 該当しない場合は0 (コールバックを発生させない)
        _num = self._SETTING_MAP.get(self._url, 0)
        return _num == num
    
    # レシピ画面のうち、どれかか？
    def is_recipe_current(self, num):
        # 該当しない場合は0 (コールバックを発生させない)
        _num = self._RECIPE_MAP.get(self._url, 0)
        return num == num
    
    # レシピ画面か？
    def is_recipe_mode(self):
        # 該当しない場合は0 (コールバックを発生させない)
        _num = self._RECIPE_MAP.get(self._url, 0)
        return _num != 0

    # URLの更新
    def Update_Page(self, url):
        self._url = url

# --- シングルトンインスタンスの作成 ---   
page_handler = Page_Manager()