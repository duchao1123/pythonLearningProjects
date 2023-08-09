"""
lock机制: 主动线性规划调用顺序，保证数据安全
库: from threading import Lock
threading.lock类来创建锁对象，一旦一个线程获得一个锁，会阻塞之后所有尝试获得该锁对象的线程，直到它被重新释
!!!! python的cpython解释器定义：单个进程内多线程不是并行运行，只是切时间片资源，随机选择单一线程运行，所以其实不存在脏数据问题
"""
from threading import Thread, Lock, current_thread
import datetime

int_common_value = 0
lock = Lock()


def target():
    max_times = 100
    global int_common_value
    while True:
        # 补充lock api, 若然作用不大
        # 加锁
        lock.acquire()
        try:
            print(f'{datetime.datetime.now()} --- {current_thread().name}, 持锁')
            if max_times == 0:
                # 注意终止条件时，也要释放锁，不然就死锁了！
                # 健壮性代码加 try.. finally ..
                print(f'{datetime.datetime.now()} --- {current_thread().name}, 结束！')
                break
            int_common_value += 1
            print(f'{datetime.datetime.now()} --- {current_thread().name}, value = [{int_common_value}]')
            max_times -= 1
        finally:
            # 释放锁
            lock.release()
            print(f'{datetime.datetime.now()} --- {current_thread().name}, 释放锁')


def exc_task(index):
    t = Thread(name=f"thread-{index}", target=target)
    t.start()


if __name__ == "__main__":
    '''
    试错案例：10个线程同时更改int_common_value，看int_common_value是否能干净增长
    '''
    for i in range(10):
        exc_task(i)















