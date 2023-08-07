# Author :   Kql_unicorn
# Date   :   2023/8/6 22:33
"""
共享内存放一组数据
"""

from multiprocessing import Process, Array

# 创建共享内存
shm = Array('i', [1, 2, 3, 45, 7])


# shm = Array('i', 5)  # 初始开辟5个整型空间
# shm = Array('c', b'hello')  # 字节串


def fun():
    # array创建共享内存对象可迭代
    for i in shm:
        print(i)
    shm[1] = 1000


if __name__ == '__main__':
    p = Process(target=fun)
    p.start()
    p.join()
# for i in shm:
#     print(i)

print("----", shm[1])
