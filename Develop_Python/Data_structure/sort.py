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
def sub_sort(list_, low, high):
    # 设置基准
    x = list_[low]
    # low向后，high向前
    while low < high:
        # 比基准小的数往前放
        while list_[high] > x and low < high:
            high -= 1
        list_[low] = list_[high]
        # 比基准大的数往后放
        while list_[low] < x and low < high:
            low += 1
        list_[high] = list_[low]
    # 当两者相碰撞时，将基准插入
    list_[low] = x
    # 返回此时的基准所在索引
    return low


# 快速排序
def quick(list_, low, high):
    # low为有序数组中第一个元素的索引，high为最后一个数组的索引
    if low < high:
        key = sub_sort(list_, low, high)
        quick(list_, low, key - 1)
        quick(list_, key + 1, high)


if __name__ == '__main__':
    l = [4, 7, 8, 1, 3, 5, 6, 2]

    # buble(l)  #冒泡排序
    quick(l, 0, len(l) - 1)  # 快速排序
    print(l)
