"""
================== 递归 ==================
1、函数自己调用自己
2、必须要有结束条件
3、每次递归要不断向结束靠近
"""

'''
斐波那契数列
'''


def fibgen():
    """
    生成器方式
    """
    k0, k1 = 0, 1
    while True:
        yield k0
        k0, k1 = k1, k0 + k1


def fibitor(*, limit):
    """
    迭代器方式
    """
    k0, k1 = 1, 1
    kn = 0
    while limit > 2:  # > 2 因为 1，2 = 1
        kn = k0 + k1  # 本次结果
        k0 = k1
        k1 = kn
        limit -= 1
    return kn


def fibrecur(n):
    """
    递归方式
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibrecur(n - 1) + fibrecur(n - 2)


# # 生成器每次调用生成一个
# gen = fibgen()
# for i in range(13):
#     print(next(gen))
#
# # 迭代器
# print(fibitor(limit=12))
#
# # 递归
# print(fibrecur(12))

'''
效率对比
'''
import time


def time_checker(tag):
    def function_holder(func):
        def function_caller():
            start_time = time.time()
            func()
            end_time = time.time()
            print(f'{tag} 耗时 {(end_time - start_time):.5f}s')

        return function_caller

    return function_holder


# 生成器每次调用生成一个
@time_checker(tag='fibgenex')
def print_fibgen():
    genex = fibgen()
    result = 0
    for i in range(limit + 1):
        result = next(genex)
    print(result)


# 迭代器
@time_checker(tag='fibitorr')
def print_fibitor():
    print(fibitor(limit=limit))


# 递归
@time_checker(tag='fibrecur')
def print_fibrecur():
    print(fibrecur(limit))


limit = 12
print_fibgen()
print_fibitor()
print_fibrecur()

'''
结果对比：
limit = 12：相差不大
fibgenex 耗时 0.00002s
fibitorr 耗时 0.00001s
fibrecur 耗时 0.00005s

limit = 36: 生成器和迭代器依旧高效，递归已经很耗时了
fibgenex 耗时 0.00002s
fibitorr 耗时 0.00001s
fibrecur 耗时 3.62986s

limit = 48: 生成器和迭代器依旧高效，递归已经不能正常返回了
fibgenex 耗时 0.00003s
fibitorr 耗时 0.00001s
fibrecur 耗时 timeout

结论：递归的效率差
'''


"""
================== 递归实现汉诺塔游戏 ==================
x, y, z三个柱子， 总共n个数量个盘子
想要把n个盘子从x -> z
要求必须小盘子放到大盘子上
思路：
1、从x移动到z，需要把最大的盘子移动到z，需要把n-1个盘子移动到y
2、最大盘子移动到z后，需要把n-1个盘子移动到z，转换目标为将n-1个盘子从y移动到z
3、从y移动到z，需要把当前最大的盘子移动到y，需要把n-2个盘子移动到x
4、把当前最大的盘子移动到z后，需要把n-2个盘子移动到z，转换目标为将n-2个盘子从x移动z
....
规律为：
n个盘子，移动n-1个盘子到非目标柱子，将最大盘子移动到目标柱子，n--，递归
"""


def hanno(n, current, other, target):
    """
    :param n: 当前要移动的盘子数量
    :param current: 当前柱
    :param other: 另一个柱
    :param target: 目标柱
    """
    '''
    为代码
    if 是最大的盘子：
        将最大盘子移动到z
    else:
        将剩余盘子 - 1移动到非目标柱子，(一共3个柱子，z为目标，当前自己处于x或y，移动到另一个)
        将当前最大盘子移动到z
        将剩余盘子 - 1移动到非目标柱子，(一共3个柱子，z为目标，当前自己处于x或y，移动到另一个)
    '''
    if n == 1:  # 判断是最大盘子，共有n个盘子，从小到大，倒序排放，n = 1时，为最大
        print(f"{current} -> {target}")
    else:
        hanno(n - 1, current, target, other)  # 从当前的盘子移动到另一个非目标盘子
        print(f"{current} -> {target}")  # 将当前最大盘子移动到z
        hanno(n - 1, other, current, target)  # 移动其余盘子到z


hanno(1, 'a', 'b', 'c')  # a -> c
print("===============================")
hanno(2, 'a', 'b', 'c')
print("===============================")
'''
a -> b
a -> c
b -> c
'''
hanno(3, 'a', 'b', 'c')
print("===============================")
'''
a -> c
a -> b
c -> b
a -> c
b -> a
b -> c
a -> c
'''


