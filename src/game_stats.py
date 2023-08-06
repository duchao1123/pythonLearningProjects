from pathlib import Path


high_score_data_file = '../data/high_score.txt'


class GameStats:

    def __init__(self, game):
        self.setting = game.setting
        self.reset_stats()
        self.high_score = 0
        self.init_stats()
        self.level = 1

    def reset_stats(self):
        self.ship_life = self.setting.ship_limit
        self.score = 0
        self.level = 1

    def init_stats(self):
        """
        启动时也要有最高纪录
        """
        path = Path(high_score_data_file)
        if path.exists() and path.is_file():
            with open(high_score_data_file, 'r') as f:
                content = f.read()
                if content.isdigit():
                    self.high_score = int(content)

    def exit_stats(self):
        """
        当要退出游戏时，需保存当前最高记录
        """
        with open(high_score_data_file, 'w') as f:
            f.write(str(self.high_score))















