"""
====================   List链表常用函数   ====================

创建、获取、长度
增、删、改
排序、反转
清除、拷贝
最大值、最小值
"""

'''
创建列表 
可以为空创建，可以扩容
多维列表
利用列表推导式创建二维列表
'''
list_value = [1, 2, 3]  # 知道元素情况
list_value_1 = []  # 未知元素情况
list_value_2 = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
print(list_value_2)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

list_value = [[0] * 3 for value in range(3)]
print(list_value)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

'''
获取
'''
# print(list_value[0])
# # print(list_value[3])  # IndexError: list index out of range, 索引越界
# list_len = len(list_value)
# max_index = list_len - 1
# print(list_value[max_index])

'''
修改
索引修改
切片整体修改
'''
# list_value = [0, 1, 2, 4, 5, 6]
# list_value[0] = 8
# print(list_value)
#
# list_value[2:] = 'a'
# print(list_value)  # [8, 1, 'a']
#
# list_value = [0, 1, 2, 4, 5, 6]
# list_value[2:] = ['a', 'b', 'c']
# print(list_value)  # [0, 1, 'a', 'b', 'c']

'''
增
append() 在列表末尾添加
insert() 指定位置添加   param0: 插入索引, param1: 插入元素
extend() 添加可迭代容器
切片追加
list 运算
'''
# list_value = [1, 2, 3]
# list_value.append(5)
# list_value.append(6)  # [8, 2, 3, 5, 6], 不能append多元素
# print(list_value)
#
# list_value.insert(3, 4)  # [8, 2, 3, 4, 5, 6]; param0: 插入索引, param1: 插入元素
# print(list_value)
#
# list_value.extend([7, 8, 9])
# print(list_value)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# list_value.extend((10, 11, 12))
# print(list_value)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# # 从len(list_value)索引位置添加
# list_value[len(list_value):] = [13, 14, 15]
# print(list_value)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# # +
# list_value = [1, 2, 3]
# list_value_1 = [4, 5, 6]
# print(list_value + list_value_1)  # [1, 2, 3, 4, 5, 6]
#
# # - 不支持 TypeError: unsupported operand type(s) for -: 'list' and 'list'
# # list_value = [1, 2, 3, 4, 5]
# # list_value_1 = [2, 3]
# # print(list_value - list_value_1)
#
# # * 不支持 list * list; TypeError: can't multiply sequence by non-int of type 'list'
# list_value = [1, 2, 3]
# list_value_1 = [2, 3]
# # print(list_value * list_value_1)
# print(list_value * 2)  # [1, 2, 3, 1, 2, 3] 重复，类似重复打印

# / 可预见不支持该操作

'''
删
# pop(index)， 删除并返回指定元素，默认index为最后一个
# del list[index] 无返回值
# remove(value) 删除指定元素
'''
# pop(index)， 删除并返回指定元素，默认index为最后一个
# list_value = [1, 2, 3]
# print(list_value.pop())  # 3
# print(list_value)  # [1, 2]
# list_value = [1, 2, 3]
# print(list_value.pop(1))  # 2
# print(list_value)  # [1, 3]
#
# # del 无返回值
# list_value = [1, 2, 3]
# del list_value[0]
# print(list_value)  # [2, 3]
#
# # remove(value) 删除指定元素
# list_value = [1, 2, 3]
# list_value.remove(3)
# print(list_value)  # [1, 2]
#
# list_value = [1, 2, 3]
# # list_value.remove(4)  # ValueError: list.remove(x): x not in list, 删除不存在的元素报错
#
# # print(list_value.index(4))  # ValueError: 4 is not in list, 获取不存在的元素的索引报错
# print(list_value.__contains__(4))  # False, 可以先判断是否包含
# print(list_value.count(4))  # 0, 可以先获取元素的数量
#
# '''
# 其他：
# __contains__   判断是否包含元素
# count    获取元素的数量
# sort  给原列表排序
# sorted 生成排序后的原列表副本
# reverse 反转原列表
# reversed 生成反转后的原列表副本
# clear 清除
# copy 请拷贝一个副本
# '''
#
# # sort 、 sorted
# list_value = [2, 5, 8, 3, 6, 1, 7]
# list_value.sort()
# print(list_value)  # [1, 2, 3, 5, 6, 7, 8]
#
# list_value = [2, 5, 8, 3, 6, 1, 7]
# new_list = sorted(list_value)
# print(new_list)  # [1, 2, 3, 5, 6, 7, 8]
# print(f'old_l = {id(list_value)}, new_l = {id(new_list)}')  # old_l = 140184242959488, new_l = 140184511861824
#
#
# # reverse 、 reversed
# list_value = [1, 2, 3, 4]
# list_value.reverse()
# print(list_value)  # [4, 3, 2, 1]
#
# list_value = [1, 2, 3, 4]
# new_list = list(reversed(list_value))  # reversed返回的是一个迭代器，需要list强转
# print(list_value)  # [1, 2, 3, 4]
# print(new_list)  # [4, 3, 2, 1]
# print(f'old_l = {id(list_value)}, new_l = {id(new_list)}')  # old_l = 140284638275264, new_l = 140284638879936
#
# # clear 清除
# list_value = [1, 2, 3]
# list_value.clear()
# print(list_value)  # []
#
# # copy 请拷贝一个副本
# list_value = [1, 2, 3]
# new_list = list_value.copy()
# print(new_list)  # [1, 2, 3]
# print(f'old_l = {id(list_value)}, new_l = {id(new_list)}')  # old_l = 140573072172736, new_l = 140573072184384
#
# '''
# 最大值、最小值
# max
# min
# '''
# list_value = [1, 2, 3]
# print(max(list_value))  # 3
# print(min(list_value))  # 1
#
#
# '''
# 负数索引 = 反向索引
# '''
# list_value = [1, 2, 3]
# print(list_value[-1])
#
#
# str_value = "abcd"
# print(str_value[0])
# print(str_value[-1])

