"""
## 今日作业

### 简答题

（1）闭包的特点是什么？
必须是函数嵌套，外函数的返回值是定义的内函数名，内函数可以使用外函数参数；
外函数名 + (外函数参数) 返回固定参数环境的内函数，调用此内函数相当于缓存了外函数参数
不同外函数参数，返回不同参数环境的内函数。

（2）什么是装饰器？装饰器有哪些特点？
装饰器是python的一种语法糖，格式为@+函数名+参数，写到在使用函数定义的上方
函数需要提前定义闭包函数，且闭包函数参数是使用函数，可以在闭包函数内部调用
作用是如名字所诉，给指定函数添加装饰功能
实质：使用python函数也是对象，函数名可以被传递和调用的特性，做的语法糖，实现了不改主逻辑，就能添加新功能的能力。符合开闭原则
如下案例4：
def append_suffix(suffix):
    def fun_holder(fun):
        def call_fun(src_str: str):
            fun(''.join([src_str, suffix]))
        return call_fun
    return fun_holder


@append_suffix('.txt')
def txt_suffix(string):
    print(string)

语法糖解析为：
txt_suffix('xxx') = append_suffix('.txt')
                = fun_holder(txt_suffix) + [suffix='.txt']
                = call_fun('xxx') + [suffix='.txt', fun=txt_suffix]
                = print(''.join(['xxx', '.txt']))
### 实操题
"""


# （1）定义一个闭包，用于求解方程的y与x值的变化，例如 y = ax + b。


def get_result(a, b):
    def call_fun(x):
        return a * x + b

    return call_fun


# （2）创建一个闭包，实现统计函数执行的次数功能。有如下调用闭包函数的代码：
def func_count():
    count = 0

    def call_fun():
        nonlocal count
        count += 1
        print(count)

    return call_fun


# （3）请使用装饰器方式来统计输出100000句"黑马程序员YYDS"的执行时间。
import time


def timer(fun):
    def call_fun():
        start_time = time.time()
        fun()
        end_time = time.time()
        print()
        print(f'{(end_time - start_time):.2f} s')
    return call_fun


@timer
def print_fun():
    for i in range(100000):
        print('黑马程序员YYDS', end=',')


# （4）定义一个函数, 返回字符串, 使用装饰器实现对这个字符串添加后缀.txt。
def append_suffix(suffix):
    def fun_holder(fun):
        def call_fun(src_str: str):
            fun(''.join([src_str, suffix]))
        return call_fun
    return fun_holder


@append_suffix('.txt')
def txt_suffix(string):
    print(string)


@append_suffix('.csv')
def csv_suffix(string):
    print(string)


if __name__ == "__main__":
    f1 = get_result(2, 1)
    print(f1(5))
    print(f1(6))

    f2 = func_count()
    f2()
    f2()
    f2()

    print_fun()

    txt_suffix('python')
    csv_suffix('python')

