"""
================== 课后作业 ==================
"""
'''
# 每日必会题
## 题目1
### 题干
有一个空字典dict1 = {}，请给他添加一个为name:python的键值对
'''
dict1 = {}
dict1['name'] = 'python'

'''
## 题目2
### 题干
现有字典dict1 = {'name':'python'}，将键为'name'的值更改为'chuanzhi'
'''
dict1 = {'name': 'python'}
dict1['name'] = 'chuanzhi'
dict1.update(name='chuanzhi')

'''
## 题目3
### 题干
请创建一个空集合set1
'''
set1 = set()
set2 = set({})
set3 = {value for value in range(0)}
print(set1)
print(set2)
print(set3)

'''
## 题目4
### 题干
有一个集合set1 = {1,2,3,4}
请实现：给set1添加一个元素5
'''
set1 = {1, 2, 3, 4}
set1.add(5)
print(set1)

set1 = {1, 2, 3, 4}
set1.update({5})
print(set1)

'''
## 题目1
### 题干
现有字典dict1 = {'name':'chuanzhi','age':18}
  要求：1.删除age：18这个键值对
       2.将整个字典里面的所有键值对，清空
'''
dict1 = {'name': 'chuanzhi', 'age': 18}
del dict1['age']
print(dict1)

dict1 = {'name': 'chuanzhi', 'age': 18}
dict1.pop('age')
print(dict1)

dict1 = {'name': 'chuanzhi', 'age': 18}
dict1.popitem()
print(dict1)

dict1.clear()
print(dict1)

'''
## 题目2
### 题干
现有字典dict1 = {'name':'chuanzhi','age':18}
要求：1.使用循环将字典中所有的键输出到屏幕上
    2.使用循环将字典中所有的键输出到屏幕上
    3.使用循环将字典中所有的键值对输出到屏幕上
      输出方式：  name：chuanzhi
                age: 18
'''
dict1 = {'name': 'chuanzhi', 'age': 18}
for k, v in dict1.items():
    print(f'{k}: {v}')

for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)

for string in [f'{k}:{v}' for k, v in dict1.items()]:
    print(string)
'''
## 题目3
### 题干
有这样的一个列表
product=[
{"name":"电脑","price":7000},
{"name":"鼠标","price":30},
{"name":"usb电动小风扇","price":20},
{"name":"遮阳伞","price":50},
]，然后小明一共有8000块钱，那么他能不能买下这所有商品？
如果能，请输出“能”，否则输出“不能”
'''
product = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 30},
    {"name": "usb电动小风扇", "price": 20},
    {"name": "遮阳伞", "price": 50},
]


def check_enough(value):
    for dict_value in product:
        price = dict_value['price']
        value -= price
        if value < 0:
            print('金额不足')
            break
    else:
        print('金额足够')


check_enough(7000)
'''
## 题目4
### 题干
有一个集合set1 = {1,2,3,4}
请实现：删除集合中的任意一个元素
'''
set1 = {1, 2, 3, 4}


def delete_e_safely(el):
    if el in set1:
        set1.remove(el)
        print('删除成功')
    else:
        print('元素不存在')
    print(set1)


set2 = {1, 2, 3, 4}


def delete_e(el):
    set2.discard(el)
    print('删除成功')
    print(set2)


delete_e_safely(5)
delete_e_safely(4)
delete_e(5)
delete_e(4)
'''
## 题目5
### 题干
有一个集合list1 = (1,2,3,4,3)
请完成去重复的功能，并且最后依然是集合
'''
list1 = (1, 2, 3, 4, 3)
print(list(set(list1)))

'''
# 企业面试题
## 1. 生成如下列表 [[0,0,0,0,0,],[0,1,2,3,4,],[0,2,4,6,8,],[0,3,6,9,12,]]
## 2. 把列表`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`中的每个元素都加100，生成一个新列表(使用三种方式)
## 3. 根据提供的两个列表, 生成指定的列表
```python
已知:list1 = ["A","B","C"], list2 = ["X","Y","Z"]使用列表推导式生成['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```
'''
print([[el * value for el in range(5)] for value in range(4)])

old_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [value + 100 for value in old_list]
print(new_list)

new_list_1 = []
for index in range(len(old_list)):
    new_list_1.append(old_list[index] + 100)
print(new_list_1)

new_list_1 = old_list[:]
index = 0
while index < len(new_list_1):
    new_list_1[index] += 100
    index += 1
print(new_list_1)  #

# 使用列表推导式生成['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
list1 = ["A", "B", "C"]
list2 = ["X", "Y", "Z"]

new_list_1 = [''.join([value0, value1]) for value0 in list1 for value1 in list2]
print(new_list_1)  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

