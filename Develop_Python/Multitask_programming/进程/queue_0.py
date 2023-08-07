# Author :   Kql_unicorn
# Date   :   2023/8/6 21:42
"""
进程间通信——消息队列演示
注意：消息队列符合先进先出原则
"""
from multiprocessing import Process, Queue
from multiprocessing.dummy import freeze_support
from time import sleep
from random import randint

q = Queue(maxsize=5)


def handle():
    for i in range(6):
        x = randint(1, 33)
        q.put(x)
    q.put(randint(1, 16))


def request():
    while True:
        sleep(2)
        print(q.get(3))


if __name__ == '__main__':
    freeze_support()
    p1 = Process(target=handle)
    p2 = Process(target=request)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
