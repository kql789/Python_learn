# @Author : Kql
# @Time : 2023/7/25 18:29
"""
socket_tcp.py tcp套接字服务端流程
注意：功能性代码，注重流程和函数使用
"""
import socket

# 创建套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('127.0.0.1', 8888))

# 设置监听
sockfd.listen(5)

# 阻塞等待处理连接
print("Waitting for connetc")
connfd, addr = sockfd.accept()
print("Connet from ", addr)  # 打印链接的客户端地址

# 收发消息
data = connfd.recv(1024)
print("收到：", data)
# 发送字节串
n = connfd.send(b'Thanks...')
print("发送%d字节" % n)

# 关闭套接字
connfd.close()
sockfd.close()