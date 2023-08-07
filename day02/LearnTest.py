"""
游戏角色：player玩家   computer电脑
游戏规则：
石头-0，剪刀-1，布-2
① 玩家赢
player = 0, computer = 1
player = 1, computer = 2
player = 2, computer = 0
② 平局
③ 电脑赢
"""
# ① 导入random模块
import random


dict_value = {0: '石头', 1: '剪刀', 2: '布', -1: '退出'}


def check_winner():
    computer_type = random.randint(0, 2)
    print(f'你出[{dict_value[player_type]}] vs 电脑出[{dict_value[computer_type]}]')
    if ((player_type == 0 and computer_type == 1)
            or (player_type == 1 and computer_type == 2)
            or (player_type == 2 and computer_type == 0)):
        print('你赢!')
    elif player_type == computer_type:
        print('平!')
    else:
        print('电脑赢!')


while True:
    print(dict_value, "  请出拳：")
    player_type = int(input())
    if player_type == -1:
        exit(0)
    else:
        check_winner()
