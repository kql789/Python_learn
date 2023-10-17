# @Author : Kql
# @Time : 2023/10/16 10:17
# @FileName : 单类继承.py
# @Blog ：https://blog.csdn.net/weixin_56175042

class Fruit():
    def color(self):
        print("Fruits are colorful")


class Apple(Fruit):
    def color(self):
        super().color()
        print("Apple is Red")


class Orange(Fruit):
    def color(self):
        super().color()
        print("Orange is orange")

apple = Apple()
orange = Orange()
apple.color()
orange.color()
