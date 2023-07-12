# Author :   Kql_unicorn
# Date   :   2023/6/8 21:59
import os
import multiprocessing

'''
Python中的multiprocess提供了Process类，实现进程相关的功能。但是它基于fork机制，
因此不被windows平台支持。想要在windows中运行，必须使用if __name__ == '__main__':的方式，
显然这只能用于调试和学习，不能用于实际环境。
另外，在multiprocess中你既可以import大写的Process，也可以import小写的process，
这两者是完全不同的东西。这种情况在Python中很多，请一定要小心和注意。
'''


def foo(i):
    # 同样的参数传递方法
    print('这里是', multiprocessing.current_process().name)
    print('模块名称：', __name__)
    print('父进程 id：', os.getppid())  # 获取父进程id
    print('当前子进程 id：', os.getpid())  # 获取自己的进程id
    print('————————————————————————————————————')


if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        p.start()
