# Author :   Kql_unicorn
# Date   :   2023/7/16 21:02

"""
栈模型的顺序存储
思考总结：
1. 列表即顺序存储，但功能多，不符合栈的模型特征
2. 利用列表，将其封装，提供接口方法
"""


# 自定义异常
class StackError(Exception):
    pass


# 顺序栈类
class SStack:
    def __init__(self):
        self._elems = []

    # 判断列表为空
    def is_empty(self):
        return self._elems == []

    # 入栈
    def push(self, val):
        self._elems.append(val)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elems.pop()

    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elems[-1]


if __name__ == "__main__":
    s1 = SStack()  # 初始化
    s1.push(10)
    s1.push(30)
    s1.push(50)
    while not s1.is_empty():
        print(s1.pop())

'''
面试题:已知，一个堆栈的入栈顺序是1，2，3，下列不可能出现的出栈的顺序的是：
3,1,2


'''
