# @Author : Kql
# @Time : 2023/7/14 16:20
'''
现有两个有序的列表，请使用单链表方式将其进行合并，合并后的数据仍然是有序数据.
'''
from link_list import *

l1 = LinkList()
l2 = LinkList()

l1.init_list([2, 3, 5, 9, 13, 15])
l2.init_list([1, 4, 6, 7, 8, 10, 11, 12, 14])


def merge(l1, l2):
    p = l1.head
    q = l2.head.next
    while p.next is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            tmp = p.next
            p.next = q
            p = p.next
            q = tmp
    p.next = q


merge(l1, l2)
l1.show()
