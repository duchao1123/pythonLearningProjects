"""
窗口，响应用户输入

"""

import sys
import pygame
from src.settings import Settings
from src.ship import Ship
from src.bullet import Bullet
from src.alien import Alien
from src.game_stats import GameStats
from src.button import Button
from src.scoreboard import Scoreboard
from src.countdown import Countdown
import time


class AlienInvasion:

    def __init__(self):
        """
        初始化游戏并并创建游戏资源
        """
        pygame.init()

        # 游戏活跃状态
        self.game_active = False
        # 创建settings
        self.setting = Settings()
        # 创建状态
        self.stats = GameStats(self)

        # 设置显示参数(width = 1200, height = 800) 单位像素
        # 返回一个surface，类似android surface，用于显示
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        # 设置标题
        pygame.display.set_caption("外星人游戏")
        # 计分牌
        self.score = Scoreboard(self)
        # 创建按钮
        self.button = Button(self, 'play')

        # 创建飞船
        self.ship = Ship(self)
        # 创建子弹组
        self.bullets = pygame.sprite.Group()
        # 创建外星人舰队
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # 创建时钟，用于控制主循环速度，进而控制游戏帧率
        self.clock = pygame.time.Clock()

        # 定义背景颜色三原色， RGB
        self.bg_color = self.setting.bg_color
        self.countdown = Countdown(self)

    def run_game(self):
        """
        开始游戏，进入主️循环
        """
        while True:
            """
            监听事件
            """
            self._check_events()
            '''
            游戏存活继续
            '''
            if self.game_active:
                """
                更新飞船
                """
                self.ship.update()
                '''
                更新子弹
                '''
                self._update_bullet()
                '''
                更新外星人
                '''
                self._update_aliens()
            """
            更新屏幕
            """
            self._update_screen()
            '''
            控制帧率
            '''
            self.clock.tick(60)

    def _ship_hit(self):
        if self.stats.ship_life > 1:
            # 准备倒计时
            for i in '321':
                self.countdown.show_countdown(i)
                pygame.display.flip()
                time.sleep(0.8)

            # 减生命
            self.stats.ship_life -= 1
            # 减少可用生命显示
            self.score.prep_ships()

            # 清空界面成员
            self.bullets.empty()
            self.aliens.empty()

            # 重新创建
            self._create_fleet()
            self.ship.center_ship()
        else:
            self.game_active = False

    def _check_fleet_edges(self):
        for alien in self.aliens:
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens:
            # 下降位置
            alien.rect.y += self.setting.alien_drop_speed
            # 水平移动方向取反
            alien.direction *= -1

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.setting.screen_height:
                self._ship_hit()
                break

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.exit_stats()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYUP:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYDOWN:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_q:
            self.stats.exit_stats()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            '''
            按空格生成子弹， 并添加到group中统一管理
            '''
            if len(self.bullets) < self.setting.bullet_max_size:
                bullet = Bullet(self)
                self.bullets.add(bullet)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _check_play_button(self, mouse_pos):
        # api: 判断点击点是否落于rect内
        clicked_play = self.button.rect.collidepoint(mouse_pos)
        if clicked_play and not self.game_active:
            # 重置关level
            self.score.prep_level_score()
            # 重置得分
            self.score.prep_score()
            # 初始化游戏难度
            self.setting.initialize_dynamic_settings()
            # 隐藏光标
            pygame.mouse.set_visible(False)
            self.stats.reset_stats()
            self.game_active = True
            # 清空界面成员
            self.bullets.empty()
            self.aliens.empty()
            # 重新创建
            self._create_fleet()
            self.ship.center_ship()

    def _check_bullet_alien_collisions(self):
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if collision:
            '''
            此时存在问题是：groupcollide只能判定有外星人被击中，但是同时可能有多个外星人被击中，所以只进行一次加分是不对的
            打印{<Bullet Sprite(in 0 groups)>: [<Alien Sprite(in 0 groups)>, <Alien Sprite(in 0 groups)>, <Alien Sprite(in 0 groups)>]}
            发现返回的collision是一个字典，key是Bullet，values是[Aliens]，所以有一个alien被击中应该积响应分数
            '''
            for aliens_list in collision.values():
                self.stats.score += self.setting.alien_points * len(aliens_list)
            # 更新分数
            self.score.prep_score()
            if self.stats.score > self.stats.high_score:
                self.stats.high_score = self.stats.score
                self.score.prep_high_score()

    def _update_ships(self):
        self.score.prep_ships()

    def _update_bullet(self):
        self.bullets.update()
        # 此处发现，调用的group的update，没有调用每一个实体的update
        # source code:   xxxxx!!!
        # for sprite in self.sprites():
        #     sprite.update(*args, **kwargs)
        for b in self.bullets.sprites().copy():
            if b.rect.bottom <= 0:  # 子弹出了屏幕顶部
                self.bullets.remove(b)

        # api: 当俩个编组内有元素叠加，仍未发生碰撞，也就是击中
        # 并且会消除碰撞元素
        self._check_bullet_alien_collisions()

        # 当外星人删除完，生成新的外星人舰队， 清空屏幕中的所有子弹
        if not self.aliens:
            self.ship.center_ship()
            self._increase_level()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        # api: 判断单个arg0：元素与arg1：编组发生重叠
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检查外星人是否触底
        self._check_aliens_bottom()

    def _update_screen(self):
        """
        渲染背景色
        """
        self.screen.fill(self.bg_color)
        '''
        绘制每一个子弹
        '''
        for b in self.bullets.sprites():  # sprites 返回所有子弹list
            b.draw_bullet()
        '''
        绘制飞船
        '''
        self.ship.blitme()
        '''
        绘制外星舰队
        '''
        self.aliens.draw(self.screen)
        """
        绘制开始按钮
        """
        if not self.game_active:
            # 显示光标
            pygame.mouse.set_visible(True)
            self.button.draw_button()
        '''
        显示计分牌
        '''
        self.score.show_score()
        self.score.show_high_score()
        self.score.show_ships()
        """
        刷新显示
        """
        pygame.display.flip()

    def _create_fleet(self):
        alien = Alien(self)
        # 放置一个，需要的空间
        add_alien_need_width, add_alien_need_height = alien.rect.width * 2, alien.rect.height * 2
        current_x, current_y = add_alien_need_width, add_alien_need_height
        margin_bottom = 100
        while self.setting.screen_height - current_y > add_alien_need_height + margin_bottom:
            while self.setting.screen_width - current_x > add_alien_need_width:
                self._create_alien(current_x, current_y)
                current_x += add_alien_need_width
            current_y += add_alien_need_height
            # 还原x初始位置
            current_x = alien.rect.right

    def _create_alien(self, *args):
        alien = Alien(self)
        # 更新定位
        alien.rect.x, alien.rect.y = args
        # 更新位移参数
        alien.x = alien.rect.x
        self.aliens.add(alien)

    def _increase_level(self):
        self.stats.level += 1
        # 重置关level
        self.score.prep_level_score()
        self.bullets.empty()
        self._create_fleet()
        self.setting.increase_speed()


if __name__ == "__main__":  # 类似main方法，被执行入口

    """
    创建游戏实例并运行
    """
    game = AlienInvasion()
    game.run_game()
