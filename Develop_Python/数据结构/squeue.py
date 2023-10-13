# @Author : Kql
# @Time : 2023/7/17 14:54
"""
squeue队列的顺序存储
思路分析：
1. 基于列表完成数据存储。
2. 通过封装规定数据操作。
"""


# 自定义异常类
class QueueError(Exception):
    pass


# 队列操作
class SQueue:
    def __init__(self):
        self._elems = []

    # 判定队列为空
    def is_empty(self):
        return self._elems == []

    # 入队,列表的尾部定义为队尾
    def enqueue(self, val):
        self._elems.append(val)

    # 出队,列表的第一个元素
    def dequeue(self):
        if not self._elems:
            raise QueueError("Queue is empty")
        return self._elems.pop(0)


from sstack import *


# 如何将出队的数据进行翻转,即先出队入栈，之后在出栈入队
def convert_queue():
    sqe = SQueue()
    for i in range(10):
        sqe.enqueue(i)

    st = SStack()
    # 出队入栈
    while not sqe.is_empty():
        st.push(sqe.dequeue())
    # 出栈入队
    while not st.is_empty():
        sqe.enqueue(st.pop())
    # 直接出队
    while not sqe.is_empty():
        print(sqe.dequeue())


if __name__ == '__main__':
    convert_queue()
    # sq = SQueue()
    # sq.enqueue(10)
    # sq.enqueue(20)
    # sq.enqueue(30)
    # while not sq.is_empty():
    #     print(sq.dequeue())
