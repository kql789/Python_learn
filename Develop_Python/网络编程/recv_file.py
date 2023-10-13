# @Author : Kql
# @Time : 2023/7/26 14:30
# 将一个文件从客户端发送到服务端保存。注：文件可能是文本类型也可能是二进制文件。

from socket import *

s = socket()
s.bind(('127.0.0.1', 8888))
s.listen(5)
c, addr = s.accept()
print("Connect from ", addr)

# 接受思路：1. wb写打开新文件
# 2. recv内容 write文件
# 打开文件
f = open('./photo/gg.jpg', 'wb')

while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)
f.close()
c.close()
s.close()
