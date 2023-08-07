"""
================== 课后作业 ==================
"""

'''
## 题目5 [加强训练]

#### 定义一个函数max1，接受的参数类型是数值，最终返回两个数中的最大值
#### 定义一个函数min1，接受的参数类型是数值，最终返回两个数中的最小值
'''


def max1(x: int, y: int):
    return x if x > y else y


def min1(x, y):
    return x if x < y else y


'''
## 题目7
定义一个函数 sum_random 接收二个参数 m, n ，在函数中计算 m + n 的值，并打印结果，要求 m 和 n 是 1 -- 100 之间的数
##### 训练提示
第一步：定义函数并接收两个参数
第二步：判断这两个参数是都在1-100之间，如果在，将这两个数相加值保存，如果不在则提示输入错误
第三步：调用函数
'''


def sun_random(m, n):
    if m not in range(1, 101) or n not in range(1, 101):
        print("输入错误")
    return m + n


print(sun_random(int(input("请输入m：")), int(input("请输入n："))))

'''
## 题目8
用函数实现一个判断用户输入的年份是否是闰年的程序，在函数中打印结果。
##### 训练提示
1.能被400整除的年份
2.能被4整除，但是不能被100整除的年份
以上2种方法满足一种即为闰年
'''


def is_run_year(year):
    if year & 400 == 0 or (year % 4 and year % 100 != 0):
        print("is")
    else:
        print("no")


is_run_year(2012)


'''
## 题目10
定义一个函数cut_str，接受三个参数，分别为字符串s、数值a1、数值a2，将字符串s从下标a1-1开始的a2个字符删除，并把结果返回
例如：
```python
s = "123456789", a1 = 2, a2 = 4 结果为: "16789"
```
##### 训练提示
1、函数的定义
2、函数的参数
3、字符串的切割
'''


def func(s: str, *, a1, a2):
    pre_s = s[:a1 - 1]
    pro_s = s[a1 - 1 + a2:]
    return ''.join([pre_s, pro_s])


print(func("123456789", a1=2, a2=4))


'''
### 题目11
请定义两个函数，一个函数打印正方形，一个函数打印三角形，并且可以从键盘输入值来决定打印矩形还是打印三角形以及决定是否退出程序
##### 训练提示
1、函数的定义
2、函数的调用
3、逻辑判断以及循环
思路提示 ：定义两个函数，一个函数打印三角形，一个函数打印矩形，通过判断用户输入来决定调用哪个函数
'''


def print_rect():
    side = 10
    for i in range(side):
        print('* ' * side)


def print_triangle():
    side = 10
    for i in range(side):
        print(' ' * (side - i), '*' * i)


def select():
    while True:
        option = int(input("请操作（0：退出， 1：打印正方形， 2：答应三角形）："))
        if option == 0:
            break
        elif option == 1:
            print_rect()
        elif option == 2:
            print_triangle()
        else:
            print('option错误！')


select()
















