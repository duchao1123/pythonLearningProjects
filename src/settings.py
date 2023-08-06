class Settings:
    """
    存储所有设置
    """
    def __init__(self):
        '''
        固定属性
        '''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 飞船生命值
        self.ship_limit = 3
        # 子弹限量
        self.bullet_max_size = 10
        # 当接触到边缘时，立刻下降幅度
        self.alien_drop_speed = 10
        # 每个外星人积分
        self.alien_points = 50
        # 游戏难度提高系数
        self.speedup_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 2
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        # 外形舰队水平移动方向 1：向左 -1：向右；由于水平移动就是 x += speed 或 x -= speed，所以矢量1时最简单的选择
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """
        提高游戏难度
        """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.speedup_scale)


