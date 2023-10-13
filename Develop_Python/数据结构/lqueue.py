# @Author : Kql
# @Time : 2023/7/17 16:05
"""
lqueue.py 链式队列
思路分析：
1. 基于链表构建队列模型
2. 链表的开端作为队头，结尾位置作为队尾。
3. 单独定义队尾标记，避免每次插入数据遍历。
4. 队头和队尾重叠时认为队列为空。
"""


# 自定义异常类
class QueueError(Exception):
    pass


# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LQueue:
    def __init__(self):
        # 定义队头和队尾的属性变量
        self.front = self.rear = Node(None)

    # 判定队列为空
    def is_empty(self):
        return self.front == self.rear

    # 入队
    def enqueue(self, val):
        self.rear.next = Node(val)
        self.rear = self.rear.next

    # 队列出队
    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("Queue is empty")
        # 此时front节点已经将第一个节点出队了，只是明面上指向一个地址节点。
        self.front = self.front.next
        return self.front.val


if __name__ == '__main__':
    sq = LQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    while sq.is_empty():
        print(sq.dequeue())
