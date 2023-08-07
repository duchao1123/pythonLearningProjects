"""
需求：世界杯案例，世界杯小组赛的比赛规则是我们的球队与其他三支球队进行比赛，然后根据总成绩(积分)确定出线资格。
小组赛球队实力已知(提示用户输入各球队实力），我们通过一个数字表示。
如果我们赢1局得3分，平一局得1分，输一局得0分，最终求球队总成绩。

4支球队 => a/b/c/d
a = 20
b = 30
c = 20
d = 10

a vs b : 40 > 30 a胜利得3分
a vs b : 30 = 30 平局得1分
a av b : 20 < 30 输一局得0分

a vs b  赢  3
a vs c  平  1
a vs d  输  0
最终结果： 3+1+0
"""


def fork_competition(mine_com, rivals):
    total_score = 0
    for com in rivals:
        if mine_com > com:
            total_score += 3
        elif mine_com == com:
            total_score += 1
    return total_score


def start():
    combat_a = int(input("a的战力评估："))
    combat_b = int(input("b的战力评估："))
    combat_c = int(input("c的战力评估："))
    combat_mine = int(input("我的战力评估："))
    total_score = fork_competition(combat_mine, [combat_a, combat_b, combat_c])
    print(f'总分 = {total_score}')


start()




