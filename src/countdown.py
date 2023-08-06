import pygame


class Countdown:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.width = 300
        self.height = 150

        self.font = pygame.font.SysFont(None, 80, bold=True)
        self.font_color = (255, 255, 255)

        self.bg_color = (255, 30, 30)
        self.bg_rect = pygame.rect.Rect(0, 0, self.width, self.height)
        self.bg_rect.center = self.screen_rect.center

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.font_color, self.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.bg_rect.center

    def show_countdown(self, msg):
        self._prep_msg(msg)
        self.screen.fill(self.bg_color, self.bg_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)





