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


# obj3 = Foo3()
# del obj  # 删除类对象


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
