# @Author : Kql
# @Time : 2023/6/8 16:51
import threading
import time

'''
信号Semaphore:
类名：BoundedSemaphore。这种锁允许一定数量的线程同时更改数据，它不是互斥锁。比如地铁安检，排队人很多，
工作人员只允许一定数量的人进入安检区，其它的人继续排队。
'''


def run(n, se):
    se.acquire()
    print("run the thread:%s" % n)
    time.sleep(1)
    se.release()


# 设置允许5个线程同时运行
semaphore = threading.BoundedSemaphore(5)
for i in range(20):
    t = threading.Thread(target=run, args=(i, semaphore))
    t.start()
    # 运行后，可以看到5个一批的线程被放行。
