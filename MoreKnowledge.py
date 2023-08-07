"""
====================   序列，常用方法   ====================
可变序列： list
不可变序列： str，tuple
"""

'''
序列常用方法
+ 、*
'''

print([1, 2, 3] + [4, 5])  # [1, 2, 3, 4, 5]
print('abc' * 3)  # abcabcabc

"""
====================  python 对象三基本属性   ====================
1、唯一标识： 对象创建就生成了，不会重复； id()函数获取唯一标识
2、类型
3、值

is   同一性判断
is not
in      包含判断
not in
"""

"""
====================  del  用法   ====================
"""
list_value = [1, 2, 3, 4, 5]
list_value[1:4] = []
# 切片 索引 1 ～ 索引 3 = [2, 3, 4]
# = [] 相当于取反 = [1, 2, 3, 4, 5] - [2, 3, 4] = [1, 5]
print(list_value)  # [1, 5]

list_value = [1, 2, 3, 4, 5]
# 删除list_value变量
# del list_value
# print(list_value)  # NameError: name 'list_value' is not defined

# 删除list_value 中某元素
del list_value[0]
print(list_value)  # [2, 3, 4, 5]

# 间隔删除
list_value = [1, 2, 3, 4, 5]
del list_value[::2]  # start:end:step   start与end省略，想到与全list
print(list_value)  # [2, 4]; 解释：step2，隔一个删一个， 从0开始删： 1，3，5

# 删除list内全部元素
list_value = [1, 2, 3, 4, 5]
del list_value[:]
print(list_value)  # []

"""
====================   序列常用方法   ====================
相互转换： 将可叠戴对象转为list、tuple、str
min(s, default)：获取最小, default 默认值
min(x, y, z): 比较元素中最小
max(s, default)：获取最大
max(x, y, z)
len: 求长度， 有最大值限制
sum：求和， 可以设置start、end，限制计算范围
sorted(): 排序，返回新可叠戴对象， 可以设置key，指定比较函数， key=len, 就是比较长度，默认是字母编码逐个比较
reversed(): 反转，返回新的迭代器
"""

empty_list = []
print(min(empty_list, default=-1))  # -1
print(max(3, 6, 1))  # 6

list_value = ['abc', 'dacf', 'ssas', 'we']
sorted_list = sorted(list_value)
print(sorted_list)  # ['abc', 'dacf', 'ssas', 'we']

sorted_list = sorted(list_value, key=len)
print(sorted_list)  # ['we', 'abc', 'dacf', 'ssas']

list_value = ['a', 'b', 'c', 'd']
result = reversed(list_value)
print(type(result))  # <oopclass 'list_reverseiterator'> 返回迭代器ß
print(list(result))

"""
====================   序列，常用方法   ====================
all:  全true，才true
any： 有true，就true

enumerate(x, start_index):  返回索引与元素组成的二元组, 可以设置start_index，设置开始索引
zip: 取相同索引，组合多可叠戴对象，成元组; 如果长度不一致，只能取最短的为标准
如果想要取最大值，使用itertools zip_longest
map(fn, values) 返回values中每个value经过fn计算得到的值的可迭代对象, 类似zip，只能取最短的为标准
filter 过滤器
iter  获取可迭代对象的迭代器
"""

list_value = ['a', 'b', 'c', 'd']
print(list(enumerate(list_value)))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
print(list(enumerate(list_value, 5)))  # [(5, 'a'), (6, 'b'), (7, 'c'), (8, 'd')]

list_value = ['a', 'b', 'c']
list_value_1 = ['1', '2', '3']
result = zip(list_value, list_value_1)
print(list(result))  # [(5, 'a'), (6, 'b'), (7, 'c'), (8, 'd')]

list_value = ['a', 'b', 'c']
list_value_1 = ['1', '2', '3']
list_value_2 = ['-', '=', '-=']
result = zip(list_value, list_value_1, list_value_2)
print(list(result))  # [('a', '1', '-'), ('b', '2', '='), ('c', '3', '-=')]

import itertools as tool

data_a = ['a', 'b']
data_b = ['cc', 'dd', 'ee']
data_c = ['ff', 'gg', 'hh', 'ii']
zipped = tool.zip_longest(data_a, data_b, data_c)
print(list(zipped))  # [('a', 'cc', 'ff'), ('b', 'dd', 'gg'), (None, 'ee', 'hh'), (None, None, 'ii')]

list_value = [1, 2, 3, 4]


def cale(value):
    return value * 3 / 2


mapped = map(cale, list_value)  # 也可以是内置函数
print(list(mapped))  # [1.5, 3.0, 4.5, 6.0]

# 如果fn是多参数，map的参数需要对应
mapped = map(pow, list_value, [2, 2, 2])
print(list(mapped))  # [1, 4, 9]

list_value = ['a', 'B', 'C', 'd']
filtered = filter(str.isupper, list_value)  # 过滤是字符串全是大写的字符串
print(list(filtered))  # ['B', 'C']

"""
====================   概念   ====================
一个迭代器一定是一个可迭代对象
迭代器只能一次操作，迭代对象可以重复操作
next 逐个取迭代取下一元素
"""
mapped = map(len, ['abc', 'aaaa', 'aaaaaaa', 'a'])  # 返回迭代器只能操作一次

for l in mapped:
    print(f'l = {l}')

'''
l = 3
l = 4
l = 7
l = 1
'''

print(list(mapped))  # []

list_value = [1, 2, 3, 4]  # 可迭代对象， 可以重复使用
print(list_value)  # [1, 2, 3, 4]

for i in list_value:
    print(i)
'''
1
2
3
4
'''

list_value = [1, 2, 3]
iter_value = iter(list_value)
print(type(iter_value))

for i in iter_value:
    print(i)

print(list(iter_value))
print(list_value)


list_value = [1, 2, 3]
iter_value = iter(list_value)
index = 0
while next(iter_value, "没有了") != "没有了":
    print(f'index = {index}, value = {list_value[index]}')
    index += 1

'''
index = 0, value = 1
index = 1, value = 2
index = 2, value = 3
'''


