# @Author : Kql

# @Time : 2023/7/26 18:27
"""
udp客户端流程,
"""
from socket import *

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 服务器地址
addr = ('127.0.0.1', 8888)

# 循环收发消息
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(), addr)
    msg, addrd = sockfd.recvfrom(1024)
    print("From server", msg.decode())

# 关闭套接字
sockfd.close()
