"""
================== 课后作业 ==================
"""

'''
# 每日必会题
## 题目1 
### 题干
使用while循环计算1~100的累加和（包含1和100）
### 训练目标
- whlie循环的基本使用
'''
sum_v = 0
i = 1
while i <= 100:
    sum_v += i
    i += 1
print(sum_v)


print('=========================')
'''
## 题目2
### 题干
使用while嵌套循环打印如下图形
```
*
* *
* * *
* * * *
* * * * *
```
### 训练目标
- while嵌套循环的使用
'''
i, j = 0, 0
while i < 5:
    j = 0
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1


print('=========================')
'''
## 题目3
### 题干
编写代码模拟用户登陆。要求：用户名为 python，密码 123456，如果输入正确，打印“欢迎光临”，程序结束，如果输入错误，提示用户输入错误并重新输入
### 训练目标
- while中的break的使用
'''
while True:
    name = input('name = ')
    pwd = input('pwd = ')
    if name == 'python' and pwd == '123':
        print('正确!')
        break
    else:
        print('错误!')


print('=========================')
'''
## 题目4
### 题干
设计“过7游戏”的程序, 打印出1-100之间除了7和7的倍数之外的所有数字，如果遇见7和7的倍数则打印“哈~”跳过本次循环。
### 训练目标
- while中的continue的使用
'''
for v in range(1, 101):
    if v % 7 == 0:
        print('哈')
        continue
    print(v)


print('=========================')
'''
## 题目1
### 题干
请用户输入一个数，使用while计算是否为素数
### 训练目标
- while...else的使用
'''
int_value = int(input('value = '))
v = 2
while int_value % v != 0:  # 除了1和自己不能整除，是素数
    if v < int_value // 2:  # 除数范围[2，value / 2]
        v += 1
    else:
        print(f'{int_value} 是素数')
        break
else:  # while 正常执行完成，证明int_value可以被整除，不是素数
    print(f'{int_value} 不是素数')

'''
## 题目2
### 题干
要求用户输入一个字符串，遍历当前字符串并打印，如果遇见“q”,则跳出循环。如果遇见“ ”（空格）则跳过当前输出。
### 训练目标
- for循环的基本使用
- break的作用
- continue的作用
'''
str_value = input("str = ")
for c in str_value:
    if c == 'q':
        break
    elif c == ' ':
        continue
    print(f'c = {c}')


print('=========================')
'''
## 题目3
### 题干
使用for循环计算用户输入值的累加和
### 训练目标
range()的使用
'''
total_value = 0
for v in range(int(input("start = ")), int(input("stop = ")), int(input("step = "))):
    total_value += v
print(total_value)

print('=========================')
'''
## 题目4
### 题干
请用户输入一个数，使用for循环计算是否为素数
### 训练目标
for...else是使用
'''
input_value = int(input('value = '))
for v in range(2, input_value // 2 + 1):
    if input_value % v == 0:
        print(f'{input_value} 不是素数')
        break
else:
    print(f'{input_value} 是素数')


print('=========================')
'''
## 题目5
### 题干
分别使用for循环和while循环，求100~200的所有素数
### 训练目标
- 循环嵌套的使用
- if条件判断
- while...else for...else的使用场景
'''
for value in range(100, 201):
    for s in range(2, value // 2 + 1):
        if value % s == 0:
            break
    else:
        print(value)

print('=========================')
int_value = 100
while 100 <= int_value <= 200:
    s_v = 2
    while 2 <= s_v <= int_value // 2 + 1:
        if int_value % s_v == 0:
            break
        else:
            s_v += 1
    else:
        print(int_value)
    int_value += 1

'''
# 企业面试题
'''

'''
##1. 阅读下面的代码，写出A0，A1至An的最终值。
```python
\1.    A0 = dict(zip(('a'，'b'，'c'，'d'，'e')，(1，2，3，4，5)))
\2.    A1 = range(10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
\3.    A2 = [i for i in A1 if i in A0]
\4.    A3 = [A0[s] for s in A0]
\5.    A4 = [i for i in A1 if i in A3]
\6.    A5 = {i:i*i for i in A1}
\7.    A6 = [[i，i*i] for i in A1]
```
'''
zip_result = zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5))
print(zip_result)
print(type(zip_result))  # <oopclass 'zip'>
dict_value = dict(zip_result)
print(dict_value)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

a2 = [i for i in range(10) if i in dict_value]
print(a2)

'''
##2.  range和xrange的区别？
'''
range_value = range(1, 10, 2)
print(range_value)
print(type(range_value))

# Python 2.x中存在内置函数xrange， Python 3.x移除
# xrange(0, 6, 2)
# list(xrange(0,6,2))  # 与range用法无区别， 返回值为生成器，需要强转

'''
## 3. 考虑以下Python代码，如果运行结束，命令行中的运行结果是什么？
```python
\1.  l = []
\2.   for  i  in  xrange(10):
\3.       l.append({‘num’:i})
\4.   print l
```
载考虑以下代码，运行结束后的结果是什么？
```python
\1.   l = []
\2.   a = {‘num’:0}
\3.   for i in xrange(10):
\4.       a[‘num’] = i
\5.       l.append(a)
\6.   print l
```
以上两段代码的运行结果是否相同，如果不相同，原因是什么？
'''
l = []
for i in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    l.append({'num': i})  # [{'num': 0}, {'num': 1}, ...]
print(l)

l = []
a = {'num': 0}
for i in range(10):
    a['num'] = i  # a = {'num': 0}; a = {'num': 1}; ....
    l.append(a)
print(l)  # [{'num': 9}, {'num': 9}, ...]
# append的是同一个dict(字典的句柄)，占1份内存，修改都是对字典本身进行的操作，所以打印结果为最后修改状态
# 而l.append({'num': i})，每次append一个【新的】【匿名】的字典，占10份内存，修改相互不影响

print('=========================')
'''
##4. 以下Python程序的输出？
```python
\1. for i in range(5，0，-1):
\2.       print(i)
```
'''
for i in range(5, 0, -1):  # 开始比结束大， step负数， 反向输出
    print(i)

# 5
# 4
# 3
# 2
# 1
# 居然倒叙输出了
print('=========================')

for i in range(5, 0, 1):  # 开始大于结束，step正常，无输出
    print(i)

print('=========================')

for i in range(-5, 0, 1):
    print(i)

# -5
# -4
# -3
# -2
# -1

print('=========================')

for i in range(-5, 0, -1):  # 开始小于结束，step不能负数，不能反向输出
    print(i)




