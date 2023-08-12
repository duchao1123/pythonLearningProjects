"""
================== 课后作业 ==================
"""
'''
### 简答题
'''

# （1）举例说明生活中的案例：分别以面向过程、面向对象方式思考
"""
比如加油：
面向过程：
我 ->打开油箱盖 ->拔出油枪 ->插入油箱口 ->按下开关 ->加满拔出油箱 ->放回
面向对象：
我 -> 要求加油站服务人员（object）将油加满
"""

# （2）说一说类和对象是什么？
"""
类是对某一事物的抽象，对该事物属性和行为的封装
对象是类的实例
"""

'''
### 实操题
'''

# （1）定义一个手机类，能开机、能关机、可以拍照。


class Phone:

    def startup(self):
        pass

    def close(self):
        pass

    def take_photo(self):
        pass


# （2）定义一个电脑类，并给电脑添加品牌、价格等属性，同时电脑能用于编程、看视频。


class Computer:

    def __init__(self, brand: str, price: float):
        self.brand = brand
        self.price = price

    def code(self):
        pass

    def watch_videos(self):
        pass


# （3）尝试定义一个算法工程师类，同时使用`__init__()`
# 初始化岗位名称、薪资金额等属性，工作内容是每天码代码，
# 同时使用`__str__()`展示对象所拥有的所有信息。
class Farmer:

    def __init__(self):
        self.title = '工程师'
        self.salary = 1_000
        self.isDie = False
        self.hair_count = 100_000
        self.health_value = 100

    def work(self):
        while not self.isDie:
            print(self)
            print(f'醒醒起来敲代码.....')
            self.hair_count *= 0.9
            self.salary += 0.1
            self.health_value -= 1
            if self.health_value <= 0:
                self.isDie = True
                print('我嘎了～')

    def __str__(self):
        return f'Farmer 健康值: {self.health_value}'

# 1 定义类 Student
# 1.1 实现init魔法方法 current_weight
# 1.2 跑步方法
# 1.3 大吃大喝方法
# 2 实例化对象
# 3 调用锻炼实体


class Student:

    def __init__(self, current_weight: int):
        self.weight = current_weight

    def go_running(self):
        print('跑步')

    def eat(self):
        print('大吃大喝')

    def fitness(self):
        print('健身了,瘦二斤')
        self.weight -= 2


# 1 实例化类 SweetPotato
# init 函数 cook_time  cook_state condiments
# cook 地瓜被烤函数
# add_condiments 添加调料
# str魔法方法
# 2 用类实例化对象
# 不断的烤地瓜/添加调料, 打印对象状态
import time


class SweetPotato:

    states = ['生', '半生', '半熟', '熟']

    def __init__(self, cook_time):
        self.need_cook_time = cook_time
        self.current_cook_time = 0
        self.cook_state = self.check_status()

    def cook(self, condi):
        print(f'加了{condi}, 继续烤地瓜...')
        time.sleep(0.5)
        self.current_cook_time += 1
        self.cook_state = self.check_status()

    def check_status(self):
        progress = int(round(self.current_cook_time / self.need_cook_time, 2) * 100)
        if progress <= 30:
            return SweetPotato.states[0]
        elif progress <= 60:
            return SweetPotato.states[1]
        elif progress < 100:
            return SweetPotato.states[2]
        else:
            return SweetPotato.states[3]

    def __str__(self):
        return f'地瓜总烤了{self.current_cook_time}s, 当前的的状态: {self.cook_state}'


if __name__ == "__main__":
    # 3
    f = Farmer()
    f.work()

    # 4
    s = Student(120)
    s.fitness()

    # 5
    need_time = 30
    condiments = ['盐', '糖', '蜂蜜']
    sp = SweetPotato(need_time)
    print(sp)

    for i in range(need_time):
        condiment = condiments[i % len(condiments)]
        sp.cook(condiment)
        print(sp)











