# @Author : Kql
# @Time : 2023/8/15 16:06
# @FileName : poll_server.py
# @Blog ：https://blog.csdn.net/weixin_56175042
"""
重点代码：
思路：IO多路复用实现并发
    建立fileno——>io对象字典用于IO查找
"""

from socket import *
from select import *

# 创建套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(5)
# 创建poll对象
p = poll()
# 建立查找字典，通过IO的fileno找到IO对象
# 始终跟register的IO保持一致
fdmap = {s.fileno(): s}

# 关注s
p.register(s, POLLIN | POLLERR)

while True:
    events = p.poll()
    # 循环遍历列表，查看哪个IO就绪，进行处理
    for fd, event in events:
        # 区分哪个IO就绪
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from", addr)
            # 关注客户端连接套接字
            p.register(c, POLLIN | POLLERR)
            fdmap[c.fileno()] = c  # 维护字典
        elif event & POLLIN:  # 判断是否为POLLIN就绪
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)  # 取消关注
                fdmap[fd].close()
                del fdmap[fd]  # 从字典删除
                continue
            print("Received:", data)
            fdmap[fd].send(b"OK")
