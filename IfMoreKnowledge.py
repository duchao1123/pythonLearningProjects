"""
====================   if进阶使用   ====================
in
not in
关键字；判断元素是否在容器内存
"""

str_value = '123'
print('1' in str_value)
print('4' not in str_value)

list_value = [1, 2, 3]
print(1 in list_value)
print(4 not in list_value)

tuple_value = (1, 2, 3)
print(1 in tuple_value)
print(4 not in tuple_value)

set_value = {1, 2, 3}
print(1 in set_value)
print(4 not in set_value)

# dict 判断key
dict_value = {1: '1', 2: '2'}
print(1 in dict_value)
print(4 not in dict_value)



