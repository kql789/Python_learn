# @Author : Kql
# @Time : 2023/8/7 16:00
"""
线程属性测试
"""
from time import sleep
from threading import Thread


def func():
    sleep(3)
    print("线程属性测试")


t = Thread(target=func, name="tarren")
t.setDaemon(True)  # 主线程退出分支线程也退出
t.start()
t.setName("Teddu")
print('name:', t.getName())
print('is alive:', t.is_alive())
print('daemon:', t.isDaemon())
