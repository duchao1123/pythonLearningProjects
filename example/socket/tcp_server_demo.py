from socket import *
from threading import Thread
from multiprocessing import Process, current_process


answers = {
    '你好': '你好',
    '在干嘛': '在搬砖',
    '白日依山尽': '黄河入海流',
    '欲穷千里目': '更上一层楼',
    'abc': 'def',
    '123': '456',
    '88': '88',
}


def answer_instance(*, c_s: socket, c_a):
    while True:
        data = c_s.recv(1024)
        if data:
            msg = data.decode(encoding='gbk')
            print(f'{c_a[1]}：{msg}')
            answer = answers.get(msg, '我回答不了你～')
            print(f'我：{answer}')
            c_s.send(answer.encode('gbk'))
            if msg == '88':
                break


def startup_server():
    print(f"启动服务端进程 -- {current_process().name}")
    """
    def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
    family的参数值有：AF_UNIX 或者 AF_INET ； AF 表示ADDRESS FAMILY 地址族，AF_INET（又称 PF_INET）是 IPv4 网络协议的套接字类型；而AF_UNIX 则是 Unix 系统本地通信
    type : 套接字类型可以根据是面向连接的还是非连接分为 SOCK_STREAM 或 SOCK_DGRAM ；
    protocol : 一般不填，默认为0。
    """
    # 创建socket
    s_socket = socket(AF_INET, SOCK_STREAM)
    '''
    def bind(self, address: Union[_Address, bytes])
    '''
    # 绑定地址
    s_socket.bind(("127.0.0.1", 8899))
    '''
    def listen(self, __backlog: int = ...)
    '''
    # 设置监听数
    s_socket.listen(5)
    '''
    接收信息
    Wait for an incoming connection.  Return a new socket
    representing the connection, and the address of the client.
    '''
    # 开始接收数据
    print("服务端就绪，等待连接")
    try:
        while True:
            c_socket, c_address = s_socket.accept()
            print(f"有客户端[{c_address[1]}]建立连接")
            hello = '你好'
            print(f'我：{hello}')
            c_socket.send(hello.encode('gbk'))
            Thread(target=answer_instance(c_s=c_socket, c_a=c_address), name=f'for-{c_address[1]}').start()
    finally:
        # 关闭socket
        s_socket.close()


if __name__ == "__main__":
    Process(target=startup_server, name='server').start()



