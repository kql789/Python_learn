# @Author : Kql
# @Time : 2023/7/26 10:36
"""
tcp客户端流程
"""
from socket import *

# 创建tcp套接字，使用默认参数——>tcp套接字
sockfd = socket()

# 服务端地址
server_addr = ('127.0.0.1', 8888)
# 连接服务器
sockfd.connect(server_addr)

while True:
    # 发送消息
    data = input("Msg>>")
    if not data:
        break
    # 将字符串转换成字节串
    sockfd.send(data.encode())

    data = sockfd.recv(1024)
    # 打印接受内容
    print("Server:", data.decode())

# 关闭套接字
sockfd.close()
