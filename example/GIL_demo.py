"""
GIL 全局解释器锁
是CPython中采用的一种机制，它确保同一时刻只有一个线程在执行Python字节码
除了io操作，单线程串行

如何绕过GIL：
1. 绕过CPython，使用JPython（Java实现的）等别的Python解释器
2. 把关键性能代码，放到别的语言（一般是C++）中实现
3. 多进程  from multiprocessing import Process
"""

from multiprocessing import Process
from threading import Thread, current_thread
import time


def task(proc_name: int):
    print("这是线程{}".format(proc_name))
    t = Thread(target=target(proc_name))
    t.start()


def target(proc_name):
    while True:
        print(f"{proc_name} - {current_thread().name} running")
        time.sleep(1)


if __name__ == "__main__":
    proc1 = Process(target=task, args=(1,))
    proc2 = Process(target=task, args=(2,))
    proc1.start()
    proc2.start()







