# @Author : Kql
# @Time : 2023/8/4 18:33
"""
进程池搭建
"""
from multiprocessing import Pool
from multiprocessing.dummy import freeze_support
from time import sleep, ctime


def worker(msg):
    sleep(2)
    print(ctime(), '---', msg)


if __name__ == '__main__':
    freeze_support()
    pool = Pool()
    for i in range(10):
        msg = "Tedu %d" % i
        pool.apply_async(func=worker, args=(msg,))
    pool.close()
    pool.join()
