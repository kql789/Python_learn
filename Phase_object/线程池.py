# @Author : Kql
# @Time : 2023/6/8 18:24
import threading
import time
import queue

'''
在使用多线程处理任务时也不是线程越多越好。因为在切换线程的时候，需要切换上下文环境，线程很多的时候，依然会造成CPU的大量开销。
为解决这个问题，线程池的概念被提出来了。

预先创建好一个数量较为优化的线程组，在需要的时候立刻能够使用，就形成了线程池。
在Python中，没有内置的较好的线程池模块，需要自己实现或使用第三方模块。
'''


class MyThreadPool:
    def __init__(self, maxsize=5):
        self.maxsize = maxsize
        self._pool = queue.Queue(maxsize)  # 使用queue队列，创建一个线程池
        for _ in range(maxsize):
            self._pool.put(threading.Thread)

    def get_thread(self):
        return self._pool.get()

    def add_thread(self):
        self._pool.put(threading.Thread)


def run(i, pool):
    print('执行任务', i)
    time.sleep(1)
    pool.add_thread()  # 执行完毕后，再向线程池中添加一个线程类


def test1():
    pool = MyThreadPool(5)  # 设定线程池中最多只能有5个线程类
    for i in range(20):
        t = pool.get_thread()  # 每个t都是一个线程类
        obj = t(target=run, args=(i, pool))  # 这里的obj才是正真的线程对象
        obj.start()
    print("活动的子线程数： ", threading.active_count() - 1)
if __name__ == '__main__':
    test1()