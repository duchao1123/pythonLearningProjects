"""
====================   常规数学函数   ====================
"""
'''
min()
max()
abs() 绝对值
divmod() 获取商和余数的元组
sum() 求和
round() 四舍五入
pow() 幂次计算
'''

# min()
print(min(1, 2))  # 至少2个数比较
print(min(1, 2, 3, 4, 5))  # 不限参数数量
print(min([1, 2, 3, 4]))  # 参数可以为list列表
print(min((1, 2, 3, 4)))  # 参数可以为tuple元组
print(min({1, 2, 3, 4}))  # 参数可以为set元组
print(min({10: 'a', 2: 's'}))  # 参数可以为dict, 根据ascii比较key
print(min({'a': 'a', 'b': 'b'}))  # 参数可以为dict, 根据ascii比较key
# print(min({'a': 'a'}, {"b": "b"}))  # TypeError: '<' not supported between instances of 'dict' and 'dict'

# max() 同上
# abs() 只能传参一个值
a = 1
b = -1
print(f'a = {a}, b = {b}, abs b = {abs(b)}')
# print(f'abs list = {abs([-1, -2, -3])}')  # TypeError: bad operand type for abs(): 'list'
# print(f'{abs(-1, -2)}')  # TypeError: abs() takes exactly one argument (2 given)

# divmod() 获取商和余数的元组
result = divmod(8, 3)
print(type(result))  # <oopclass 'tuple'>
print(result)  # (2, 2)

# sum()略， 类似min，可以传多种数据类型

# round() 四舍五入;
# 不设置小数点后取舍，默认取整
print(f'approximation = {round(3.1)}')  # 3
print(f'approximation = {round(3.8)}')  # 4
# 设置小数点后取舍，按下一位四舍五入
print(f'approximation = {round(3.1415, 3)}')  # 3.142
print(f'approximation = {round(3.1415, 2)}')  # 3.14

# pow() 幂次计算
int_v = 2

# 2 * n[次幂]
print(pow(2, 0))  # 1
print(pow(2, 1))  # 2
print(pow(2, 2))  # 4
print(pow(2, 3))  # 8

# 2 * n[次幂] % x 计算完幂运算后 取余第三个数
print(pow(2, 2, 2))  # 0
print(pow(2, 2, 3))  # 1
# 最多只能3个参数
# print(pow(2, 3, 3, 2))  # TypeError: pow() takes at most 3 arguments (4 given)

'''
===========================  未完待续符 \  ===============
'''

if True \
    or False \
    or True \
    or True:
    print('xxx')


'''
any() 内部列表元素全部为False返回False, 有一个True, 就返回True， 类似or
'''

print(any([False, False, False]))
print(False or False or False)

print(any([True, False, False]))
print(True or False or False)

'''
help()函数可以帮助查看函数或模块的详细说明。
'''
help(print)
'''
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''

'''
range(start, stop, step) 范围
[) 包左不包右，start起始值默认0，stop结束值，但是不包含值，step步长默认1
'''
range_v = range(2)
print(range_v)  # range(0, 2)
print(type(range_v))  # <oopclass 'range'>

range_v = range(2, 5)
print(range_v)  # range(2, 5)
list_v = list(range_v)
print(list_v)  # [2, 3, 4] 不包含右

print(f'{list(range(1, 12, 2))}')  # [1, 3, 5, 7, 9, 11]

'''
reversed()函数返回一个新的反转的迭代器，要转换的序列，
可以是元祖、字符串、列表或者range。
list_v.reverse() 反转源列表
'''
list_v = [1, 2, 3, 4, 5]
rev_list = reversed(list_v)
print(type(rev_list))  # <oopclass 'list_reverseiterator'>
print(list(rev_list))  # [5, 4, 3, 2, 1]

string_v = 'abcdef'
rev_str = reversed(string_v)
print(type(rev_str))  # <oopclass 'reversed'>
print(str(rev_str))  # <reversed object at 0x7fa3c00d7190>
print(list(rev_str))  # ['f', 'e', 'd', 'c', 'b', 'a']
# 惊呆了，字符串反转，还得用list?


tuple_v = (1, 2, 3)
print(tuple(reversed(tuple_v)))  # (3, 2, 1)

range_v = range(0, 10, 2)
print(list(range_v))  # [0, 2, 4, 6, 8]
print(list(reversed(range_v)))  # [8, 6, 4, 2, 0]

'''
sorted()函数对所有可迭代的对象进行排序操作。
sort()是应用在列表list上的方法，而sorted可以对所有可迭代的对象进行排序操作。
列表list的sort()方法返回的是对已经存在的列表进行操作，
而内置函数sorted()返回的是一个新的list，而不是在原来的基础上进行的操作。
'''
list_v = [1, 3, 6, 2, 4, 5]
# print(list_v.sort())  # None; 没有返回值，在源数据上排序
print(list_v)  # [1, 2, 3, 4, 5, 6]

sorted_v = sorted(list_v)
print(sorted_v)  # [1, 2, 3, 4, 5, 6]

print(id(list_v))  # 140234843337536
print(id(sorted_v))  # 140234843273408
# 非同数据，sorted创建了新的

