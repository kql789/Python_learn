# @Author : Kql
# @Time : 2023/7/21 13:50
"""
sort.py 排序算法训练
"""


# 冒泡排序
def buble(list_):
    n = len(list_)
    # 一共循环多少轮
    for i in range(n - 1):
        # 每轮两两比较的次数
        for j in range(n - 1 - i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]

# 快速排序
def quick():
    pass

l = [4, 7, 8, 1, 3, 5, 6, 2]

buble(l)
print(l)
