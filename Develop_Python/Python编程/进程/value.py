# Author :   Kql_unicorn
# Date   :   2023/8/6 22:27
"""
开辟单一共享内存空间
注意：共享内存只能有一个值
"""

from multiprocessing import Process, Value
import time
import random

# 创建共享内存
money = Value('i', 5000)


# 线程函数
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += random.randint(1, 1000)

#   线程函数
def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= random.randint(100, 800)


if __name__ == '__main__':
    p1 = Process(target=man)
    p2 = Process(target=girl)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("一个月余额：", money.value)
