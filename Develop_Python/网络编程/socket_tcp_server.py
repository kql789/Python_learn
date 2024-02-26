import socket

# 创建套接字对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址和端口
server_socket.bind(('127.0.0.1', 8888))

# 开始监听连接
server_socket.listen(5)

print("Server is listening on port 8888...")

# 接受客户端连接
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# 接收客户端数据并发送响应
client_data = client_socket.recv(1024)
print(f"Received: {client_data.decode()}")

client_socket.send(b"Hello, client!")

# 关闭连接
client_socket.close()
server_socket.close()
