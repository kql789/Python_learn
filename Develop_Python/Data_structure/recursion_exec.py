# @Author : Kql
# @Time : 2023/7/20 15:46

"""
求一个数的阶乘
递归思想
"""


def recursion(num):
    if num <= 1:
        return 1
    return num * recursion(num - 1)


if __name__ == '__main__':
    print(recursion(10))
