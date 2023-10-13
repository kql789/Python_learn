# Author :   Kql_unicorn
# Date   :   2023/7/30 10:39
"""
使用udp完成，客户端不断录入学生信息
将其发送到服务端，在服务端奖学生信息写入到一个文件中，
每个学生信息占一行。
信息格式： id name age score
"""
from socket import *
import struct

st = struct.Struct('i32sif')
# 创建套接字
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))
f = open('student.txt', 'a')

while True:
    data, addr = s.recvfrom(1024)
    data = st.unpack(data)
    info = "%d      %-10s      %d      %.1f" % data
    f.write(info)
    f.write("\n")
    f.flush()
    print("ip: {},写入成功".format(addr))
