# @Author : Kql
# @Time : 2023/8/16 19:00
# @FileName : gevent_test.py
# @Blog ：https://blog.csdn.net/weixin_56175042

import gevent
from gevent import monkey

monkey.patch_time()
from time import sleep


def func1(a, b):
    print("Runing func1 ....", a, b)
    sleep(2)
    print("func1 again ....")


def bar():
    print("Runing bar ....")
    sleep(3)
    print("bat again ....")


# 生成协程对象
f = gevent.spawn(func1, 1, 2)
g = gevent.spawn(bar)
gevent.joinall([f, g])  # 阻塞等待两个协程执行完毕
