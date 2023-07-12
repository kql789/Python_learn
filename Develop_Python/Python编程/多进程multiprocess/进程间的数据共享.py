# Author :   Kql_unicorn
# Date   :   2023/6/8 22:06
from multiprocessing import Process, set_start_method, Manager, queues
import multiprocessing

set_start_method('fork')
from multiprocessing import Array

'''
在Linux中，每个子进程的数据都是由父进程提供的，每启动一个子进程就从父进程克隆一份数据。
创建一个进程需要非常大的开销，每个进程都有自己独立的数据空间，不同进程之间通常是不能共享数据的，
要想共享数据，一般通过中间件来实现。
下面我们尝试用一个全局列表来实现进程间的数据共享：
'''

lis = []


def foo1(i):
    lis.append(i)
    print("This is Process ", i, " and lis is ", lis, " and lis.address is  ", id(lis))


def test1():
    for i in range(5):
        p = Process(target=foo1, args=(i,))
        p.start()


'''
可以看到，全局列表lis没有起到任何作用，在主进程和子进程中，lis指向内存中不同的列表。
想要在进程之间进行数据共享可以使用Queues、Array和Manager这三个multiprocess模块提供的类。
'''

# 1. 使用Array共享数据
'''
对于Array数组类，括号内的“i”表示它内部的元素全部是int类型，而不是指字符“i”，数组内的元素可以预先指定，
也可以只指定数组的长度。Array类在实例化的时候必须指定数组的数据类型和数组的大小，类似temp = Array('i', 5)。对于数据类型有下面的对应关系：
'''
"""
'c': ctypes.c_char, 'u': ctypes.c_wchar,
'b': ctypes.c_byte, 'B': ctypes.c_ubyte,
'h': ctypes.c_short, 'H': ctypes.c_ushort,
'i': ctypes.c_int, 'I': ctypes.c_uint,
'l': ctypes.c_long, 'L': ctypes.c_ulong,
'f': ctypes.c_float, 'd': ctypes.c_double
"""


def func1(i, temp):
    temp[0] += 100
    print("进程%s " % i, ' 修改数组第一个元素后----->', temp[0])


def test2():
    temp = Array('i', [1, 2, 3, 4])
    for i in range(10):
        p = Process(target=func1, args=(i, temp))
        p.start()


""" 输出结果
进程0   修改数组第一个元素后-----> 101
进程1   修改数组第一个元素后-----> 201
进程2   修改数组第一个元素后-----> 301
进程3   修改数组第一个元素后-----> 401
进程4   修改数组第一个元素后-----> 501
进程5   修改数组第一个元素后-----> 601
进程6   修改数组第一个元素后-----> 701
进程7   修改数组第一个元素后-----> 801
进程8   修改数组第一个元素后-----> 901
进程9   修改数组第一个元素后-----> 1001
"""

# 2. 使用Manager共享数据
'''
通过Manager类也可以实现进程间数据的共享。Manager()返回的manager对象提供一个服务进程，
使得其他进程可以通过代理的方式操作Python对象。manager对象支持 list, dict, Namespace,
 Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, 
 Value ,Array等多种格式。
'''


def func2(i, dic):
    dic['num'] = 100 + i
    print(dic.items())


def test3():
    dic = Manager().dict()
    for i in range(10):
        p = Process(target=func2, args=(i, dic))
        p.start()
        p.join()


''' 输出结果
[('num', 100)]
[('num', 101)]
[('num', 102)]
[('num', 103)]
[('num', 104)]
[('num', 105)]
[('num', 106)]
[('num', 107)]
[('num', 108)]
[('num', 109)]
'''


# 3.使用queues的Queue类共享数据
def func4(i, q):
    ret = q.get()
    print("进程%s从队列里获取了一个%s，然后又向队列里放入了一个%s" % (i, ret, i))
    q.put(i)


def test4():
    lis = queues.Queue(20, ctx=multiprocessing)
    lis.put(0)
    for i in range(10):
        p = Process(target=func4, args=(i, lis,))
        p.start()


'''
关于queue和Queue，在Python库中非常频繁的出现，很容易就搞混淆了。
甚至是multiprocessing自己还有一个Queue类(大写的Q)，
一样能实现queues.Queue的功能，导入方式是from multiprocessing import Queue。
'''

if __name__ == '__main__':
    # test3()
    test4()
# test1()
# test2()
