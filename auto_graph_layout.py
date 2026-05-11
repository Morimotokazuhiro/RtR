import plotly.graph_objects as go
import pandas as pd
import datetime

class AutoGraphLayout:
    """
    グラフのデータ蓄積とレイアウトを管理するクラス。
    """
    def __init__(self, max_points=150, title='トレンドグラフ', series_names=['データ']):
        self.max_points = max_points
        self.title=title
        # 複数のデータ系列名を受け取る
        self.series_names = series_names
        # 二重リスト構造。例: [[データポイント_1_1, データポイント_1_2, ...], [データポイント_2_1, データポイント_2_2, ...]]
        self.data_list = [[] for _ in series_names]

    # new_dataは「系列数分のデータポイントのリスト」として受け取る
    def push_data(self, new_data: list):
        """
        新しいデータポイントのリスト（系列ごとの値）をリストに追加します。
        """
        if len(new_data) != len(self.series_names):
             # データの数が系列名と一致しない場合はエラーまたはスキップ
             print(f"警告: データポイントの数 ({len(new_data)}) がシリーズ名 ({len(self.series_names)}) と一致しません。")
             return

        # 各系列にデータを追加
        for i, data_point in enumerate(new_data):
            self.data_list[i].append(data_point)
            
            # リストが最大ポイント数を超えないように調整
            if len(self.data_list[i]) > self.max_points:
                self.data_list[i] = self.data_list[i][-self.max_points:]

    # update_and_create_figureも「リスト」として受け取る
    def update_and_create_figure(self, new_data_points: list):
        """
        新しい単一データポイントのリストをプッシュし、最新のfigureを返します。
        """
        # 単一のデータポイントをプッシュ
        self.push_data(new_data_points)
        
        # 蓄積されたデータでfigureを作成し、返す
        return self.create_figure()


    def create_figure(self):
        """
        蓄積されたデータリストからグラフを作成します。
        """
        # グラフの作成
        fig = go.Figure()
        
        # 💡 修正点 5: 複数の系列をループでトレースに追加
        for i, series_data in enumerate(self.data_list):
             # 時刻軸（ここでは点数）は共通
            timestamps = list(range(len(series_data)))
            
            fig.add_trace(go.Scatter(
                x=timestamps,
                y=series_data,
                mode='lines',
                name=self.series_names[i], # 系列名を凡例に使用
                # 系列ごとに異なる色を設定することも可能
                line=dict(width=2) 
            ))
        
        # 💡 修正: グラフのレイアウトを設定し、X軸の範囲をmax_pointsに固定
        fig.update_layout(
            # タイトルや背景色などの既存設定があればここに維持
            title={
                'text': self.title, # ここでインスタンスのタイトルを設定
                'y':0.95,           # タイトルのY位置（上部）
                'x':0.5,            # タイトルのX位置（中央）
                'xanchor': 'center',
                'yanchor': 'top'
            },
            xaxis=dict(
                # 常に0から (max_points - 1) までの範囲を表示するように固定
                range=[0, self.max_points - 1], 
                showgrid=True,
                zeroline=False,
                title='経過時間 (点数)' # 必要に応じてタイトルを変更
            ),
            yaxis=dict(
                # Y軸の自動スケールを維持するか、固定範囲を設定
                autorange=True, 
                showgrid=True,
                zeroline=False,
                title='値' # 必要に応じてタイトルを変更
            ),
            # グラフの余白を調整
            margin=dict(l=40, r=20, t=60, b=30), # t（上マージン）を増やしてタイトルスペースを確保 
            autosize=True, # 親要素に合わせる
            showlegend=False,
            plot_bgcolor="#CFEFD5"
        )

        return fig
