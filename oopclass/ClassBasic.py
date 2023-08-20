"""
=========================   class对象   =========================
python函数可以不指定类型，所以只要传入参数对象具备函数内调用的方法，就可以正常运行，不像java严苛
eg：
def work(x):
    x.do()

class Singer:
   def work(self):
        print('唱歌')

class Farmer:
   def work(self):
       print('搬砖')

class Pingtouge:
   def work(self):
       print('干仗')

work(Singer())
work(Farmer())
work(Pingtouge())
不必在乎调用work参数是谁，也不像java 有接口控制共同能力，只要具备work函数就行

抽象类
导包：from abc import ABC, abstractmethod
定义抽象类 class xxx(ABC)
定义抽象方法：@abstractmethod
"""


class Parent:
    '''
    构造
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def work(self):
        pass


"""
继承
"""


class A(Parent):
    '''
    构造
    super遵循mro法制
    '''

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    '''
    多态
    重写父类方法
    '''

    def work(self):
        print("A do work")


class B(Parent):
    '''
    多态
    重写父类方法
    '''

    def work(self):
        print("B do wirk")


class C:
    '''
    组合
    一个类中引用别的类
    '''
    a = A(1, 2, 3)
    b = B(4, 4)

    '''
    封装
    并没有继承A，B，Parent； 所以work属于自己定义的方法，把执行流程放到一个函数中叫封装
    '''

    def work(self):
        '''
        绑定对象
        为什么需要self，因为类可以创建多个实例，self可以绑定对应具体实例
        可以用isinstan判断是否是类的实例
        :return:
        '''
        self.a.work()
        self.b.work()


c = C()
c.work()


class D(A, B):
    pass


d = D(1, 2, 3)
d.work()  # A do work
'''
python可以多继承
d继承A，也继承B，调用work为什么会打印'A do work'？
因为MRO原则，查找调用顺序遵循MRO
查询MRO：
mro()
__mro__  自省方式
'''
print(D.mro())
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Parent'>, <class 'object'>)


"""
=========================   mixin   =========================
混入例子，
一般混入都是
"""

"""
=========================   slots   =========================
类内部属性存储是依赖字典，可以查看__dick__, 字典的特征是方便存取，非常灵活。但是其实是用空间还的时间，
所以python也提供了限制类大小的__slots__ = []
slots一经定义，就不能定义其他属性，也不能添加新的属性，大小是确定下来的。用灵活性换了空间
父类定义的slots， 不影响子类创建自己的属性dick，同时可以被子类调用
"""


class Cat:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.z = z  # AttributeError: 'Cat' object has no attribute 'z'


cat = Cat(1, 2)
# print(cat.__dict__)  # AttributeError: 'Cat' object has no attribute '__dict__'
print(cat.__slots__)  # ['x', 'y']
print(cat.x)
print(cat.y)


class LittleCat(Cat):
    pass


lc = LittleCat(0, 0)
print(lc.__dict__)
print(lc.__slots__)
print(lc.x)
print(lc.y)
lc.z = 8
print(lc.__dict__)  # {'z': 8}
lc.x = 9
print(lc.x)
