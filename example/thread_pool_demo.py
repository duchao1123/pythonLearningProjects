"""
线程池
库：from concurrent.futures import ThreadPoolExecutor
直接创建线程的弊端：频繁的线程创建将会严重拖垮程序的执行的效率。临时创建一个线程需要耗费不小的代价
采用线程池技术： 预先创建几个空闲线程，在需要多线程来处理任务时，将任务分配给一个处于空闲状态的线程，
              该线程在执行完成后，将会回归空闲状态，而不是直接销毁
"""
from concurrent.futures import ThreadPoolExecutor, Future
import time


def task_handler(*args, **kwargs):
    if args:
        print(f'task_handler {args}')
    if kwargs:
        print(f'task_handler {kwargs}')
    return args[0]


def task_done_callback(f: Future):
    print(f'task_done_callback {f.result()}')


if __name__ == "__main__":
    """
    创建线程池
    def __init__(self, max_workers=None, thread_name_prefix='',
                 initializer=None, initargs=()):
    """
    executor = ThreadPoolExecutor(max_workers=5)

    task_list = [f't-{value}' for value in range(10)]
    for index, task in enumerate(task_list):
        '''
        def submit(*args, **kwargs):
        '''
        future = executor.submit(task_handler, index, task)
        '''
        def add_done_callback(self, fn):
        '''
        future.add_done_callback(task_done_callback)






























