"""
====================   Tuple更多知识   ====================
1、定义元组可以不带()
2、元组也支持切片
3、解包，不止元组，list、set、dict等数据类型都支持
推导式：类似list？ 元组没有推导式 （value for value in lsit）这个叫生成器
"""

'''
创建
'''
# 正常创建
tuple_value = (1, 2, 'a', 'b', True)
print(tuple_value)

# 不携带（）; 不推荐， 容易引起争议，降低阅读性
tuple_value_1 = 1, 2, 'a', 'b', True
print(tuple_value_1)  # (1, 2, 'a', 'b', True)

# 生成一个元素的元组, 必须加 ','
tuple_value_2 = (1)
print(type(tuple_value_2))  # <oopclass 'int'>
tuple_value_2 = (1, )
print(type(tuple_value_2))  # <oopclass 'tuple'>

'''
获取
索引获取： 略
切片获取
'''

tuple_value = 1, 2, 3, 4, 5
new_tuple_value = tuple_value[:]
print(new_tuple_value)  # (1, 2, 3, 4, 5)

'''
其他方法
count: 略
index：略
元组 + 元组：类似list 略
元组 * 数： 类似list 略
'''

'''
解包
'''
tuple_value = (1, 2, 3)
x, y, z = tuple_value
print(f'x = {x}, y = {y}, z = {z}')  # x = 1, y = 2, z = 3
set_value = {'a', 'b', 'c'}
x, y, z = set_value
print(f'x = {x}, y = {y}, z = {z}')  # x = c, y = a, z = b

# dict只对key做解包赋值
dict_value = {'name': 'xiaoming', 'age': 18, 'phone': '110'}
x, y, z = dict_value
print(x)




