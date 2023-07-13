# @Author : Kql
# @Time : 2023/7/13 19:26
from link_list import *
import time

l = range(999999)

link = LinkList()
link.init_list(l)
tm = time.time()
# for i in l:
#     print(i)  #  3.307s 列表
link.show()  # 4.61s  单链表
print("time:", time.time() - tm)
