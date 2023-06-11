# Author :   Kql_unicorn
# Date   :   2023/6/10 20:19
import threading
import time


# 	创建两个线程，其中一个输出1-52，另外一个输出A-Z。
# 	输出格式要求：
# 	12A
# 	34B
# 	56C
# 	...
# 	5152Z

def func():
    for i in range(53):
        print(i, end='')
        time.sleep(1)


def func1():
    for i in range(65, 91):
        time.sleep(1)
        print(chr(i), end='')
        print()


def test1():
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func1)
    t1.start()
    t2.start()


#  使用多线程在终端打印hello world+线程名字
class PrintHello(threading.Thread):
    def run(self):
        print("Hello,World" + self.name)


def test2():
    print_task = PrintHello()
    # 启动线程
    print_task.start()


if __name__ == '__main__':
    test2()
