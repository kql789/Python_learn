# Author :   Kql_unicorn
# Date   :   2023/6/8 22:43
from multiprocessing import Process, set_start_method
from multiprocessing import Array, RLock, Lock, Condition, Semaphore
import time

set_start_method('fork')

'''
为了防止和多线程一样的出现数据抢夺和脏数据的问题，同样需要设置进程锁。与threading类似，
在multiprocessing里也有同名的锁类RLock，Lock，Event，Condition和 Semaphore，
连用法都是一样样的，这一点非常友好！
'''


def func(i, lis, lc):
    lc.acquire()
    lis[0] = lis[0] - 1
    time.sleep(1)
    print('say hi', lis[0])
    lc.release()


''' 输出结果
say hi 9
say hi 8
say hi 7
say hi 6
say hi 5
say hi 4
say hi 3
say hi 2
say hi 1
say hi 0
'''
if __name__ == '__main__':
    array = Array('i', 1)
    array[0] = 10
    lock = Lock()
    for i in range(10):
        p = Process(target=func, args=(i, array, lock))
        p.start()
