"""
==================  ==================
"""


class CarF(object):

    @staticmethod
    def run():
        print('staticmethod')

    @classmethod
    def run(cls):
        print('classmethod')

    def run(self, val: int):
        print('membermethod with param')

    def run(self):
        print('membermethod')


class Car(CarF):

    def test(self):
        """
        期望调用staticmethod
        TypeError: run() missing 1 required positional argument: 'self'
        """
        CarF.run()

    def test1(self):
        """
        期望调用membermethod with param
        TypeError: run() takes 1 positional argument but 2 were given
        """
        CarF.run(self, 1)

    def test2(self):
        """
        期望调用membermethod
        membermethod
        """
        CarF.run(self)

    def run(self):
        print('runrunrun')

    def test3(self):
        """
        super() -> same as super(__class__, <first argument>)
        super(type) -> unbound super object
        super(type, obj) -> bound super object; requires isinstance(obj, type)
        super(type, type2) -> bound super object; requires issubclass(type2, type)
        Typical use to call a cooperative superclass method:
        class C(B):
            def meth(self, arg):
                super().meth(arg)
        This works for class methods too:
        class C(B):
            @classmethod
            def cmeth(cls, arg):
                super().cmeth(arg)

        # (copied from class doc)
        """
        s = super()
        print(type(s))  # <class 'super'>
        print(s)  # <super: <class 'Car'>, <Car object>>
        print(id(s))  # 140209208614272
        s.run()  # membermethod

        s1 = super(CarF)
        print(type(s1))  # <class 'super'>
        print(s1)  # <super: <class 'CarF'>, NULL>
        print(id(s1))  # 140209208614400
        s1.run()  # AttributeError: 'super' object has no attribute 'run'

        s2 = super(CarF, self)
        print(type(s2))  # <class 'super'>
        print(s2)  # <super: <class 'CarF'>, <Car object>>
        print(id(s2))  # 140209208614464
        s2.run()  # AttributeError: 'super' object has no attribute 'run'


if __name__ == '__main__':
    Car().test3()

    # 验证类中方法定义：
    # print(CarF.__dict__)
    '''
    {
        '__module__': '__main__', 
    --> 'run': <function CarF.run at 0x7fa450196790>, 
        '__dict__': <attribute '__dict__' of 'CarF' objects>, 
        '__weakref__': <attribute '__weakref__' of 'CarF' objects>, 
        '__doc__': None
    }
    结论：
    1、定义类时，同名方法只有一个，不论时静态方法、类方法、参数不同方法（没有重载概念）.
    '''

    # Car().test()
    # Car().test1()
    # Car().test2()
    '''
    结论：
    2、后写的方法会覆盖先写的
    '''

    '''
    所以：区分调用的是什么方法，看参数，类名也可以直接调用成员方法
    '''