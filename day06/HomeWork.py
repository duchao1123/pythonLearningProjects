"""
================== 课后作业 ==================
"""

'''
# 每日必会题
## 题目1
### 题干
定义一个简单的函数run，函数的功能是输出"我在跑步" 以及 “管住嘴，迈开腿”，并调用此函数。
'''


def run():
    print("我在跑步")
    print("管住嘴，迈开腿")


run()

'''
## 题目2
### 题干
在第一题中，我们已经用函数run实现了一些功能，如果我们想run函数做的操作执行1000遍，怎么实现代码？
'''


def run():
    for i in range(100):
        print("我在跑步")
        print("管住嘴，迈开腿")


run()

'''
## 题目3
### 题干
现在我们来实现一个有参数有返回值的函数addnum，并实现调用，要求如下 ：
我们要用函数来实现7与13两个数字的加法运算，并返回两个数的和进行输出
'''


def addnum(x, y):
    result = x + y
    print(f'result = {result}')
    return result


addnum(7, 13)

'''
# 每日练习题
## 题目1
### 题干
手机上都有计算器的功能（两个数字的加减乘除）并且实现将结果输出，那么假如你是开发人员，你怎么用一个函数来实现这个功能？
例如：输入： 2+33
​	 输出：和为35
'''


def cale(*, option: str, x: int, y: int):
    if option == '+':
        result = x + y
        print(f'和为{result}')
        return result
    elif option == '-':
        result = x - y
        print(f'差为{result}')
        return result
    elif option == '*':
        result = x * y
        print(f'积为{result}')
        return result
    elif option == '/':
        result = x / y
        print(f'商为{result}')
        return result


def exec_cale(option_str: str):
    if '+' in option_str:
        params_list = [int(value.strip()) for value in option_str.split('+')]
        return cale(option="+", x=params_list[0], y=params_list[1])
    elif '-' in option_str:
        params_list = [int(value.strip()) for value in option_str.split('-')]
        return cale(option="-", x=params_list[0], y=params_list[1])
    elif '*' in option_str:
        params_list = [int(value.strip()) for value in option_str.split('*')]
        return cale(option="*", x=params_list[0], y=params_list[1])
    elif '/' in option_str:
        params_list = [int(value.strip()) for value in option_str.split('/')]
        return cale(option="/", x=params_list[0], y=params_list[1])
    else:
        print("不支持")


# exec_cale(input("请输入："))
#
# print(f'result = {eval(input("请输入："))}')

'''
## 题目2
### 题干
有如下代码：

```python
num = 10
def anum():
    num = 20
print(num)
```
请问这段代码最终输出的值是多少？ 
'''
10

'''
## 题目3

### 题干
有如下代码：
```python
def abnum(big, small, middle):
    .....#此处省略一千行代码
```
现在要调用abnum函数，但是怕在调用的时候将参数的位置传错，如何避免这个情况？写一段代码示范下
'''
print('关键字参数')
print('big=1, small=2, middle=3')

'''
# 企业面试题

## 题目1
### 题干
在填写个人资料时，如果选了女性，那么性别是女；如果不选性别，那就是默认是男，那么这个功能用函数怎么实现？
要求如下：定义一个函数gender，并在函数中将“所选性别为*”，并可以成功调用运行。
'''


def gender(sex: str = '男'):
    print(f'sex = {sex}')


gender('女')
gender()

'''
## 题目2
### 题干
要求实现一段代码：
声明一个函数num，并且在调用函数的时候，不管输入多少个非关键字参数，函数都可以运行，且在函数内部还要把每个参数输出到屏幕上。
'''


def num(*params):
    pass


num(1, 2, 3, 4, 5, 6)


'''
## 题目3
### 题干
如下所示这是一个字典，{"name":"电脑","price":7000}
请定义这样一个函数num，讲上述字典中的键值对传入到函数num中，要求用不定长参数来接收，并在函数中打印键值对输出
输出格式为：key：”name“   value：“电脑”
​		  key：“price”    value：7000
'''


def num(**params):
    for k, v in params.items():
        print(f'key = {k}, value = {v}')


num(name='电脑', price=7000)

'''
## 题目4
### 题干
对于一个函数num，当调用nun(1,2,a=3,b=4)和调用num(3,4,5,6,a=1)以及num(a=1,b=2)的时候都可以正常运行，
并且可以对元组以及字典类型进行遍历输出，对字典类型进行输出字典的键值对(形式为：key：a，value：1)，
请写出这个函数并完成调用。
'''


def num(*args, **kvargs):
    print(args)
    for arg in args:
        print(arg)
    for k, v in kvargs.items():
        print(f'key: {k}, value: {v}')


num(1, 2, a=3, b=4)
num(3, 4, 5, 6, a=3)
num(a=1, b=2)



'''
# 企业面试题
## 题干1
Python函数调用的时候参数的传递方式是值传递还是引用传递？
'''
"""
基础数据类型是值传递，引用数据类型是引用传递
"""

'''
## 题干2
对缺省参数的理解?
'''
"""
在定义函数时，可以给某个参数指定一个默认值，具有默认值的参数就叫做缺省参数。
调用函数时，如果没有传入缺省参数的值，则在函数内部使用定义函数时指定的参数默认值。
作用：函数作者定义的默认参数、常规参数，有助于调用者调用函数
"""

'''
## 题干3
为什么函数名字可以当做参数用?
'''
"""
函数名本质上是一个对象，可以被赋值给变量，也可以作为参数传递给其他函数
"""


'''
## 题干4
Python中pass语句的作用是什么?
'''
"""
无函数体，或函数体占位，比如封装接口使用
"""


'''
## 题干5
有这样一段代码，print c会输出什么，为什么?
```python
a = 10
b = 20
c = [a]
a = 15
```
'''
"""
[10]
"""
a = 10
b = 20
c = [a]
a = 15
print(c)  # 10
"""
a是基础数据类型，构造列表时，赋值后固定，外部修改变量a不对列表内元素造成影响
"""



