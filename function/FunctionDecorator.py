"""
====================   装饰器   ====================
"""
'''
例子：统计方法调用时间
'''
import time


def long_time_fun():
    time.sleep(2)
    print('exec finished!')


def time_checker(func):
    print('开始计时')
    start_time = time.time()
    func()
    print('结束计时')
    end_time = time.time()
    total_time = end_time - start_time
    print(f'总耗时 = {total_time:.2f}s')


# time_checker(long_time_fun())


# time_checker(long_time_fun)  # 显然time_checker不是每次期望调用的目标，但是需要调用fun，就执行到time_checker
# 1、修改time_checker， 希望调用time_checker传递一个fun，能返回调用fun获取计时的函数引用
def time_checker_1(func):
    def call_fun():
        print('开始计时')
        start_time = time.time()
        func()
        print('结束计时')
        end_time = time.time()
        total_time = end_time - start_time
        print(f'总耗时 = {total_time:.2f}s')
    return call_fun


# # 2、定义函数变量long_time_fun，传递函数long_time_fun， 返回一个能在call_fun内部调用的函数引用
# long_time_fun = time_checker_1(long_time_fun) = call_fun
# # 3、调用函数引用，相当于调用了call_fun，func = long_time_fun
# long_time_fun() = call_fun() = func()


# 再次优化，python定义 2， 3步为装饰器，即可以给任意函数添加装饰器，来实现装饰器函数内的能力
@time_checker_1
def long_time_fun_1():
    time.sleep(2)
    print('exec finished!')


# 调用装饰器函数
# long_time_fun_1()

'''
进阶例子：
如果要区分调用不同函数耗时
传入函数不同的tag，作为参数，打印是使用tag表明不同的函数
'''


def time_checker_2(tag):
    def function(func):
        def call_fun():
            print(f'{tag}开始计时')
            start_time = time.time()
            func()
            print(f'{tag}结束计时')
            end_time = time.time()
            total_time = end_time - start_time
            print(f'{tag}总耗时 = {total_time:.2f}s')
        return call_fun
    return function


@time_checker_2(tag='funA')
def fun_a():
    time.sleep(3)
    print('fun a 执行完成')


@time_checker_2(tag='funB')
def fun_b():
    time.sleep(5)
    print('fun b 执行完成')


# fun_a = time_checker_2(tag='funA') = function
# time_checker_2(tag='funA')(fun_a) =  call_fun
# fun_a() = call_fun()、tag = 'funA'、func = fun_a
fun_a()
fun_b()

'''
log:
funA开始计时
fun a 执行完成
funA结束计时
funA总耗时 = 3.00s
funB开始计时
fun b 执行完成
funB结束计时
funB总耗时 = 5.00s
'''

"""
总结：装饰函数的定义需要分析出，具体调用的函数是谁，怎么获取
"""





