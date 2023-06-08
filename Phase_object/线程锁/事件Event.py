# @Author : Kql
# @Time : 2023/6/8 17:02
import threading
import time

'''
类名：Event
事件线程锁的运行机制：全局定义了一个Flag，如果Flag的值为False，那么当程序执行wait()方法时就会阻塞，如果Flag值为True，线程不再阻塞。这种锁，类似交通红绿灯（默认是红灯），它属于在红灯的时候一次性阻挡所有线程，在绿灯的时候，一次性放行所有排队中的线程。
事件主要提供了四个方法set()、wait()、clear()和is_set()。
调用clear()方法会将事件的Flag设置为False。
调用set()方法会将Flag设置为True。
调用wait()方法将等待“红绿灯”信号。
is_set():判断当前是否"绿灯放行"状态
'''
# 下面是一个模拟红绿灯，然后汽车通行的例子：
event = threading.Event()


def lighter():
    green_time = 5
    red_time = 5
    event.set()  # 初始设置为绿灯,即全部放行
    while True:
        print("\33[32;0m 绿灯亮...\033[0m")
        time.sleep(green_time)
        event.clear()  # 即阻塞，全部等待
        print("\33[31;0m 红灯亮...\033[0m")
        time.sleep(red_time)
        event.set()  # 再次全部通行


def run(name):
    while True:
        if event.is_set():  # 判断当前是否"放行"状态
            print("一辆[%s] 呼啸开过..." % name)
        else:
            print("一辆[%s]开来，看到红灯，无奈的停下了..." % name)
            event.wait()
            print("[%s] 看到绿灯亮了，瞬间飞起....." % name)


if __name__ == '__main__':
    light = threading.Thread(target=lighter, )
    light.start()
    for name in ['奔驰', '宝马', '奥迪']:
        car = threading.Thread(target=run, args=(name,))
        car.start()
