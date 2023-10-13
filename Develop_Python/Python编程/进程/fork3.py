# Author :   Kql_unicorn
# Date   :   2023/7/31 22:29
"""
multiprocessing 创建多线程
"""
import os
import multiprocessing as mp
from time import sleep


def f1():
    sleep(3)
    print("吃饭")
    print(os.getppid(), '--', os.getpid())


def f2():
    sleep(3)
    print("睡觉")
    print(os.getppid(), '--', os.getpid())


def f3():
    sleep(3)
    print("打豆豆")
    print(os.getppid(), '--', os.getpid())

if __name__ == '__main__':

    jobs = []
    th = [f1, f2, f3]
    for t in th:
        p = mp.Process(target=t)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()
