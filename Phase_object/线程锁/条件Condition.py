# @Author : Kql
# @Time : 2023/6/8 17:15
import threading
import time

'''
类名：Condition
Condition称作条件锁，依然是通过acquire()/release()加锁解锁。
wait([timeout])方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。
notify()方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池），其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
notifyAll()方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
下面的例子，有助于你理解Condition的使用方法：
'''

num = 0
con = threading.Condition()


class Foo(threading.Thread):
    def __init__(self, name, action):
        super(Foo, self).__init__()
        self.name = name
        self.action = action

    def run(self):
        global num
        con.acquire()
        print('%s开始执行....' % self.name)
        while True:
            if self.action == 'add':
                num += 1
            elif self.action == 'reduce':
                num -= 1
            else:
                exit(1)
            print('当前num为： ', num)
            time.sleep(1)
            if num == 5 or num == 0:
                print('暂停执行%s!' % self.name)
                con.notify()
                con.wait()
                print('%s开始执行..' % self.name)
        con.release()


if __name__ == '__main__':
    a = Foo("线程A", 'add')
    b = Foo('线程B', 'reduce')
    a.start()
    b.start()
