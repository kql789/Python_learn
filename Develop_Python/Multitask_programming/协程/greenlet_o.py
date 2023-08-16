# @Author : Kql
# @Time : 2023/8/16 18:13
# @FileName : greenlet_o.py
# @Blog ：https://blog.csdn.net/weixin_56175042
"""
协程行为示例
"""
from greenlet import greenlet


def fun1():
    print("执行func1")
    gr2.switch()
    print("结束func1")
    gr2.switch()


def fun2():
    print("执行func2")
    gr1.switch()
    print("结束func2")


# 将函数变成协程
gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()  # 选择执行哪个协程
