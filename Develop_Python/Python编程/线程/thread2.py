# @Author : Kql
# @Time : 2023/8/7 15:35

"""
线程传参

"""
from threading import Thread
from time import sleep


# 含有参数的线程函数
def func(sec, name):
    print("线程函数传参")
    sleep(sec)
    print("%s 执行完毕" % name)


# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=func, args=(2,), kwargs={'name': 'T%s' % i})
    jobs.append(t)  # 存储线程对象
    t.start()
for i in jobs:
    i.join()
