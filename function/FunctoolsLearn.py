"""
====================   高阶函数   ====================
高阶函数： 函数参数是函数对函数
比如前面装饰器
内置高阶函数库 functools
内省：函数的一些自带属性
"""


import functools as tools


def add(x, y):
    return x + y


print(tools.reduce(add, [1, 2, 3]))  # 6
# lambda方式
print(tools.reduce(lambda x, y: x + y, [1, 2, 3]))  # 6
'''
functools.reduce 相当于add(add(1, 2), 3)
'''
# help(tools.reduce)  # 打印方法文档
print(tools.reduce.__doc__)  # 打印内省文档


'''
偏函数
根据不同参数，返回不同结果的函数引用
'''
square = tools.partial(pow, exp=2)  # 求平方
cube = tools.partial(pow, exp=3)  # 求立方
print(square(2))  # 4
print(cube(2))  # 8


'''
@wraps
解决装饰器打印内省名称问题
'''


def checker(func):
    def call_func():
        func()
    return call_func


@checker
def fcc():
    pass


print(fcc.__name__)  # 正常预期为fcc， 但实际结果call_func, 见装饰器
# 解决办法是@wraps


def checker_1(func):
    @tools.wraps(func)
    def call_func():
        func()
    return call_func


@checker_1
def fdd():
    pass


print(fdd.__name__)  # fdd
