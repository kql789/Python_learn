# Author :   Kql_unicorn
# Date   :   2023/7/31 21:49

"""
僵尸进程——创建子进程
"""
import os
from time import sleep


def f1():
    for i in range(3):
        sleep(2)
        print("写代码!")


def f2():
    for i in range(2):
        sleep(4)
        print("测试代码")


pid = os.fork()
if pid == 0:
    p = os.fork()
    if p == 0:
        f1()
    else:
        os._exit(0)
else:
    os.wait()
    f2()
