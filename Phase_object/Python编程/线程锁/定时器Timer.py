# @Author : Kql
# @Time : 2023/6/8 17:36

from threading import Timer

'''定时器Timer类是threading模块中的一个小工具，用于指定n秒后执行某操作。一个简单但很实用的东西。'''


def hello():
    print('hello world')


# 表示1秒后执行hello函数
t = Timer(1, hello)
t.start()
