# @Author : Kql
# @Time : 2023/6/8 16:42
import threading
import time

# 互斥锁  互斥锁是一种独占锁，同一时刻只有一个线程可以访问共享的数据。使用很简单，初始化锁对象，
# 然后将锁当做参数传递给任务函数，在任务中加锁，使用后释放锁。
number = 0
lock = threading.Lock()


def plus(lk):
    global number  # 生声明number是全局变量
    lk.acquire()  # 开始加锁
    for _ in range(1000000):
        number += 1
    print(print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number)))
    # 释放锁，让别的线程也可以访问number
    lk.release()


'''
RLock的使用方法和Lock一模一样，只不过它支持重入锁。该锁对象内部维护着一个Lock和一个counter对象。
counter对象记录了acquire的次数，使得资源可以被多次require。最后，当所有RLock被release后，其他线程才能获取资源。
在同一个线程中，RLock.acquire()可以被多次调用，利用该特性，可以解决部分死锁问题。
'''
if __name__ == '__main__':
    # 开启两个子线程，可以观察到脏数据
    for i in range(2):
        t = threading.Thread(target=plus, args=(lock,))
        t.start()
    time.sleep(2)  # 等待2秒，确保2个子线程都伊宁结束运算
    print("主线程执行完毕后，number = ", number)
