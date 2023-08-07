"""
======================  描述符 和 property ============================
__get__
__set__
__delete__
"""


class DescClass:

    def __get__(self, instance, owner):
        print(f"owner[{owner}] 通过 instance{[instance]} 调用get")
        return instance._x

    def __set__(self, instance, value):
        print(f"instance{[instance]} 调用set value[{value}]")
        instance._x = value

    def __delete__(self, instance):
        print(f'instance[{instance}] 调用delete')
        del instance._x


class HostClass:
    desc = DescClass()

    def __init__(self, x):
        print(f'init -> x ={x}')
        self._x = x

    # def __delattr__(self, item):
    #     print(f'delattr item={item}')
    #     super.__delattr__(self, item)


h = HostClass(100)
print(h)
# <__main__.HostClass object at 0x7fee00164190>

print(h.desc)
# owner[<class '__main__.HostClass'>] 通过 instance[<__main__.HostClass object at 0x7fee00164190>] 调用get
# 100

h.desc = 10
# instance[<__main__.HostClass object at 0x7fe2e8124190>] 调用set value[10]

print(h.desc)
# owner[<class '__main__.HostClass'>] 通过 instance[<__main__.HostClass object at 0x7fc9a80a4190>] 调用get
# 10

del h.desc
# instance[<__main__.HostClass object at 0x7fbd60184190>] 调用delete

# print(h.desc)
# # AttributeError: 'HostClass' object has no attribute '_x'
print("=" * 50)

'''
上述方式存在不合理
1、使用描述符访问了隐藏变量_x，虽然可以实现，但是python不推荐

改进为property方式
将隐藏变量_x，封装出对应g、s、d方法，包裹到property给外部调用，调用赋值、获取、删除方法，相当于被property拦截转发给对应方法

而property由描述符实现
使用描述符实现自己的property
'''


class HostPropertyClass:

    def __init__(self, x):
        self._x = x

    def getx(self):
        print(f'getx ->')
        return self._x

    def setx(self, value):
        print(f'setx ->')
        self._x = value

    def delx(self):
        print(f'delx ->')
        del self._x

    x = property(getx, setx, delx)


h1 = HostPropertyClass(100)
print(h1.x)
# getx ->
# 100

h1.x = 10
# setx ->

print(h1.x)
# getx ->
# 10

del h1.x
# delx ->

# print(h1.x)
# # AttributeError: 'HostPropertyClass' object has no attribute '_x'

print("=" * 50)

'''
使用描述符实现自己的property
'''


class MyProperty:

    def __new__(cls, *args, **kwargs):
        print('__new__')
        super().__new__(cls)

    '''
    property作用是做方法调用转换，所以需要传入真正的方法
    '''

    def __init__(self, fget, fset, fdel):
        self._fg = fget
        self._fs = fset
        self._fd = fdel

    '''
    描述符必备三方法
    '''

    def __get__(self, instance, owner):
        self._fg(instance)  # 相当于fget()

    def __set__(self, instance, value):
        self._fs(instance, value)

    def __delete__(self, instance):
        self._fd(instance)


class HostMyPropertyClass:

    def __init__(self, x):
        # 定义出隐藏变量_x

        print(f'init set前 --------------')
        print(f'x = {self.x}')  # x = None 证明此时成员x还未进行初始化，所以下面的set操作不能被代理
        self._x = x

    '''
    真正实现
    '''

    def getx(self):
        return self._x

    def setx(self, x):
        self._x = x

    def delx(self):
        del self._x

    '''
    使用MyProperty
    '''
    x = MyProperty(getx, setx, delx)


hy = HostMyPropertyClass(100)
print(hy.x)  # None 为啥构造传入的100，没有打印？
print(hy.__dict__)  # {'_x': 100} 可以看到赋值已经生效
'''
1、
def __init__(self, x):
    print(f'init set前 --------------')
    print(f'x = {self.x}')  # x = None 证明此时成员x还未进行初始化，所以下面的set操作不能被代理
    self._x = x
2、x = MyProperty(getx, setx, delx) 一定需要写到定义了getx, setx, delx之后
'''

hy.x = 10
print(hy.x)

del hy.x
print("=" * 50)

'''
property 的作用是将内置方法代理给x，供外部调用
那存在魔法函数__getattr__、__setattr__、__delattr__，也可以拦截操作实现该功能。
俩者对比优劣势
可见
1、property简化了代码，易于阅读
2、property可以使用内置函数，使用装饰器的方式代替property构造过程，使得更为灵活
'''


