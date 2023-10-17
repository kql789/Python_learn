from collections.abc import Iterator

'''
__init__ :      构造函数，在生成对象时调用
__del__ :       析构函数，释放对象时使用
__repr__ :      打印，转换
__setitem__ :   按照索引赋值
__getitem__:    按照索引获取值
__len__:        获得长度
__cmp__:        比较运算
__call__:       调用
__add__:        加运算
__sub__:        减运算
__mul__:        乘运算
__div__:        除运算
__mod__:        求余运算
__pow__:        幂
需要注意的是，这些成员里面有些是方法，调用时要加括号，有些是属性，调用时不需要加括号
'''


# 1. __doc__  说明性文档和信息，Python自建，无需自定义
class Foo(object):
    '''描述类信息，可被自定收集'''

    def func(self):
        pass


# 输出：描述类信息，可被自定收集
print(Foo.__doc__)


# 2. __init__ 实例化方法，通过类创建实例时，自动触发执行
class Foo1(object):
    def __init__(self, name):
        self.name = name
        self.age = 18


obj = Foo1('jack')  # 自动执行类中的__init__方法


# 3. __module__  和__class__
# __module__ 表示当前操作的对象在属于哪个模块
# __class__ 表示当前操作的对象属于哪个类

class Foo2:
    pass


obj2 = Foo2()
print(obj2.__module__)  # 输出：__main__
print(obj2.__class__)  # 输出：<class '__main__.Foo2'>


# 4. __del__() 析构方法，当对象在内存中被释放时，自动触发此方法，无需定义，因Python 自带内存分配和释放机制
# 除非你需要在释放的时候指定做一些动作。析构函数的调用是由解释器在进行垃圾回收时自动触发执行的。
class Foo3:
    def __del__(self):
        print("我被释放回收了！")


obj3 = Foo3()
del obj  # 删除类对象


# 5. __call__ 将一个类实例变成一个可调用对象，使用函数方法调用。如果为一个类编写了该方法，那么在该类的实例后面加括号，可直接调用这个方法。
# 构造方法的执行是由类加括号执行的，即：对象 = 类名()，而对于__call__() 方法，是由对象后加括号触发的，即：对象() 或者 类()()
class Foo4:
    def __init__(self, name):
        self.name = name

    def __call__(self, friend):
        print('My name is %s...' % self.name)
        print('My friend is %s...' % friend)


obj4 = Foo4('jack')
obj4('小明')


# 6. __dict__  列出类或对象中所有成员，非常重要和有用的一个属性，Python内置，无需自定义
class Province:
    country = 'BeiJing'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print('func')


# 7. __dict__ 获取类成员
# 输出{'__module__': '__main__', 'country': 'BeiJing', '__init__': <function Province.__init__ at 0x104668940>, 'func': <function Province.func at 0x1046689d0>,
# '__dict__': <attribute '__dict__' of 'Province' objects>, '__weakref__': <attribute '__weakref__' of 'Province' objects>, '__doc__': None}
print(Province.__dict__)
# 获取对象objt的成员
objt = Province('XiaoMing', 20)
print(objt.__dict__)  # 输出{'name': 'XiaoMing', 'count': 20}
objr = Province('XIAOHONG', 30)
print(objr.__dict__)  # 输出： {'name': 'XIAOHONG', 'count': 30}


# 8. __str__ 如果一个类中定义了该方法，那么在打印对象时，默认输出该方法的返回值，需要自定义。
class Foo5:
    pass


obj5 = Foo5()
print(obj5)  # 输出：<__main__.Foo5 object at 0x104994850>


class Foo6:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return self.name + '居住在' + self.city


obj6 = Foo6('小明', '上海')
print(obj6)  # 输出：小明居住在上海

# 8.__getitem__()、__setitem__()、__delitem__()
'''取值、赋值、删除这“三剑客”的套路，在Python中，我们已经见过很多次了，比如前面的@property装饰器。
Python中，标识符后面加圆括号，通常代表执行或调用方法的意思。而在标识符后面加中括号[]，通常代表取值的意思。
Python设计了__getitem__()、__setitem__()、__delitem__()这三个特殊成员，用于执行与中括号有关的动作。
它们分别表示取值、赋值、删除数据。如果有一个类同时定义了这三个魔法方法，那么这个类的实例的行为看起来就像一个字典一样，如下例所示：'''


