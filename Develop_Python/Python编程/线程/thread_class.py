# Author :   Kql_unicorn
# Date   :   2023/8/7 22:24
"""
自定义线程类实例
"""
from threading import Thread


# 自定义线程类
class ThreadClass(Thread):
    # 重写父类init
    def __init__(self, *args, **kwargs):
        self.args = args[0]
        super().__init__()  # 加载父类init

    def f1(self):
        print("step 1")

    def f2(self):
        print("step 2")

    # 重写run逻辑调用
    def run(self):
        self.f1()
        self.f2()


t1 = ThreadClass("abc")
t1.start()
t1.join()
