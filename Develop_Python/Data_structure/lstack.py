# @Author : Kql
# @Time : 2023/7/17 12:03
"""
栈的链式栈
思路分析：
1. 源于链表结构
2. 封装栈的操作方法 | 入栈出栈，栈空，栈顶元素。
3. 链表的开头作为栈顶？（不用每次遍历）
"""


# 自定义异常
class StackError(Exception):
    pass


# 创建节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 链式栈操作
class LStack:
    def __init__(self):
        # 标记栈的栈顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, val):
        self._top = Node(val, self._top)

    def pop(self):
        if self._top is None:
            raise StackError("Stack is empty")
        value = self._top.val
        self._top = self._top.next
        return value


if __name__ == "__main__":
    ls = LStack()
    ls.push(20)
    ls.push(30)
    ls.push(10)
    print(ls.pop())

