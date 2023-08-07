"""
====================   函数常用方法   ====================
形参、实参、关键字参数、参数默认值 略
"""
# help 方法查看方法使用说明时，
# '/'的作用：左边必须传递位置参数，而不能时关键字参数
help(abs)
'''
abs(x, /)
    Return the absolute value of the argument.
'''
# abs(x=-1)  # TypeError: abs() takes no keyword arguments
print(abs(-1))


# def abc(a, b, /, d):
#     pass

# abc(a=1, b=2, d=3)  # TypeError: abc() got some positional-only arguments passed as keyword arguments: 'a, b'
# abc(1, 2, d=3)

def abc(a, b, d):  # 没有/ 和 * 随意
    pass


abc(a=1, b=2, d=3)
abc(1, 2, 3)


def gfd(a, b, *, d):  # *左边可以使用位置参数，也可以使用关键字参数，但*右边必须使用关键字参数
    pass


gfd(1, b=2, d=3)  # SyntaxError: positional argument follows keyword argument


'''
收集参数
元组形收集参数 *args
'''


def aaa(*args, a, b):
    print(args)  # (1, 2, 3)
    print(a)  # 9
    print(b)  # 8


aaa(1, 2, 3, a=9, b=8)


'''
字典形收集参数  **kvargs
'''


def fun(**kvargs):
    print(kvargs)


# fun(1)  # TypeError: fun() takes 0 positional arguments but 1 was given
fun(a=1, b=2)  # {'a': 1, 'b': 2}


# 混合例子
def myfun(a, b, /, *e, c, d=4, **f):
    """
    :param a,b: 在 / 之前，必须使用位置参数
    :param c, d: 在 / 之后，使用关键字参数。关键字参数不能在*之前，所以在元组参数*e之后 ，d有默认值
    :param e: 元组参数
    :param f: 字典参数，关键字参数不能在字典参数之后
    """
    print(f'a = {a}, b = {b} c = {c}, d = {d}')  # a = 1, b = 2 c = 3, d = 4
    print(e)  # (5, 6, 7)
    print(f)  # {'f': 8, 'i': 9, 'h': 10}


myfun(1, 2, 5, 6, 7, c=3, f=8, i=9, h=10)

'''
解包
*解包 元组
**解包 字典
'''
args = (1, 2, 3)


def func(x, y, z):
    print(x, y, z)


# fun(args)  # 报错需要三个参数，传递了一个。TypeError: fun() takes 0 positional arguments but 1 was given
func(*args)  # 1 2 3

kvargs = {'a': 1, 'b': 2}


def fun1(a, b):
    print(a, b)


fun1(**kvargs)  # 1 2

"""
====================   函数内修改全局变量   ====================
global 关键字修饰
"""
global_value = 1


def funcc():
    # global_value = 2
    # print(global_value)  # 2
    global global_value
    global_value = 3
    print(global_value)  # 3


funcc()


print(global_value)  # 1  # 3ß


"""
====================   嵌套函数   ====================
外部无法调用嵌套函数的内部函数，需要函数内部调用
嵌套函数，内部函数修改外部函数局部变量 nonlocal 关键字修饰
规则： LEGB
local > enclosed > global > buildins
"""


def fun_outside():
    x = 1

    def fun_inside():
        nonlocal x
        x = 2
        print(x)
    fun_inside()  # 必须内部调用
    print(x)  # 1 # 2


fun_outside()


"""
====================   函数常用方法   ====================
参数类型注释：
作用：用于增加代码阅读性，python本身不会对类型控制
"""


def func(s_p: str, i_p: int, l_p: list, ls_p: list[int], d_p: dict = {'name': 'xiaoming'}):
    pass



