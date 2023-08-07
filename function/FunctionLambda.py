"""
====================   lambda表达式   ====================
lambda arg0, arg1, arg2 : 表达式
"""
# 随便写一个
lambda_str = lambda x: x + 1

# 随便用一下
print(lambda_str(5))  # 6

# 有啥作用呢？
# 比如利用推导式创建一个list


def cale(x):
    return x * 3 % 2 + 100


list_value = [cale(value) for value in range(10)]
print(list_value)

# 改为lambda

list_value = [(lambda x: x * 3 % 2 + 100)(value) for value in range(10)]
print(list_value)

# 看起来没多大优势?
import random
lambda_list = [
    lambda x: x * 3 % 2 + 100,
    lambda x: x * 4 % 3 + 100,
    lambda x: x * 5 % 4 + 100,
    lambda x: x * 6 % 5 + 100
]
list_value = [(lambda_list[random.randint(0, 3)])(value) for value in range(10)]
print(list_value)
# def就不可以保存到list，用来操作了
