# 多线程通信
from multiprocessing import Process


# 写一个冒泡排序的函数


def bubble_sort(lst):
    # 循环执行比较操作
    for i in range(len(lst)):
        # 循环执行比较操作
        for j in range(len(lst) - 1 - i):
            # 如果当前元素大于前一个元素
            if lst[j] > lst[j + 1]:
                # 将当前元素替换为前一个元素
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


# 生成一个插入排序函数
def insert_sort(lst):
    # 循环执行比较操作
    for i in range(1, len(lst)):
        # 循环执行比较操作
        for j in range(i, 0, -1):
            # 如果当前元素小于前一个元素
            if lst[j] < lst[j - 1]:
                # 将当前元素替换为前一个元素
                lst[j], lst[j - 1] = lst[j - 1], lst[j]


lits_i = [1, 7, 3, 9, 2, 6]
# 将lits_i排序
insert_sort(lits_i)
print(lits_i)