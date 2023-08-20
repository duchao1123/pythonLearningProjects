"""
================== 课后作业 ==================
"""
'''
### 简答题
'''
from abc import ABC, abstractmethod


# （1）请写出单继承与多继承的语法格式?
class A(object):
    pass


class B(A, object):
    pass


#  （2）什么是方法重写，为什么要方法重写?
class P(object):

    def work(self):
        print('parents do work!')


class S(P):

    def work(self):
        print('sun do work!')


# 因为重写保证了编程的灵活性，也是多态的一种表现

'''
### 实操题
1.创建一个Animal（动物）基类，其中有一个run方法，输出`跑起来....`；
2.创建一个Horse（马）类继承于动物类，Horse类中不仅有run()方法还有eat()方法；
  2.1run方法输出 `跑起来....`
  2.2 eat 方法输出 `吃东西...`
'''


class Animal(object):

    def run(self):
        print('跑起来....')


class Horse(Animal):

    def run(self):
        print('Horse', end=' ')
        super().run()

    def eat(self):
        print('吃东西...')


'''
### 加强题
1.创建一个动物(Animal)的基类,其中有一个run方法, 输出`跑起来....`
2.创建一个Horse（马）类继承于动物类，Horse类中重写run方法，增加打印输出"`迈着矫健的步伐跑起来!!`"，同时实现eat方法, 输出 `吃东西...`
'''


class Horse1(Horse):

    def run(self):
        print('迈着矫健的步伐跑起来!!')


'''
### 综合训练
- 1.创建一个动物(Animal)的基类，其中有一个run方法, 输出`跑起来....`
- 2.创建一个Horse（马）类继承于动物类，Horse类中不仅有run方法还有eat方法
  - 2.1 run方法输出 `跑起来....`
  - 2.2 eat 方法输出 `吃东西...`
- 3.创建一个 SwiftHorse（千里马）类继承Horse类，初始化init方法name属性为千里马，
同时针对吃东西，SwiftHorse类中重写eat方法，增加打印输出"`一天可以吃一担粮食...`"
'''


class SwiftHorse(Horse):

    def __init__(self, name='千里马'):
        self.name = name

    def eat(self):
        print(f'{self.name} 一天可以吃一担粮食...')


'''
（7）综合训练：

定义一个`Person` 类,包含初始化 init 方法:
实例属性: 名字, name, 年龄, age
1. 记录由该类创建的对象的个数，创建一个对象，计数+1，删除一个对象，计数-1；
2. 定义一个方法，可以打印当前对象的个数；
3. 定义一个方法`show_info`, 输出以下信息
   ```
   这是一个 Person 类,谢谢查看!
   ```
4. 打印对象的时候，可以输出打印自己的名字和年龄
   ```python
   我的名字是 xxx, 年龄是 xxx
   ```
5. 定义一个方法 `study`, 输出以下信息
   ```python
   我叫 xxx, 我要好好学习
   ```
6. 操作步骤
   1.  调用`show_info `方法；
   2.  创建两个对象, 打印当前对象，并打印当前的对象个数；
   3.  分别使用两个对象调用`study`方法；
   4.  删除一个对象，打印输出当前的对象个数。
'''


class Person(object):

    _instance_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person._instance_count += 1

    @staticmethod
    def print_instance_count():
        print(f'实例个数为：{Person._instance_count}')

    def __del__(self):
        Person._instance_count -= 1


def show_info(p: Person):
    print(f'这是一个 Person(name: {p.name}, age: {p.age}),谢谢查看!')


def study(p: Person):
    print(f' 我叫 {p.name}, 我要好好学习')


'''
（8）编写一下多态场景

```pyhton
构建对象对战平台object_play
1 英雄一代战机（战斗力60）与敌军战机（战斗力70）对抗。英雄1代战机失败！
2 卧薪尝胆，英雄二代战机（战斗力80）出场！，战胜敌军战机！
3 对象对战平台object_play, 代码不发生变化的情况下, 完成多次战斗

```
'''


class Plane(ABC):

    __slots__ = ['combat']

    def fight_with(self, p):
        print(f'战斗{"胜利" if self.combat > p.combat else "失败"}！')


class Plane_L(Plane):

    def __init__(self):
        self.combat = 60


class Plane_H(Plane_L):

    def __init__(self):
        super().__init__()
        self.combat = 80


class Enemy(Plane):

    def __init__(self):
        self.combat = 70




'''
(9) 编写一下抽象类场景

```pyhton
国家部门制定了打印机标准
1、请抽象父类，制定标准：抽象printer，要求支持黑白打印(Black_white_printing)、彩色打印(color_printing)。
2、完成打印机hp、小米、佳能（canon）硬件入围；入围测试平台 make_test_printing(myobj:抽象类))
3、完成多态场景测试
```
'''



class Printer(ABC):

    @abstractmethod
    def print(self):
        pass


class HP_Printer(Printer):

    def print(self):
        print('HP 打印')


class XM_Printer(Printer):

    def print(self):
        print('XM 打印')


class JN_Printer(Printer):

    def print(self):
        print('JN 打印')


class YJ(object):

    def print(self):
        print('YJ 打印')


def make_test_printing(printable: Printer):
    printable.print()


if __name__ == "__main__":
    Horse().run()
    Horse1().run()
    SwiftHorse().run()
    SwiftHorse().eat()

    p0 = Person('aaa', 1)
    p1 = Person('bbb', 2)
    p2 = Person('ccc', 3)

    show_info(p0)
    show_info(p1)
    show_info(p2)

    Person.print_instance_count()
    del p1
    del p2
    Person.print_instance_count()

    pl = Plane_L()
    ph = Plane_H()
    en = Enemy()
    pl.fight_with(en)
    ph.fight_with(en)

    hp = HP_Printer()
    xm = XM_Printer()
    jn = JN_Printer()
    yj = YJ()
    make_test_printing(hp)
    make_test_printing(xm)
    make_test_printing(jn)
    make_test_printing(yj)















