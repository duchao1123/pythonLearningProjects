import pygame.font
from src.ship import Ship


class Scoreboard:
    
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.setting = game.setting
        self.stats = game.stats

        self.level_font_color = self.font_color = (30, 30, 30)
        self.level_font = pygame.font.SysFont(None, 48)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_level_score()
        self.prep_score()

        self.high_font_color = (255, 30, 30)
        self.high_font = pygame.font.SysFont(None, 50)
        self.prep_high_score()

        self.ships = pygame.sprite.Group()
        self.prep_ships()

    def prep_level_score(self):
        level = f'level: {self.stats.level}'
        self.level_image = self.font.render(level, True, self.level_font_color, self.setting.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.top = 20
        self.level_image_rect.right = self.screen_rect.right - 20

    def prep_score(self):
        # 格式化输出分数
        # round( x [, n]  ) 它返回x的小数点指定舍入n位数后的值
        # :, 每三位用'，'隔开
        score = f'{round(self.stats.score, -1):,}'
        self.score_image = self.font.render(score, True, self.font_color, self.setting.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.top = self.level_image_rect.bottom + 20
        self.score_image_rect.right = self.level_image_rect.right

    def show_score(self):
        self.screen.blit(self.level_image, self.level_image_rect)
        self.screen.blit(self.score_image, self.score_image_rect)

    def prep_high_score(self):
        score = f'{round(self.stats.high_score, -1):,}'
        self.high_score_image = self.high_font.render(score, True, self.high_font_color, self.setting.bg_color)
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.midtop = self.screen_rect.midtop
        self.high_score_image_rect.top = 20

    def show_high_score(self):
        self.screen.blit(self.high_score_image, self.high_score_image_rect)

    def prep_ships(self):
        self.ships = pygame.sprite.Group()
        if self.stats.ship_life > 1:
            current_x = 20
            for index in range(self.stats.ship_life - 1):
                ship = Ship(self.game)
                ship.rect.top = 20
                ship.rect.x = current_x
                current_x += ship.rect.width + 20
                self.ships.add(ship)

    def show_ships(self):
        self.ships.draw(self.screen)






