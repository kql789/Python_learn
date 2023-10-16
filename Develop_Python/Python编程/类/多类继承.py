# @Author : Kql
# @Time : 2023/10/16 11:44
# @FileName : 多类继承.py
# @Blog ：https://blog.csdn.net/weixin_56175042
"""
在单类继承中，super()函数用于指向要继承的父类，且不需要显式的写出父类名称。
但是在多类继承中，会涉及到查找顺序（MRO）、
钻石继承等问题。MRO 是类的方法解析顺序表,
也就是继承父类方法时的顺序表。钻石继承：
    A
   / \
  B   C
   \ /
    D

"""


class Plant():
    def __init__(self):
        print("Enter plant")
        print("Leavel plant")


class Fruit(Plant):
    def __init__(self):
        print("Enter Fruit")
        super().__init__()
        print("Leavel fruit")


class Vegetable(Plant):
    def __init__(self):
        print("Enter vegeable")
        super().__init__()
        print("Leavel vegeable")


class Tomato(Fruit, Vegetable):
    def __init__(self):
        print("Enter Tomato")
        super().__init__()
        print("Level Tomato")


# ve = Vegetable()
# fu = Fruit()
to = Tomato()
print(Tomato.__mro__)