# @Author : Kql
# @Time : 2023/6/8 15:41
import threading
import time

'''
hreading模块包含下面的类：
Thread：基本线程类
Lock：互斥锁
RLock：可重入锁，使单一进程再次获得已持有的锁(递归锁)
Condition：条件锁，使得一个线程等待另一个线程满足特定条件，比如改变状态或某个值。
Semaphore：信号锁。为线程间共享的有限资源提供一个”计数器”，如果没有可用资源则会被阻塞。
Event：事件锁，任意数量的线程等待某个事件的发生，在该事件发生后所有线程被激活
Timer：一种计时器
Barrier：Python3.2新增的“阻碍”类，必须达到指定数量的线程后才可以继续执行。
'''
# 1. 多线程
'''
有两种方式来创建线程：一种是继承Thread类，并重写它的run()方法；
另一种是在实例化threading.Thread对象的时候，将线程要执行的任务函数作为参数传入线程。
'''


# 方法1
class MyThread(threading.Thread):
    def __init__(self, thread_name):
        # 注意：一定要显式的调用父类的初始化函数。
        super(MyThread, self).__init__(name=thread_name)

    def run(self):
        print("%s正在运行中......" % self.name)


def test():
    for i in range(10):
        MyThread('thread' + str(i)).start()


# 方法2
def show(arg):
    time.sleep(1)
    print('thread ' + str(arg) + " running....")


'''
对于Thread类，它的定义如下：
threading.Thread(self, group=None, target=None, name=None,
     args=(), kwargs=None, *, daemon=None)
参数group是预留的，用于将来扩展；
参数target是一个可调用对象，在线程启动后执行；
参数name是线程的名字。默认值为“Thread-N“，N是一个数字。
参数args和kwargs分别表示调用target时的参数列表和关键字参数。
'''


def test2():
    for i in range(10):
        t = threading.Thread(target=show, args=(i,))
        t.start()


# 在多线程执行过程中，有一个特点要注意，那就是每个线程各执行各的任务，不等待其它的线程，自顾自的完成自己的任务.
# 有时候我们希望主线程等等子线程，不要“埋头往前跑”。那要怎么办？使用join()方法！
# join方法，使其子线程进行等待
def dowaiting():
    print('start waiting:', time.strftime('%H:%M:%S'))
    time.sleep(3)
    print('stop waiting', time.strftime('%H:%M:%S'))


def test3():
    t = threading.Thread(target=dowaiting)
    t.start()
    # 确保线程已经启动
    print('start join')
    t.join()
    print('end join')
    time.sleep(1)


# 方法2 使用setDaemon(True) 把所有的子线程变成主线程的守护线程 当主线程执行完毕后，守护子线程也会随之结束，整个程序也跟着退出
def run():
    # 返回当前线程,current_thread;获取线程名字，getName;
    print(threading.current_thread().getName(), "开始工作")
    time.sleep(2)  # 子线程停2s
    print("子线程工作完毕")


def test4():
    for i in range(3):
        t = threading.Thread(target=run)
        t.setDaemon(True)  # 把子线程设置为守护线程，必须在start之前设置
        t.start()
    time.sleep(1)
    print('主线程结束了')
    # 输出活跃的线程数
    print(threading.active_count())


# 自定义线程类 对于threading模块中的Thread类，本质上是执行了它的run方法。因此可以自定义线程类，让它继承Thread类，然后重写run方法。

class Mythreading(threading.Thread):
    def __init__(self, func, arg):
        super(Mythreading, self).__init__()
        self.func = func
        self.arg = arg

    def run(self):
        self.func(self.arg)


def my_func(args):
    '''可以把让线程做的任何事放在这里'''
    for i in range(2):
        print('start' + str(i))
        time.sleep(1)


def test5():
    obj = Mythreading(my_func, 123)
    obj.start()


# 线程锁
'''
由于线程之间的任务执行是CPU进行随机调度的，并且每个线程可能只执行了n条指令之后就被切换到别的线程了。
当多个线程同时操作一个对象，如果没有很好地保护该对象，会造成程序结果的不可预期，这被称为“线程不安全”。
为了保证数据安全，我们设计了线程锁，即同一时刻只允许一个线程操作该数据。线程锁用于锁定资源，可以同时使用多个锁，
当你需要独占某一资源时，任何一个锁都可以锁这个资源，就好比你用不同的锁都可以把相同的一个箱子锁住是一个道理。
'''

if __name__ == '__main__':
    # test2()
    # test3()
    # test4()
    test5()
