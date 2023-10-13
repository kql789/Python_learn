# Author :   Kql_unicorn
# Date   :   2023/8/10 21:11
"""
线程锁演示
"""

from threading import Thread, Lock

a = b = 0
lock = Lock()


def value():
    while True:
        # 上锁
        lock.acquire()
        if a != b:
            print("a=%d,b=%d" % (a, b))
        # 解锁
        lock.release()


t = Thread(target=value)
t.start()
while True:
    # 上锁
    with lock:
        a += 1
        b += 1
t.join()
