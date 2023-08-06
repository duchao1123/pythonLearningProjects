from pygame import image
from pygame.sprite import Sprite


class Ship(Sprite):
    """
    管理飞船的类
    """
    def __init__(self, game):
        super().__init__()
        """
        初始化飞船并设置初始位置
        :param game AlienInvasion, 内部包含pygame、screen等引用
        """

        # 设置
        self.settings = game.setting
        # surface
        self.screen = game.screen
        # 屏幕范围矩形
        self.screen_rect = game.screen.get_rect()

        # 加载飞机图片资源
        self.image = image.load('../images/ship.bmp')
        # 飞机范围矩形
        self.rect = self.image.get_rect()

        # 新飞机位置定位为底部居中
        # 可见定位可以通过rect
        self.center_ship()

        # 移动标识
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        if self.rect.x != self.x:
            self.rect.x = self.x

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.rect.y != self.y:
            self.rect.y = self.y

    def blitme(self):
        """
        在指定位置绘制飞船
        """
        self.screen.blit(self.image, self.rect)





