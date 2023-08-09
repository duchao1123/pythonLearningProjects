"""
python 线程
库：threading
守护线程作用：将子线程设置为守护线程，此时主线程任务一旦完成退出，所有子线程将会和主线程一起结束（就算子线程没有执行完也会退出）
"""
from threading import Thread, current_thread
import time
import datetime


def print_current_thread(c_thread=current_thread()):
    # print(type(c_thread))  # <class 'threading._MainThread'>
    # print(c_thread.__dict__)
    """
    {'_target': None, '_name': 'MainThread', '_args': (), '_kwargs': {}, '_daemonic': False,
    '_ident': 4453959168, '_native_id': 617322, '_tstate_lock': <locked _thread.lock object at 0x7f8700138840>,
    '_started': <threading.Event object at 0x7f8700138610>, '_is_stopped': False, '_initialized': True,
    '_stderr': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>,
    '_invoke_excepthook': <function _make_invoke_excepthook.<locals>.invoke_excepthook at 0x7f870013fdc0>}
    """
    print(f'当前线程: {c_thread.name}, 是否是守护线程: {c_thread.daemon}, '
          f'ident: {c_thread.ident}, native_id: {c_thread.native_id}')
    # 当前线程: MainThread, 是否是守护线程: False, ident: 4453959168, native_id: 617322


def create_thread(group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
    """
    创建线程
    :param group: 线程组
    :param target: run方法
    :param name: 线程名称
    :param args: 传给实例的参数
    :param kwargs: 传给实例的参数
    :param daemon: 是否是守护线程
    """
    thread = Thread(group, target, name, args, kwargs, daemon=daemon)
    return thread


def start_thread(thread: Thread):
    """
    启动线程
    """
    thread.start()


def block_thread(thread: Thread):
    """
    使用join阻塞线程
    thread.join(timeout=5) 限时阻塞，如果时间到了，join进来的线程即使没有执行完成，外部线程也会恢复执行，
    join线程也会继续执行，直到完成
    """
    # thread.join()
    thread.join(timeout=5)


def kill_thread():
    """
    使用全局flag，终止线程内循环条件，从而退出线程
    杀死线程之前，请一定慎重，锁资源并不会因为当前线程的退出而释放，可能会成为典型的死锁场景
    """


def target(*args, **kwargs):
    """
    字典数据需要封包 **kwargs
    self._target(*self._args, **self._kwargs)
    TypeError: target() got an unexpected keyword argument 'arg0'
    """
    # print(args)
    # print(kwargs)
    # # 看target运行在什么线程
    # c_thread = current_thread()
    # print_current_thread(c_thread)
    global max_size
    while True:
        if max_size == 0:
            break
        print(f"{datetime.datetime.now()} --- {current_thread().name} is running....")
        max_size -= 1
        time.sleep(0.5)


"""
线程间通信
1. 直接使用全局变量虽然可行，但是资源的并发读写会引来线程安全问题，解决办法：
线程锁 @lock_demo
同步队列 @queue_demo
"""
max_size = 30
max_size_main = 30


if __name__ == "__main__":
    # print_current_thread()
    new_thread = create_thread(None, target, "myThread-0", (1, 2, 3), {"arg0": 'haha', "arg1": 10})
    # 伴随主线程退出
    new_thread.setDaemon(True)
    print_current_thread(new_thread)
    print(new_thread.__dict__)
    '''
    {... '_args': (1, 2, 3), '_kwargs': {'arg': 'haha', 'arg1': 10}, ...}
    '''
    # <class 'threading.Thread'>
    # 当前线程: myThread-0, 是否是守护线程: False, ident: None, native_id: None

    # 传入参数获取
    # 方案一：不推荐
    print(new_thread.__dict__['_args'])  # (1, 2, 3)
    # 方案二：参数都带入了target函数中
    start_thread(new_thread)
    # 启动myThread-0，观看打印
    # (1, 2, 3)
    # {'arg0': 'haha', 'arg1': 10}
    # <class 'threading.Thread'>
    # 当前线程: myThread - 0, 是否是守护线程: False, ident: 123145393958912, native_id: 632632
    # 发现差异，thread没有启动时ident: None, native_id: None， 启动后ident: 123145393958912, native_id: 632632
    # 原理：内核thread启动后赋值

    '''
    join new_thread，阻塞当前调用线程（主线程），等待new_thread执行完成后，才能继续执行
    '''
    # block_thread(new_thread)

    while True:
        if max_size_main == 0:
            break
        if max_size_main == max_size_main - 1:
            # 比上面调用更直观，在主线程任务loop时，join
            # 但是得注意，new_thread线程是否活跃；并且new_thread start后，target有可能已经获取到资源进行运行了
            block_thread(new_thread)
        print(f"{datetime.datetime.now()} --- {current_thread().name} is running....")
        max_size_main -= 1
        time.sleep(0.5)






