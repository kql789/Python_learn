# @Author : Kql
# @Time : 2023/8/7 15:01
"""
线程基本使用
步骤：基本等同Process
1.封装线程函数
2. 创建线程对象
3. 启动线程
4. 回收线程
"""
import threading
from time import sleep
import os

a = 1


def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(), "播放：黄河大合唱!")
    global a
    print("--->", a)
    a = 10000


# 创建线程对象
t = threading.Thread(target=music)
# 启动线程
t.start()

for i in range(4):
    sleep(1)
    print(os.getpid(), "播放：葫芦娃")
# 回收线程
t.join()
print("===>", a)
