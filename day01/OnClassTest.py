"""
================== 注释 ==================
"""

# 单行

"""
多行 双引号注释
"""

'''
多行 单引号
'''

"""
================== 变量: 数据类型 ==================
"""
# int
a = 1
# string
b = '2'
# float
c = 0.1
# bool
d = True
# 列表， 没有数组概念！
g = [1, 2, 3]
# 元组数据类型，一旦定义不能修改其值
h = (1, 2, 3)
"""
TypeError: 'tuple' object does not support item assignment
所以元组不能修改内容
def try_change_tuple():
    h[0] = 1
"""

# 集合 set 类似java set 去重（元素唯一），查询会快么？
i = {'c', 'd'}  # {'c', 'd'}
j = {'a', 'a', 'a', 'b'}  # {'b', 'a'} 因为去重会修改顺序？
k = {'4', '4', '3', '3', '2', '2', '1', '1'}  # {'4', '1', '2', '3'} 乱序？可能不是都需遍历
# 字典 java的map？键值对？ 有点像ios字典
m = {'name': 'xiaoming', 'age': 12, 'sex': '女'}

"""
================== 占位符区别 ==================
"""
floatValue = 0.1
print('value is %d' % floatValue)  # value is 0
print('value is %f' % floatValue)  # value is 0.100000
print('value is %s' % floatValue)  # value is 0.1
print('value is %.2f' % floatValue)  # value is 0.10
floatValue = 3.1415926
print('value is %.3f' % floatValue)  # value is 3.142  自动四舍五入
print('value is %.0f' % floatValue)  # value is 3  .0和.一样，取小数点后0位
print('value is %.f' % floatValue)  # value is 3 .0和.一样，取小数点后0位
intValue = 11
print('value is %d' % intValue)  # value is 11
print('value is %05d' % intValue)  # value is 00011
# print('value is %15d' % intValue)  # 没有这种case
# print('value is %x5d' % intValue)  # 没有这种case
intValue = 1234567
print('value is %02d' % intValue)  # value is 1234567； 数据本身比占位要求长，会全部显示

"""
================== format方式 ==================
"""
s_value = 'xxx'
f_value = 3.1415926
print('value = %s' % s_value)
print('value = {}'.format(s_value))
print('value = {f_value:.2f}')  # log: value = {f_value:.2f}
print(f'value = {f_value:.2f}')  # log: value = 3.14  证明字符串内想要使用{}format，必须在前面f
print(f'value = {s_value}')  # log: value = xxx  证明最前面的f代表format，与float无关

"""
================== 输入，输出 ==================
"""
pwd = input('pwd is : ')
print(pwd)

"""
================== string 方法尝试 ==================
"""
print(s_value.__eq__('x'))  # same of ==
print(s_value == 'xxx')
# print(s_value === 'xxx')  # python 没有全等概念

string = 'abcdcba'
print(string.index('cdc'))
# 列表index
countNums = [180, 160]
print(countNums.index(160))

print(string.find('cdc'))
print(string.count('a'))
print(string.count('d'))
print(string.__contains__('abc'))
# print(string.index('efg'))  # ValueError: substring not found, 保存而不是-1
print(string.__contains__('efg'))

"""
================== 课堂练习 ==================
"""
# 打印
mySelf = {'name': 'haha', 'age': 30, 'height': 170}
print(f'my name is %s, age is %d, height is {mySelf.get("height")}' % (mySelf['name'], mySelf.get('age')))

# 间隔符、结束符
print('a', 'b', 'c', sep=',')
print('a', end=',')
print('b', end=',')
print('c', end='\n')  # \n 换行符
print('d', end='\t')  # \t tab对齐
print('===========')

# 输入输出
stuName = input('学生姓名：')
stuAge = int(input('学生年龄：'))
stuHeight = float(input('学生身高：'))
stuNo = input('学生学号：')
print(f'学生{stuName}, 年龄%d岁, 身高%.1fm, 学号是{stuNo}' % (stuAge, stuHeight))

# 算苹果价格
price = float(input('当前苹果单价： '))
weight = float(input('购买苹果重量： '))


def cale():
    return price * weight


print('总价：%.2f元' % cale())
