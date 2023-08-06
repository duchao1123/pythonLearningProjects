"""
射击相关
"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # 继承Sprite, 作用：编组相同元素，同时操作
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.speed = self.setting.bullet_speed
        self.color = self.setting.bullet_color

        # 创建子弹矩形
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        # 初始子弹位置：飞船顶部居中
        self.rect.midtop = game.ship.rect.midtop
        # 记录子弹初始y
        self.y = float(self.rect.y)

    def update(self):
        # 更新子弹位置
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # 绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
        '''
        rect(surface, color, rect) -> Rect
        '''



