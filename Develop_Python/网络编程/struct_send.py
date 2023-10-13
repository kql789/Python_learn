# Author :   Kql_unicorn
# Date   :   2023/7/30 10:41
from socket import *
import struct

# 数据格式定义
st = struct.Struct('i32sif')

# udp套接字
s = socket(AF_INET, SOCK_DGRAM)
addr = ('127.0.0.1', 8888)
while True:
    print("========================")
    id = int(input("ID:"))
    name = input("Name:").encode()
    age = int(input("Age:"))
    score = float(input("Score:"))
    # 打包数据发送
    data = st.pack(id, name, age, score)
    s.sendto(data, addr)
