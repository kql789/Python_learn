# @Author : Kql
# @Time : 2023/7/26 14:49
from socket import *

s = socket()
s.connect(('127.0.0.1', 8888))

# 读取目标文件
f = open('/Users/user/Documents/photo/头像.jpg', 'rb')
while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)
f.close()
s.close()
