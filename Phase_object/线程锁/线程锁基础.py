# @Author : Kql
# @Time : 2023/6/8 16:31
import threading
import time

'''
由于线程之间的任务执行是CPU进行随机调度的，并且每个线程可能只执行了n条指令之后就被切换到别的线程了。
当多个线程同时操作一个对象，如果没有很好地保护该对象，会造成程序结果的不可预期，这被称为“线程不安全”。
为了保证数据安全，我们设计了线程锁，即同一时刻只允许一个线程操作该数据。线程锁用于锁定资源，可以同时使用多个锁，
当你需要独占某一资源时，任何一个锁都可以锁这个资源，就好比你用不同的锁都可以把相同的一个箱子锁住是一个道理。
'''
# 没有锁，导致脏数据产生
number = 0


def plus():
    global number
    for _ in range(1000000):
        number += 1
    print('子线程%s运算完后,number = %s' % (threading.current_thread().getName(), number))


def test1():
    for i in range(2):
        # 开启两个子线程，就可以观察到脏数据
        t = threading.Thread(target=plus)
        t.start()
        t.join()  # 添加这一行就让两个子线程变成了顺序执行


'''
面为了防止脏数据而使用join()的方法，其实是让多线程变成了单线程，属于因噎废食的做法，正确的做法是使用线程锁。Python在threading模块中定义了几种线程锁类，分别是：
Lock 互斥锁
RLock 可重入锁
Semaphore 信号
Event 事件
Condition 条件
Barrier “阻碍
'''

if __name__ == '__main__':
    pass
    test1()
    time.sleep(2)  # 等待2秒，确保两个子线程都结束运算
    print('主线程执行完毕，number= ', number)
    '''输出结果：，并不是2000000
        子线程Thread-1运算完后,number = 1260744
        子线程Thread-2运算完后,number = 1369186
        主线程执行完毕，number=  1369186
    '''
    # 这是因为两个线程在运行过程中，CPU随机调度，你算一会我算一会，在没有对number进行保护的情况下，就发生了数据错误。

'''
通过with语句使用线程锁
所有的线程锁都有一个加锁和释放锁的动作，非常类似文件的打开和关闭。在加锁后，如果线程执行过程中出现异常或者错误，
没有正常的释放锁，那么其他的线程会造到致命性的影响。通过with上下文管理器，可以确保锁被正常释放。其格式如下：

with some_lock:
    # 执行任务...
这相当于：

some_lock.acquire()
try:
    # 执行任务..
finally:
    some_lock.release()
'''
