# @Author : Kql
# @Time : 2023/8/11 18:08
"""
多进程网络并发模型
1. 创建监听套接字
2. 等待接收客户端请求
3. 客户端连接创建新的进程处理客户端请求
4. 原进程继续等待其他客户端连接。
"""
import os
from multiprocessing import Process
from socket import *
import signal

# 全局变量
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口重用
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

print("Listen the port 8888")


# 具体处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


while True:
    try:
        c, addr = s.accept()
        print("Connnet from ", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    # 创建子进程处理客户端事务
    p = Process(target=handle, args=(c))
    p.start()
    p.daemon = True  # 父进程结束则所有服务终止
