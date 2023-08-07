"""
====================   字典，常用方法   ====================
创建
"""

# 创建
# 1、常规，推荐
dict_value = {'name': 'xiaoming', 'age': 18}
# 2、dict方法
dict_value_1 = dict(dict_value)
dict_value_2 = dict({'name': 'xiaoming', 'age': 18})
# 不推荐吧
dict_value_3 = dict(name='xiaoming', age=18)
dict_value_4 = dict({'name': 'xiaoming'}, age=18)
dict_value_5 = dict(zip(('name', 'age'), ('xiaoming', 18)))

print(dict_value)
print(dict_value_1)
print(dict_value_2)
print(dict_value_3)
print(dict_value_4)
print(dict_value_5)
print("========================================")

"""
增
常规dict[key] =  value, 存在进行替换，不存在进行插入
fromkeys
"""
dict_value = {'name': 'xiaoming'}
dict_value['age'] = 18
print(dict_value)  # {'name': 'xiaoming', 'age': 18}
dict_value['age'] = 19
print(dict_value)  # {'name': 'xiaoming', 'age': 19}

dict_value = dict.fromkeys(['name', 'age'], '?')
print(dict_value)  # {'name': '?', 'age': '?'}
print("========================================")

"""
删
pop(key, default), 删除key对应的键值对，不存在key，返回default
del dict[key]
clear  清空字典
"""
dict_value = {'name': 'xiaoming', 'sex': 'man'}
print(dict_value.pop('age', '不存在age'))  # 不存在age
del dict_value['sex']
print(dict_value)  # {'name': 'xiaoming'}
dict_value.clear()
print(dict_value)  # {}
print("========================================")

"""
改
常规dict[key] =  value, 存在进行替换
update 多个键值对修改
"""
dict_value = {'name': 'xiaoming', 'age': 18, 'sex': 'man'}
dict_value.update({'name': 'lilei', 'age': 19})
print(dict_value)  # {'name': 'lilei', 'age': 19, 'sex': 'man'}

dict_value = {'name': 'xiaoming', 'age': 18, 'sex': 'man'}
dict_value.update(name='lilei', age=19)
print(dict_value)  # {'name': 'lilei', 'age': 19, 'sex': 'man'}
print("========================================")

"""
查
dict[key], 但是key不存在时，会报错
get
setdefault(key, default) 如果key存在，返回。否则设置value=default
"""
dict_value = {'name': 'xiaoming', 'age': 18, 'sex': 'man'}
# print(dict_value['phone'])  # KeyError: 'phone'
print(dict_value.get('phone', '不存在phone'))  # 不存在phone
dict_value.setdefault('phone', '110')
print(dict_value)  # {'name': 'xiaoming', 'age': 18, 'sex': 'man', 'phone': '110'}
print("========================================")

"""
遍历
items 返回键值对视图对象（字典修改，此对象内容也会修改）
keys 返回键对视图对象（字典修改，此对象内容也会修改）
values 返回值对视图对象（字典修改，此对象内容也会修改）
"""
dict_value = {'name': 'xiaoming', 'age':18}
items = dict_value.items()
keys = dict_value.keys()
values = dict_value.values()

dict_value.pop('age')
print(dict_value)  # {'name': 'xiaoming'}
print(items)  # dict_items([('name', 'xiaoming')])
print(keys)  # dict_keys(['name'])
print(values)  # dict_values(['xiaoming'])
print("========================================")

"""
====================   字典推导式   ====================
"""
# 基础推导式
dict_value_data = {'a': 1, 'b': 2, 'c': 3}
dict_value = {(k + '1'): v for k, v in dict_value_data.items()}
print(dict_value)  # {'a1': 1, 'b1': 2, 'c1': 3}

# 升级推导式
dict_value_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_value = {k.upper(): v for k, v in dict_value_data.items() if v % 2 == 0}
print(dict_value)  # {'B': 2, 'D': 4}




