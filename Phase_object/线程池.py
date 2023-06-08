# @Author : Kql
# @Time : 2023/6/8 18:24
import threading
import time
import queue
import contextlib

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


'''
分析一下上面的代码：

实例化一个MyThreadPool的对象，在其内部建立了一个最多包含5个元素的阻塞队列，并一次性将5个Thread类型添加进去。
循环100次，每次从pool中获取一个thread类，利用该类，传递参数，实例化线程对象。
在run()方法中，每当任务完成后，又为pool添加一个thread类，保持队列中始终有5个thread类。
一定要分清楚，代码里各个变量表示的内容。t表示的是一个线程类，也就是threading.Thread，而obj才是正真的线程对象。
上面的例子是把线程类当做元素添加到队列内，从而实现的线程池。这种方法比较糙，每个线程使用后就被抛弃，并且一开始就将线程开到满，
因此性能较差。下面是一个相对好一点的例子，在这个例子中，队列里存放的不再是线程类，而是任务，
线程池也不是一开始就直接开辟所有线程，而是根据需要，逐步建立，直至池满。
'''

"""
一个基于thread和queue的线程池，以任务为队列元素，动态创建线程，重复利用线程，
通过close和terminate方法关闭线程池。
"""
# 创建空对象，用于停止线程
StopEvent = object()


def callback(status, result):
    '''
    根据需要进行回调函数，默认不执行。
    :param status： action函数的执行状态
    :param: result: action函数的返回值
    :return:
    '''
    pass


def action(thread_name, arg):
    '''
    真实的任务定义在这个函数里
    :param thread_name:执行该方法的线程名
    :param: arg: 改函数需要的参数
    :return:
    '''
    # 模拟改函数执行了0.1秒
    time.sleep(0.1)
    print("第%s个任务调用了线程 %s，并打印了这条信息！" % (arg + 1, thread_name))


class ThreadPool:
    def __init__(self, max_num, max_task_num=None):
        """
        初始化线程池
        :param max_num: 线程池最大线程数量
        :param max_task_num: 任务队列长度
        """
        # 如果提供了最大任务数的参数，则将队列的最大元素个数设置为这个值。
        if max_task_num:
            self.q = queue.Queue(max_task_num)
        else:
            # 默认队列可接受无限多个的任务
            self.q = queue.Queue()
        # 设置线程池最多可实例化的线程数
        self.max_num = max_num
        # 任务取消标识
        self.cancel = False
        # 任务中断标识
        self.terminal = False
        # 已实例化的线程列表
        self.generate_list = []
        # 处于空闲状态的列表
        self.free_list = []

    def put(self, func, args, callback=None):
        # 判定任务标识，看看任务是否取消了
        if self.cancel:
            return
        # 如果没有空闲的线程，并且已创建的线程数量小于预定义的最大线程数，则创建新线程
        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            self.generate_thread()
        #     构造任务参数元组，分别是调用的函数、改函数的参数，回调函数
        w = (func, args, callback)
        self.q.put(w)

    def generate_thread(self):
        '''创建一个线程'''
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        """
        循环去获取任务函数并执行任务函数。在正常情况下，每个线程都保存生存状态，
        直到获取线程终止的flag。
        """
        # 获取当前线程的名字
        current_thread = threading.current_thread().getName()
        # 将当前线程的名字加入到已实例化的线程列表中
        self.generate_list.append(current_thread)
        # 从人物队列获取一个任务
        event = self.q.get()
        # 让获取的任务不是终止线程的标识对象时
        while event != StopEvent:
            # 解析任务中封装的三个参数
            func, arguments, callback = event
            # 抓取异常，防止线程因为异常退出
            try:
                # 正常执行任务函数
                result = func(current_thread, *arguments)
                success = True
            except Exception as e:
                # 当任务执行过程中弹出异常
                result = None
                success = False
            # 如果有指定的回调函数
            if callback is not None:
                # 执行回调函数，并抓取异常
                try:
                    callback(success, result)
                except Exception as e:
                    pass
            # 当某个县城正常执行完一个任务时，先执行work_state方法
            with self.worker_state(self.free_list, current_thread):
                # 如果强制关闭线程的flag开启，则传入一个StopEvent元素
                if self.terminal:
                    event = StopEvent
                # 否则获取一个正常的任务，并回调work_state方法的yield语句
                else:
                    # 从这里开始又是一个正常的任务循环
                    event = self.q.get()
        else:
            # 一旦发现任务是个终止线程的标识元素，将线程从已经创建的线程列表中删除。
            self.generate_list.remove(current_thread)

    def close(self):
        """
        执行完所有的任务后，让所有线程都停止的方法
        """
        # 设置flag
        self.cancel = True
        # 计算已创建线程列表中线程的个数
        # 然后往任务队列里推送相同数量的终止线程的标识元素
        full_size = len(self.generate_list)
        while full_size:
            self.q.put(StopEvent)
            full_size -= 1

    def terminate(self):
        '''在任务执行过程中，终止线程，提前退出'''
        self.terminal = True
        # 强制性的停止线程
        while self.generate_list:
            self.q.put(StopEvent)

    # 该装饰器用于管理上下文
    @contextlib.contextmanager
    def worker_state(self, state_list, worker_thread):
        '''用于记录空闲的线程，或从空闲的列表中取出线程处理任务'''
        # 将当前线程，添加到空闲线程列表中
        state_list.append(worker_thread)
        # 捕获异常
        try:
            # 再次等待
            yield
        finally:
            # 将线程从空闲列表中移除
            state_list.remove(worker_thread)


# 调用方式
if __name__ == '__main__':
    # 创建一个最多包含5个线程的线程池
    pool = ThreadPool(5)
    # 创建100个任务，让线程池进行处理
    for i in range(100):
        pool.put(action, (i,), callback)
    # 等待一定时间，让线程执行任务
    time.sleep(3)
    print("-" * 50)
    print("任务停止之前线程池中有%s个线程，空闲的线程有%s个!"
          % (len(pool.generate_list), len(pool.free_list)))
    pool.close()
    print("任务执行完毕，正常退出")
