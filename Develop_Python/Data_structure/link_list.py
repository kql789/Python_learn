# @Author : Kql
# @Time : 2023/7/13 19:13

# 创建节点类
class Node:
    """
    思路：将自定义的类视为节点的生成的类，实例对象中包含数据部分和指向下一个节点的next
    """

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkList():
    """
    思路:单链表类，生成对象可以进行增删改查操作
    具体操作通过调用具体方法完成。
    """

    def __init__(self):
        """
        初始化链表，标记一个链表的开端，以便于获取后续的节点。
        """
        self.head = Node(None)

    # 通过list_为来拿表添加一组节点
    def init_list(self, list_):
        p = self.head  # p作为移动变量
        for item in list_:
            p.next = Node(item)
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head.next
        while p is not None:
            print(p.val)
            p = p.next  # 向后移动一个
