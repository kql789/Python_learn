# @Author : Kql
# @Time : 2023/8/16 19:20
# @FileName : gevent_server.py
# @Blog ：https://blog.csdn.net/weixin_56175042
"""
基于协程的tcp并发
思路：1.将每个客户端处理设置为协程函数
2.让socket模块下的阻塞可以触发协程跳转
"""

import gevent
from gevent import monkey

monkey.patch_all()  # 执行脚本，修改socket阻塞
from socket import *


def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')


# 创建tcp套接字，使用默认参数——>tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_addr = ('127.0.0.1', 8888)
s.bind(server_addr)
s.listen(5)

while True:
    # 接收客户端请求
    c, addr = s.accept()
    print("Connetc from ", addr)
    # 处理具体的客户端请求
    gevent.spawn(handle, c)  # 协程方案
