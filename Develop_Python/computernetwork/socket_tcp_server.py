# @Author : Kql
# @Time : 2023/7/25 18:29
"""
socket_tcp.py tcp套接字服务端流程
注意：功能性代码，注重流程和函数使用
"""
import socket

# 创建套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置端口可以立即重用，绑定地址之前
sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定地址
sockfd.bind(('127.0.0.1', 9999))

# 设置监听
sockfd.listen(5)

while True:
    # 阻塞等待处理连接
    print("Waitting for connetc")
    try:
        connfd, addr = sockfd.accept()
        print("Connet from ", addr)  # 打印链接的客户端地址
    except KeyboardInterrupt:
        print("Server exit")
        break
    except Exception as e:
        print(e)
        continue
    while True:
        # 收发消息
        data = connfd.recv(1024)
        if not data:
            break
        print("收到：", data.decode())
        # 发送字节串
        n = connfd.send(b'Thanks...')
        print("发送%d字节" % n)

    connfd.close()
# 关闭套接字
sockfd.close()
