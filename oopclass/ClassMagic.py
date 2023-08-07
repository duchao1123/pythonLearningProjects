"""
=========================   class 魔法方法   =========================
__new__: 实例创建时，先调用__new__创建实例，然后调用__init__, 传递self（实例）
__del__: 类销毁前会调用__del__, 重写此方法，利用global或者闭包，可以实现self实例被持有不销毁
"""


# eg:
class AutoUpperStr(str):

    def __new__(cls, string: str):
        print('step: __new__')
        string = string.upper()
        return super().__new__(cls, string)

    def __init__(self, string: str):
        super().__init__()
        print('step: __init__')

    def __call__(self, *args, **kwargs):
        print('step: __call__')


'''
顺序
step: __new__
step: __init__
'''
data = AutoUpperStr("hello")
data1 = AutoUpperStr("hello1")
print(data)  # HELLO
data.x = 1
data.y = 2
data()  # step: __call__
print(type(data()))  # <class 'NoneType'>
print("=" * 50)  # HELLO


# 正常情况del了实例，类会被回收，如果想要不被回收


class NeverDieAutoUpperStr(AutoUpperStr):

    def __new__(cls, self_holder_func, string: str):
        return super().__new__(cls, string)

    def __init__(self, self_holder_func, string: str):
        super().__init__(string)
        self.self_holder_func = self_holder_func

    def __del__(self):
        # 将实例传给外界闭包持有
        self.self_holder_func(self)


def holder():
    instance = None

    def hold_instance(one=None):
        nonlocal instance  # nonlocal，让内部函数使用外部函数局部变量，而不是定义自己的局部变量
        if one:
            instance = one
        else:
            return instance
    return hold_instance


func = holder()
string_value = NeverDieAutoUpperStr(func, 'python')
print(string_value)      # PYTHON
print(id(string_value))  # 140434156686800
del string_value
origin_instance = func()
print(origin_instance)      # PYTHON
print(id(origin_instance))  # 140434156686800
# 做到了del但不销毁
