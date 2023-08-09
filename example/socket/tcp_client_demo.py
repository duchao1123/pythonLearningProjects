"""
Socket  TCP
在Python 语言中创建 Socket 服务端程序，需要使用 socket 模块中的socket类。
创建 Socket 服务器程序的步骤如下：
（1） 创建 Socket 对象。
（2） 绑定端口号。
（3） 监听端口号。
（4） 等待客户端Socket 的连接。
（5） 读取客户端发送过来的数据。
（6） 向客户端发送数据。
（7） 关闭客户端Socket 连接。
（8） 关闭服务端Socket 连接。

导包：from socket import *
"""
from socket import *
from threading import Thread
from multiprocessing import Process, current_process


if __name__ == "__main__":
    print(f"启动客户端进程 -- {current_process().name}")
    c_socket = socket(AF_INET, SOCK_STREAM)
    """
    def connect(self, address: Union[_Address, bytes])
    """
    print(f"客户端开始连接服务端")
    c_socket.connect(("127.0.0.1", 8899))

    while True:
        data = c_socket.recv(1024)
        if data:
            answer = data.decode(encoding='gbk')
            print(f'服务端：{answer}')
            if answer == '88':
                break
            msg = input("我 > ")
            data = msg.encode('gbk')
            c_socket.send(data)
    # 关闭socket
    c_socket.close()
































