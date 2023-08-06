from pygame.sprite import Sprite
import pygame


class Alien(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.speed = game.setting.alien_speed
        self.direction = game.setting.fleet_direction
        self.image = pygame.image.load('../images/alien.bmp')
        self.rect = self.image.get_rect()

        # 定位初始位置 x, y 为左上角顶点
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    '''
    由于绘制调用的是self.aliens.draw(self.screen)
    源码内可见，是抓取Alien类的指定的成员属性：image， rect
    绘制操作也是调用surface.blit(self.image, self.rect)
    所以属性名称必须固定！或者使用魔法函数拦截
    当然尽量不建议这么玩
    '''
    # self.rect_1 = self.image.get_rect()
    # def __getattribute__(self, item):
    #     print(f"__getattribute__ item = {item}")
    #     if item == 'rect':
    #         return self.__dict__.get('rect_1')
    #     else:
    #         return super().__getattribute__(item)

    def update(self):
        self.x += self.speed * self.direction
        self.rect.x = self.x

    def check_edges(self):
        """
        检查是否到达边缘
        :return: True 到达
        """
        return self.rect.left <= 0 or self.rect.right >= self.screen_rect.right


















