import pygame


class Button:

    def __init__(self, game, msg):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.font_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48, bold=True)
        self.rect = pygame.rect.Rect(0, 0, self.width, self.height)
        # 位置
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.font_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)







