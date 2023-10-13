# @Author : Kql
# @Time : 2023/8/14 16:54
# @FileName : block_io.py
# 套接字非阻塞示例

from socket import *
from time import ctime, sleep

# 打开日志文件
f = open('photo/log.txt', 'a+')

# tcp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1', 8888))
sockfd.listen(5)

# 设置套接字为非阻塞
# sockfd.setblocking(False)

# 设置超时检测，注：超时检测与非阻塞不会同时使用
sockfd.settimeout(3)
while True:
    print("Waitting for connetc")
    # 没有客户端连接每隔3写一条日志
    try:
        connfd, addr = sockfd.accept()
    except (BlockingIOError, timeout) as e:
        sleep(3)
        f.write("%s :%s\n" % (ctime(), e))
    else:
        print("Connect from", addr)
        data = connfd.recv(1024).decode()
        print(data)
