# @Author : Kql
# @Time : 2023/7/13 19:26
from link_list import *
import time

# l = range(999999)
l = [i for i in range(999999)]
# 链表初始化
link = LinkList()
# 链表插入
link.init_list(l)
# 开始计时
tm = time.time()
# for i in l:
#     print(i)  #  3.307s 列表
# link.show()  # 4.61s  单链表
# l.append(8899)  # 列表尾部插入 2.86* 10-6

# link.append(8899)  # 链表尾部插入  0.0534

# l.insert(0, 8899)   # 列表头部插入，0.00392
# link.head_insert(8899)  # 链表头部插入 4.76*10-6
# l.insert(100, 2344)  # 列表插入到指定位置数据， 0.0037
# link.insert(300000, 2344)  # 0.021

# l.remove(200)  # 按照值进行删除 0.0058
# link.delete(850218)  # 按照值进行删除 0.085
# print(l[10])  # 按照索引获取值,1.88
print(link.get_index(10))  # 按照索引获取值，2.69*10-5
# 计时结束
print("time:", time.time() - tm)

'''
总结：
1. 数据初始化输出，列表的速度最快，即线性表的顺序结构查询速度高。
2. 数据尾部插入，列表速度最快，即线性表的顺序结构。
3. 数据头部插入，链表的插入最快，不需要遍历，列表插入时，需要把后续数据全部重构。
4. 插入到指定指定位置时，只有特殊的头部或尾部才有明显的时间差，其他位置时间差相差不大。
'''
