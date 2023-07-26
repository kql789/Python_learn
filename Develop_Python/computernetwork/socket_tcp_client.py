# @Author : Kql
# @Time : 2023/7/26 10:36
"""
tcp客户端流程
"""
import socket

# 创建tcp套接字，使用默认参数——>tcp套接字
sockfd = socket()

# 服务端地址
server_addr = ('127.0.0.1', 8888)
# 连接服务器
sockfd.connect(server_addr)

