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


# 选择排序
def select(list_):
    # 每轮选出一个最小值，需要选len(list_)-1轮
    for i in range(len(list_) - 1):
        min = i  # 将数据所在的索引作为擂主,即假设 list_[i]为最小值
        for j in range(i + 1, len(list_)):
            if list_[min] > list_[j]:
                min = j  # 擂主换人
        # 进行交换，将最小值换到应该在的位置
        if min != i:
            list_[i], list_[min] = list_[min], list_[i]


# 插入排序
def insert(list_):
    # 控制每次比较的数是谁，从第二个数开始
    for i in range(1, len(list_)):
        x = list_[i]  # 空出list_[i]的数值
        j = i - 1
        while j >= 0 and list_[j] > x:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = x


# 二分查找
def search(list_, key):
    # 第一个数index，和最后一个数index
    low, high = 0, len(list_) - 1
    while low <= high:
        mid = (low + high) // 2
        if list_[mid] > key:
            high = mid - 1
        elif list_[mid] < key:
            low = mid + 1
        else:
            return mid


if __name__ == '__main__':
    l = [4, 7, 8, 1, 3, 5, 6, 2]

    # buble(l)  #冒泡排序
    # quick(l, 0, len(l) - 1)  # 快速排序
    # select(l)   #选择排序
    # insert(l)
    li = [1, 2, 3, 4, 5, 6, 8, 9]
    print(search(li, 9))
    # print(l)
