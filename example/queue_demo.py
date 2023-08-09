"""
lock机制: 主动线性规划调用顺序，保证数据安全
库:
from queue import Queue                  先进先出队列
from queue import LifoQueue              先进后出队列
from queue import PriorityQueue          优先级队列
from queue import SimpleQueue            无界的先进先出队列, 简单实现，缺少Queue中的任务跟踪等高级功能
FIFO:
first in first out 先进先出
"""
from queue import Queue
from threading import Thread
import time
import random

'''
Queue(maxsize=5)  # 创建一个FIFO队列，并制定队列大小，若maxsize被指定为小于等于0，则队列无限大
Queue.qsize() # 返回队列的大致大小，注意并不是确切值，所以不能被用来当做后续线程是否会被阻塞的依据
Queue.empty() # 判断队列为空是否成立，同样不能作为阻塞依据
Queue.full()  # 判断队列为满是否成立，同样不能作为阻塞依据
Queue.put(item, block=True, timeout=None) 
# 投放元素进入队列，block为True表示如果队列满了投放失败，将阻塞该线程，timeout可用来设置线程阻塞的时间长短（秒）；
# 注意，如果block为False，如果队列为满，则将直接引发Full异常，timeout将被忽略（在外界用try处理异常即可）

Queue.put_nowait(item) # 相当于put(item, block=False)
Queue.get(block=True, timeout=False) # 从队列中取出元素，block为False而队列为空时，会引发Empty异常
Queue.get_nowait() # 相当于get(block=False)
Queue.task_done() # 每个线程使用get方法从队列中获取一个元素，该线程通过调用task_done()表示该元素已处理完成。
Queue.join() # 阻塞至队列中所有元素都被处理完成，即队列中所有元素都已被接收，且接收线程全已调用task_done()。
'''

'''
demo：生产消费者模式
p: 一直生产商品，如果存在未消费商品，就停止生产
c: 一直消费商品，如果不存在待消费商品，就停止等待商品
'''


class Product:

    def __init__(self, queue):
        self.q = queue
        self.t = None
        self.product_count = 0

    def loop_produce(self):
        while True:
            if self.product_count >= 50:
                print('全部生产完成，停止生产')
                break
            # 模拟生产
            time.sleep(1)
            # 因为python单核，生产随机数个商品，模拟并行
            # 期望出现，本次生产数 + 未消费数 》 max，出现阻塞。
            # 而消费线程进行消费后，恢复上架
            for i in range(1, random.randint(1, 5)):
                self.product_count += 1
                if self.product_count > 50:
                    print('全部生产完成，停止生产')
                    break
                # 上架商品，block=True，如果在售商品达到最大值，就阻塞等待
                self.q.put(f"商品 - {self.product_count}", block=True)
                print(f'上架了：商品 - {self.product_count}')

    def start_produce(self):
        self.t = Thread(target=self.loop_produce, name="product", daemon=False)
        self.t.start()


class Consumer:

    def __init__(self, queue):
        self.q = queue
        self.t = None
        self.consume_count = 0

    def loop_consume(self):
        while True:
            if self.consume_count == 50:
                print('全部消费完成，停止消费')
                break
            # 获取商品，block=True，如果没有商品，就阻塞等待
            prod = self.q.get(block=True)
            print(f'消费了：{prod}')
            self.consume_count += 1
            self.q.task_done()

    def start_consume(self):
        self.t = Thread(target=self.loop_consume, name="consumer", daemon=False)
        self.t.start()


if __name__ == "__main__":
    # 创建任务队列, maxsize定义同时最多只能有5个商品在售
    q = Queue(maxsize=5)
    # 创建生产者
    p = Product(q)
    # 创建消费者
    c = Consumer(q)
    # 开始生产消费轮询
    p.start_produce()
    c.start_consume()













