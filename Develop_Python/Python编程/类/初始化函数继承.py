# @Author : Kql
# @Time : 2023/10/16 11:11
# @FileName : 初始化函数继承.py
# @Blog ：https://blog.csdn.net/weixin_56175042

"""
如果我们需要给类传入参数，需要使用初始化函数。如果所有子类中部分参数是相同的，
那么可以在父类的初始化函数中定义这些参数，然后子类继承父类的初始化函数，
这样所有子类就可共享这些参数，而不需要在每个子类中单独定义。初始化函数的继承：
"""


class Fruit():
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape


class Apple(Fruit):
    def __init__(self, color, shape, taste):
        Fruit.__init__(self, color, shape)  # 等价于super().__init__(color,shape)
        self.taste = taste

    def feature(self):
        print("Apple's color is {}, shape is {} and taste {}".format(
            self.color, self.shape, self.taste))


class Orange(Fruit):
    def __init__(self, color, shape, taste):
        # Fruit.__int__(self, color, shape)
        super().__init__(color, shape)
        self.taste = taste

    def feature(self):
        print("Orange's color is {}, shape is {} and taste {}".format(
            self.color, self.shape, self.taste))


apple = Apple("red", "square", "sour")
apple.feature()
orange = Orange("orange", "round", "sweet")
orange.feature()
