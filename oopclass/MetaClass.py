"""
===============================  元类  ================================
__new__  : 实现类定义时调用
__init__ : 实现类定义时调用
__call__ : 实现类创建实例时调用
"""

# 需求，使用元类限制实例创建


class LimitClass(type):  # 元类必须继承type， 元类的元类type

    def __new__(mcs, *args, **kwargs):
        print('__new__')
        return type.__new__(mcs, *args, **kwargs)

    def __init__(cls, *args, **kwargs):
        print('__init__')
        cls.hasinstance = False
        type.__init__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.hasinstance:
            raise TypeError('只能创建一个实例')
        cls.hasinstance = True


class UseClass(metaclass=LimitClass):

    pass


u1 = UseClass()


class UseClass1(metaclass=LimitClass):

    pass


# u2 = UseClass()


# 需求：使用元类实现单例


class SingleInstanceClass(type):

    def __init__(cls, *args, **kwargs):
        # 定义实例
        cls._instance = None
        # 注意调用type的参数
        # TypeError: type.__init__() takes 1 or 3 arguments
        type.__init__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            # 注意调用type的参数
            cls._instance = type.__call__(cls, *args, **kwargs)
        return cls._instance


class SingleInstanceImpl(metaclass=SingleInstanceClass):
    pass


instance0 = SingleInstanceImpl()
instance1 = SingleInstanceImpl()

print(instance0 == instance1)  # True