class Foo7:
    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj7 = Foo7()
result = obj7['k1']  # 自动触发执行 __getitem__
obj7['k2'] = 'jack'  # 自动触发执行 __setitem__
del obj7['k1']  # 自动触发执行 __delitem__

# 9. __iter__
'''
这是迭代器方法！列表、字典、元组之所以可以进行for循环，是因为其内部定义了 __iter__()这个方法。
如果用户想让自定义的类的对象可以被迭代，那么就需要在类中定义这个方法，并且让该方法的返回值是一个可迭代的对象。
当在代码中利用for循环遍历对象时，就会调用类的这个__iter__()方法。
'''


class Foo8:
    def __init__(self, sq):
        self.sq = sq

    def __iter__(self):
        return iter(self.sq)


obj8 = Foo8([11, 22, 33, 44])
for i in obj8:
    print(i)

# 10.  __len__
'''
在Python中，如果你调用内置的len()函数试图获取一个对象的长度，在后台，其实是去调用该对象的__len__()方法，所以，下面的代码是等价的：
Python的list、dict、str等内置数据类型都实现了该方法，但是你自定义的类要实现len方法需要好好设计。
'''
print(len('ABC'))
print('ABC'.__len__())

# 11. __repr__
'''
这个方法的作用和__str__()很像，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。通常两者代码一样。
'''


class Foo11:
    def __init__(self, city):
        self.city = city

    def __str__(self):
        return "小明居住在%s" % self.city

    __repr__ = __str__


obj11 = Foo11("Bejing")
print(obj11)  # 输出小明居住在Bejing

# 12. 运算魔法
'''
__add__: 加运算 
__sub__: 减运算 
__mul__: 乘运算 
__div__: 除运算 
__mod__: 求余运算
 __pow__: 幂运算
 Python支持运算符的重载，也就是重写。
'''


class MyClass:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    # 两个对象的长相加，宽不变.返回一个新的类
    def __add__(self, others):
        return MyClass(self.height + others.height, self.weight + others.weight)

    # 两个对象的宽相减，长不变.返回一个新的类
    def __sub__(self, others):
        return MyClass(self.height - others.height, self.weight - others.weight)

    # 说一下自己的参数
    def intro(self):
        print("高为", self.height, " 重为", self.weight)


def main_test():
    a = MyClass(height=10, weight=5)
    a.intro()

    b = MyClass(height=20, weight=10)
    b.intro()

    c = b - a
    c.intro()

    d = a + b
    d.intro()


main_test()

# 13. __auther____author__代表作者信息


__author__ = "Kql"


def show():
    print(__author__)


show()
# 14 __slots__
'''
Python作为一种动态语言，可以在类定义完成和实例化后，给类或者对象继续添加随意个数或者任意类型的变量或方法，这是动态语言的特性。
'''


def test14(self):
    print('hello')


class Foo14:
    pass


obj14_1 = Foo14()
obj14_2 = Foo14()
# 动态添加实例变量
obj14_1.name = 'kql'
obj14_2.age = 20
# 动态的给类添加实例方法
Foo14.show = test14
obj14_1.show()
obj14_2.show()


# 限制给实例添加的变量使用__slots__

class Foo14_1:
    __slots__ = ('name', 'age')
    pass


obj14_t = Foo14_1()
obj14_w = Foo14_1()
# 动态添加实例变量
obj14_t.name = 'kql'
obj14_w.age = 20
# obj14_t.sex = 0 #会报错
# 无法限制给类添加方法
Foo14_1.show = test14
obj14_t.show()
obj14_w.show()

'''
注意：__slots__定义的属性仅对当前类的实例起作用，对继承了它的子类时不起作用的。
若是需要对子类也起作用，则需要也在子类上加上__slots__方法，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__
'''


class Foo15:
    __slots__ = ('name', 'age')
    pass


class Foo16(Foo15):
    print('this class is Foo16')
    __slots__ = ('sex')
    pass


obj16 = Foo16()
obj16.name = 'jack'
obj16.age = 30
obj16.sex = '男'
# obj16.city = 'Beijing'  # 报错，因为父类和子类的__slots__中都没有city变量，所以是不允许添加的。
