"""
====================   List进阶使用   ====================
列表推导式： 将for循环和创建新元素合并成一行代码；效率更好！！！直接以c语言运行
切片： 创建一个新列表，指定原列表的开始和结束索引[)，拷贝区间内的元素
切片： data = [1, 2, 3] data[::-1] = [3, 2, 1]反转，字符串是字符数组也可以，实用例子判断是否是，回文字符串
浅拷贝、深拷贝
"""

'''
列表推导式
'''
# 数值列表，其实感觉是提供的创建等差列表api
# range_value = range(1, 10, 3)  # param0: 从几开始，默认0； param1: 到那结束，不包含； param2: 步数
# print(list(range_value))  # [1, 4, 7]
#
# # normal
# range_value = range(2, 5)
# print(range_value)
# list_value = []
# for value in range_value:
#     list_value.append(value)
# print(list_value)  # [2, 3, 4]
#
# # 列表推导式
# range_value_1 = range(1, 6)
# print(range_value_1)
# list_value_1 = [value for value in range_value_1]
# print(list_value_1)  # [1, 2, 3, 4, 5]
#
# # 可以运算后插入
# range_value_2 = range(10)
# list_value_2 = [value * 2 for value in range_value_2]
# print(list_value_2)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#
# # 可以调函数
# range_value_3 = range(10)
#
#
# def cale(cale_value):
#     return cale_value * 2 if cale_value % 2 == 0 else cale_value
#
#
# list_value_3 = [cale(value) for value in range_value_3]
# print(list_value_3)  # [0, 1, 4, 3, 8, 5, 12, 7, 16, 9]
#
# '''
# 切片
# [:] 不设置开始结束索引，默认就是全列表复制
# [a:b] [a, b)包左不包右
# [-a:] 取列表后a位
# [a:b:c]  c步幅！
# [::-c]  -c 反向遍历切片
# '''
# list_value = [1, 2, 3, 4, 5]
# new_list_value = list_value[1:4]
# print(new_list_value)  # [2, 3, 4], [)范围
# print(f'origin list {id(list_value)}, new list {id(new_list_value)}')  # origin list 140252158185856, new list 140252158185536
#
# list_value = [1, 2, 3, 4, 5]
# print(list_value[:])  # [1, 2, 3, 4, 5]， 不设置开始结束索引，默认就是全列表复制
#
# list_value = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 模拟大列表
# print(list_value[-3:])  # [7, 8, 9]， 取大列表后三位

# list_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list_value = list_value[1:10:2]  # [1, 3, 5, 7, 9]
# print(new_list_value)
#
# new_list_value = list_value[::-2]  # [9, 7, 5, 3, 1]
# print(new_list_value)


# 推导式获取二维数组中元素，只是一个例子，举一反三靠自己
list_value = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 打印2， 5， 8
result = [value[1] for value in list_value]  # value 二维数组的元素，一维数组
print(result)
# 打印1，5，9
result_1 = [value[list_value.index(value)] for value in list_value]
print(result_1)
# 随机打印
import random
list_value = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9],
    [10, 11, 12, 13]
]
result_2 = [value[random.randint(0, len(value) - 1)] for value in list_value]
print(result_2)  # [5, 9, 10] ; [5, 8, 10] ; [1, 7, 11] 每次都不一样

# random小偏门知识，random是伪随机数
origin_state = random.getstate()
result_2 = [value[random.randint(0, len(value) - 1)] for value in list_value]
print(result_2)  # [3, 7, 11] ; [4, 9, 10] ; [1, 8, 13]
random.setstate(origin_state)
result_2 = [value[random.randint(0, len(value) - 1)] for value in list_value]
print(result_2)  # [3, 7, 11] ; [4, 9, 10] ; [1, 8, 13]
# 随机数不灵了！

'''
推导式进阶：
[fn(value) for value in list if xxx]
在for后面加判断，用于filter。
执行顺序：
1、for
2、if
3、fn(value)
'''
str_list = ['Abc', 'Def', 'Acd', 'ghd']
a_str_list = [value for value in str_list if value.startswith('A')]
print(a_str_list)  # ['Abc', 'Acd']

str_list = ['Abc', 'Def', 'Acd', 'ghd']
b_str_list = [value.replace('A', 'B') for value in str_list if value.startswith('A')]
print(b_str_list)  # ['Bbc', 'Bcd']
'''
推导式进阶：
[fn(value_b) for value_a in list for value_b in value_a]
for 嵌套， 和展开的for嵌套一样
实际使用如：展开二维数组
'''
list_value = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9]
]
new_list_value = [value_b for value_a in list_value for value_b in value_a]
print(new_list_value)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# eg: 组合数据
char_as = ['a', 'b', 'c']
char_bs = ['d', 'e', 'f']
list_value = [f'{a + b}' for a in char_as for b in char_bs]  # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(list_value)

'''
推导式终极篇
[fn(value_b) for value_a in list if xx
            for value_b in value_a if xx
            ...
            ]
for嵌套 + if条件判断

但是设计原则   =  简洁 + 已读
'''


'''
浅拷贝、深拷贝
对于引用类型数据，浅拷贝只是拷贝了引用，深拷贝才可能复制数据实体
'''
# list_one = [1, 2, 4]
# list_value = [
#     list_one, [4, 5, 6], [7, 8, 9]
# ]
# # 说明：二维数组，内部元素为一元数组，是引用数据类型
# new_list_value = list_value.copy()
#
# print(list_value[0] is new_list_value[0])  # True, 证明是同一个引用
# list_value[0][0] = 'a'
# print(new_list_value[0][0])  # a, 修改同时生效，因为修改是对list_one实体进行，俩个引用获取数据相同
#
# '''
# 深拷贝
# 实现方式 import copy
# deepcopy
# '''
# import copy
# list_two = [1, 2, 3]
# list_value = [
#     list_two, [4, 5, 6], [7, 8, 9]
# ]
# new_list_value = copy.deepcopy(list_value)
#
# list_value[0][0] = 'a'
# print(list_value)  # [['a', 2, 3], [4, 5, 6], [7, 8, 9]]
# print(new_list_value)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# str_one = 'abc'
# str_two = 'abc'
# print(str_one is str_two)  # False， 证明str是引用类型
#
# list_value = [
#     str_one, 'def', 'ghi'
# ]
#
# print(str_one is list_value[0])  # True, 证明持有的确实是str的引用
#
# list_value[0] = 'lll'
# print(str_one)  # 'abc', 为啥没改？
# print(list_value[0])  # lll
#
# str_one = 'eee'
# print(list_value[0])  # lll, 证明str_one与list_value又是脱钩的
# 特殊在str这个数据类型。


'''
判断字符串是否是，回文字符串
'''
str_value = '12321'
str_value_1 = '121asd21'
print(f'{str_value} 是回文字符串' if str_value == str_value[::-1] else f'{str_value} 不是回文字符串')  # 12321 是回文字符串
print(f'{str_value_1} 是回文字符串' if str_value_1 == str_value_1[::-1] else f'{str_value_1} 不是回文字符串')  # 121asd21 不是回文字符串

