"""
====================   集合常用方法   ====================
set
特性：
唯一性：可以去重list为无重复
无序性：内部元素没有顺序，所以不能使用索引获取，不支持
"""

'''
创建
'''
# 常规
set_value = {'a', 'b'}
# set方法
set_value_1 = set('abc')
# 推导式
set_value_2 = {value for value in range(10)}
# 无序性
print(set_value)  # {'b', 'a'}
print(set_value_1)  # {'b', 'c', 'a'}
print(set_value_2)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

'''
唯一性
'''
list_value = [1, 1, 2, 2, 3, 3, 4]
set_value = set(list_value)
print(set_value)  # {1, 2, 3, 4}

# 判断list是否有重复元素
list_value = [1, 1, 2, 2, 3, 3, 4]
print(len(list_value) == len(set(list_value)))  # F

'''
判断包含关系
in
not in
'''
set_value = {'a', 'b', 'c'}
print('a' in set_value)  # T
print('d' not in set_value)  # T


"""
====================   常用方法   ====================
a.isdisjoint(b)  判断a与b无交集
a.issubset(b)  判断a是b的子集    可以使用运算符代替  a <= b
a.issuperset(b) 判断a是b的父集                    a >= b
a.union(b) 获取a与b的并集                         a | b
a.intersection(b) 获取a与b的交集                  a & b
a.difference(b) 获取a对于b的差集，只存在于a中，不存在与b中  a - b
a.symmetric_difference(b)  获取对称差集（a中存在，但是b中不存在的元素 + b中存在，但a中不存在的元素） a ^ b
"""
set_value = {'a', 'b', 'c'}
set_value_1 = {'e', 'f', 'g'}
print(set_value_1.isdisjoint(set_value))  # True


set_value = {'a', 'b', 'c'}
set_value_1 = {'a', 'b'}
print(set_value_1.issubset(set_value))  # T
print(set_value.issuperset(set_value_1))  # T

set_value = {'a', 'b', 'c'}
set_value_1 = {'d', 'e'}
print(set_value.union(set_value_1))  # {'d', 'a', 'c', 'e', 'b'}

set_value = {'a', 'b', 'c'}
set_value_1 = {'b', 'e'}
print(set_value.intersection(set_value_1))  # {'b'}

set_value = {'a', 'b', 'c'}
set_value_1 = {'b', 'e'}
print(set_value.difference(set_value_1))  # {'a', 'c'}
print(set_value_1.difference(set_value))  # {'e'}


set_value = {'a', 'b', 'c'}
set_value_1 = {'b', 'e'}
print(set_value.symmetric_difference(set_value_1))  # {'a', 'c', 'e'}


"""
====================   修改   ====================
"""

set_value = {'a', 'b', 'c'}
# 插入数据
set_value.update({'d', 'e'})
print(set_value)  # {'a', 'b', 'c', 'd', 'e'}

# 多参数插入
set_value.update({'d', 'e'}, {'f', 'g', 'h', 'i'})
print(set_value)  # {'f', 'c', 'h', 'b', 'i', 'g', 'a', 'e', 'd'}

# 不可修改的集合
frozenset_value = frozenset('abcd')
print(frozenset_value)  # frozenset({'b', 'a', 'd', 'c'})
# frozenset_value.update({'d', 'e'})  # AttributeError: 'frozenset' object has no attribute 'update'

# 改变原集合的集合操作
# 交集结果赋予原集合
set_value = {'a', 'b', 'c'}
set_value_1 = {'b', 'f', 'g'}
set_value.intersection_update(set_value_1)
print(set_value)  # {'b'}

# 差集结果赋予原集合
set_value = {'a', 'b', 'c'}
set_value_1 = {'b', 'f'}
set_value.difference_update(set_value_1)
print(set_value)  # {'a', 'c'}

# 对称差集赋予原集合
set_value = {'a', 'b', 'c'}
set_value_1 = {'b', 'f', 'g'}
set_value.symmetric_difference_update(set_value_1)
print(set_value)  # {'a', 'c', 'f', 'g'}

'''
add
add的字符串作为一个整体添加进集合，而update会拆分后添加
'''
set_value = {'a', 'b', 'c'}
set_value.update('de')
set_value.add('fg')
print(set_value)  # {'e', 'b', 'a', 'c', 'd', 'fg'}


"""
====================   删除   ====================
remove  删除不存在的元素，会报错
discard 静默处理
pop 随机从集合中弹出一个元素
clear 清空集合
"""
set_value = {'a', 'b', 'c'}
set_value.remove('a')
# set_value.remove('d')  # KeyError: 'd'
set_value.discard('d')
print(set_value)  # {'b', 'c'}

set_value = {'a', 'b', 'c'}
print(set_value.pop())  # a
print(set_value)  # {'c', 'b'}

set_value.clear()
print(set_value)  # set()


