# @Author : Kql
# @Time : 2023/7/20 15:49

"""
链式二叉树遍历
思路分析：
1. 使用链式存储，一个Node表示一个树的节点
2. 节点考虑使用两个属性变量分别表示左来连接和右连接

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树遍历类
class Bitree:
    pass

