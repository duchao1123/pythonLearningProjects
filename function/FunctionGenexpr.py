"""
================== 生成器 ==================
1、基础生成器
区别：
关键词yeild
生成器每次只生成一个数据，迭代器内部包含全部数据
2、生成器表达式
区别于推导式
"""

'''
基础生成器
'''


def gen(limit):
    """
    生成器，没有return，依靠关键字yield，标识返回数据，每次返回一个数据
    :param limit:
    :return:
    """
    i = 0
    while i <= limit:
        yield i
        i += 1


generator = gen(5)
print(type(generator))  # <oopclass 'generator'>

for i in generator:
    print(i)
# print(len(generator))  # 所以生成器不包含所有内容，TypeError: object of type 'generator' has no len()


# generator = gen(5)
# while True:
#     print(next(generator))
# StopIteration 不限制next，生成完成后，报错


'''
生成器表达式
'''
# 推导式
list_value = [value for value in range(10)]
generator_value = (value for value in range(10))
print(type(generator_value))

print(next(generator_value))
print(next(generator_value))
print(next(generator_value))
print(next(generator_value))
print("==============================")


"""
================== 习题 ==================
使用生成器实现斐波那且数列
"""


def fib():
    k_0, k_1 = 0, 1
    while True:
        yield k_0
        k_0, k_1 = k_1, k_0 + k_1


fib = fib()
for i in range(20):
    print(next(fib))


# 这比java递归时间复杂度，空间复杂度优化太多了

