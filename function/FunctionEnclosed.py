"""
====================   闭包   ====================
1、嵌套函数，外部函数返回内部函数，可以不通过外部函数调用到内部函数，
2、同时内部函数持有外部函数，外部函数的局部变量不被销毁
3、利用nonlocal关键字，修改外部函数局部变量，做到记录的功能
"""

# 简单定义一个人的位置x,y
# 移动做+运算


def worker(x, y):
    def move(step):
        nonlocal x, y
        x += step
        y += step
        print((x, y))
    return move


move = worker(0, 0)
move(1)
move(2)
move(3)