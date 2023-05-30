from math import sqrt

"""
装饰器 property，静态属性
使用场景一：修饰方法，指方法可以像属性一样访问
使用场景二：与定义的属性配合使用，防止属性被修改
静态属性（用来封装逻辑）与实例对象绑定。在将方法装饰成静态属性后，调用的时候就像是在调用属性（对象名.方法名），方法必须有返回值。
之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，
比如我们没有办法检查赋给属性的值是否有效。我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，
不建议外界直接访问，那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便，代码如下。

静态方法：
与静态属性一样，需要在方法前用@staticmethod装饰，而它所装饰的方法既不和实例化对象绑定，也不和类绑定所以它既不能调用实例化对象的属性，也不能使用类的属性。

类方法：
类方法自然的是与类绑定，用classmethod装饰器装饰的方法，类方法的第一个参数约定名为cls，cls实际上代表的就是类名，就像self代表的是实例化对象名一样，
其和类绑定只能访问类的属性调用方法时使用类名.方法名（参数…）也可以对象名.方法名（参数）**建议使用类名调用。

"""


# property使用场景一 修饰方法
class DataSet(object):
    @property
    def method_with_property(self):
        return "hello"

    def method_without_property(self):
        return "hello2"


def test1():
    test = DataSet()
    # 加了@property，可以用调用属性的形式来调用方法，后面不需要加()
    print(test.method_with_property)
    # 没有加@property，必须使用正常的调用的方法，即后面加()
    print(test.method_without_property())


# property使用场景二 保护属性
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器——getter方法
    # 加@property后，这个方法相当于一个属性，这个属性可以让用户进行使用，且用户没有办法随意修改。
    @property
    def name(self):
        return self._name

    # 访问器——getter方法
    @property
    def age(self):
        return self._age

    # 修改器——setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person("王大锤", 12)
    person.play()
    # 用户进行调用时，直接调用age即可，而不知道属性名_age，因此用户无法更改属性，从而保护了类的属性
    person.age = 22
    person.play()

    # person.name = "白远方"
    # AttributeError: can't set attribute


# 静态方法 计算三角形周长和面积，输入三条边
class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 静态方法，判定是否满足构成三角形
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    # 求周长
    def perimeter(self):
        return self._a + self._b + self._c

    # 求面积
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def test2():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print("周长:%s." % t.perimeter())
        print("面积:%s." % t.area())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        print("周长:%s." % Triangle.perimeter(t))
        print("面积:%s." % Triangle.area(t))
    else:
        print("无法构成三角形")


# 综合案例 静态属性、静态方法、类方法
class School:
    school = 'HengShui'

    def __init__(self, name, size, arrd):
        self.name = name
        self._size = size
        self.arrd = arrd

    def tech(self):
        print("开始上课了")

    @staticmethod  # 静态方法，不与对象绑定，也不与类绑定，即不能使用类的变量和对象的变量
    def area(width, height):
        print("学校面积为:%s." % (width * height))

    @classmethod  # 类方法，与类绑定(只能访问类变量)
    def xiake(cls):
        print("%s下课了." % cls.school)

    @property  # 静态属性，与实例对象绑定
    def size(self):
        return self._size  # 必须要有返回值

    @size.setter  # 修改器
    def size(self, size):
        self._size = size


def test3():
    p1 = School('Myschool', 4000, '关山大道')
    print(School.__dict__)
    print(p1.__dict__)
    # 类方法由类直接调用(推荐使用),也可以使用实例对象调用(意义不大)
    School.xiake()
    p1.xiake()

    # 静态方法有类调用,对象调用也可
    School.area(200, 300)
    p1.area(200, 300)

    # 访问静态属性或修改,可以向访问数据属性一样去访问area,会触发一个函数的执行,动态计算出一个值
    print(p1.size)
    p1.size = 300
    print(p1.size)


if __name__ == '__main__':
    test1()
    main()
    test2()
    test3()
