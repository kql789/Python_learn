# Author :   Kql_unicorn
# Date   :   2023/7/31 22:14

import multiprocessing as mp
from time import sleep


def func():
    print("开始一个进程")
    sleep(5)
    print("子进程结束")

if __name__ == '__main__':

    p = mp.Process(target=func)
    p.start()  # 开始进程
    p.join()  # 回收进程