class HostPropertyClass1:

    def __init__(self, x):
        self._x = x

    def __getattr__(self, item):
        print('__getattr__')
        if item == 'x':
            return self._x
        else:
            # return super().__getattr__(item)  # 此处有问题！本类没有继承，默认继承object，object没有__getattr__方法，所以会报错
            # AttributeError: 'super' object has no attribute '__getattr__'

            # 自己改一下，是不可以这样
            return self.__dict__.get(item, None)

    def __setattr__(self, key, value):
        print('__setattr__')
        if key == 'x':
            self._x = value
        else:
            return super().__setattr__(key, value)

    def __delattr__(self, item):
        print('__delattr__')
        if item == 'x':
            del self._x
        else:
            return super().__delattr__(item)


hp1 = HostPropertyClass1(100)
print(hp1.x)
# __getattr__
# 100

hp1.x = 10
# __setattr__   第一次：key == 'x'， 调用self._x = value
# __setattr__   第二次：key == '_x'  调用super().__setattr__(key, value)

print(hp1.x)
# __getattr__
# 10

del hp1.x
# __delattr__
# __delattr__
# 俩次调用的原因同set

print(hp1.y)
# __getattr__
# None

# dict_data = {}
# print(dict_data['key'])  # KeyError: 'key'
# 果然！ 获取字典不存在key的值，会报错
# 改用带default的方式
# print(dict_data.get('key', None))  # None
# 擦！！！！get定义的默认值不是关键字参数，写default=xxx又会报错。真心不严谨

print("=" * 50)

'''
property的格式是传入函数，代理函数执行，这个操作是'装饰器'
所以改为装饰器
同时property内置函数getter、setter、deleter可以再次简化指定property x的过程
'''


class HostPropertyClass2:

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        pass

    @x.getter
    def x(self):
        print(f'property gx ->')
        return self._x

    @x.setter
    def x(self, value):
        print(f'property sx ->')
        self._x = value

    @x.deleter
    def x(self):
        print(f'property dx ->')
        del self._x

    # x = property(getx, setx, delx)


hp2 = HostPropertyClass2(100)
print(hp2.x)
# property gx ->
# 100

hp2.x = 10
# property sx ->

print(hp2.x)
# property gx ->
# 10

del hp2.x
# property dx ->
print("=" * 50)

'''
装饰器转换过程
def property(func):
    def call_fun():
        return func()
    return call_fun

hp2.x = hp2.x() 
      = property(x) 
      = call_fun() & func = x 
      = x() = self._x
'''

'''
模拟实现
getter、setter、deleter

思路：
1、首先这三个是property内部的装饰器
'''


class MyProperty1:
    '''
    property作用是做方法调用转换，所以需要传入真正的方法
    '''

    def __init__(self, fget=None, fset=None, fdel=None):  # 注意！一定要给默认值，否则使用时需要传入参数
        self._fg = fget
        self._fs = fset
        self._fd = fdel
        print('__init__')

    def getter(self, func):
        print('getter ->')
        self._fg = func
        return self

    def setter(self, func):
        print('setter ->')
        self._fs = func
        return self

    def deleter(self, func):
        print('deleter ->')
        self._fd = func
        return self

    '''
    描述符必备三方法
    '''

    def __get__(self, instance, owner):
        print('__get__ ->')
        return self._fg(instance)

    def __set__(self, instance, value):
        print('__set__ ->')
        self._fs(instance, value)

    def __delete__(self, instance):
        print('__delete__ ->')
        self._fd(instance)


class HostMyPropertyClass1:

    def __init__(self):
        self._x = 0

    @MyProperty1
    def x(self):
        '''
        相当于定义了x = MyProperty1(self)
        '''
        print('@MyProperty1 ->')
        pass

    @x.getter
    def get(self):
        print('@x.getter ->')
        return self._x

    @x.setter
    def set(self, x):
        print('@x.setter ->')
        self._x = x

    @x.deleter
    def dele(self):
        print('@x.deleter ->')
        del self._x


hmp = HostMyPropertyClass1()
# 初始化类时， 初始化方法，会执行装饰器
# __init__
# getter ->
# setter ->
# deleter ->

hmp.x = 100
# __set__ ->
# @x.setter ->

print(hmp.__dict__)
# {'_x': 100}

print(hmp.x)
# __get__ ->
# @x.getter ->
# 100


# del hmp.x
print("=" * 50)

'''
property
分为数据类型和非数据类型
数据类型：任意实现 __set__ or __delete__
非数据类型：只实现 __get__
调用优先级：
数据类型 > 实例对象属性 > 非数据类型 > 类属性
__set_name__: 用于设置__dick__ 的key，而不是固定指定'x'
'''


class DataDescClass:

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)


class HostClass:

    d = DataDescClass()


hh = HostClass()
hh.d = 100
print(hh.d)  # 100












