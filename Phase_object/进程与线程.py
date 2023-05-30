from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


# 多进程
def download_task(filename):
    print('启动下载进程.进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main2():
    start = time()
    # process类创建进程，target为传入的函数，表示要执行的代码，args是一个元组，代表传递函数的参数
    p1 = Process(target=download_task, args=('Python从入门到放弃',))
    # 启动进程
    p1.start()
    p2 = Process(target=download_task, args=('数据结构与算法.pdf',))
    p2.start()
    # 等待进程执行结束
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main2()
