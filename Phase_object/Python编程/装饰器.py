from collections.abc import Iterable

'''
装饰器（Decorator）：从字面上理解，就是装饰对象的器件。可以在不修改原有代码的情况下，为被装饰的对象增加新的功能或者附加限制条件或者帮助输出。
装饰器有很多种，有函数的装饰器，也有类的装饰器。装饰器在很多语言中的名字也不尽相同，它体现的是设计模式中的装饰模式，
强调的是开放封闭原则。装饰器的语法是将@装饰器名，放在被装饰对象上面
规则是：被装饰的函数的名字会被当作参数传递给装饰函数。装饰函数执行它自己内部的代码后，会将它的返回值赋值给被装饰的函数。
'''

'''
开放封闭原则主要体现在两个方面：
对扩展开放，意味着有新的需求或变化时，可以对现有代码进行扩展，以适应新的情况。
对修改封闭，意味着类一旦设计完成，就可以独立其工作，而不要对类尽任何修改。
'''


def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        result = func()
        # return result

    return wrapper


@debug
def tesy():
    print("Hello")


tesy()  # 相当于tesy = debug(tesy)


def outer1(func):
    def inner(*args, **kwargs):
        # print("认证成功！")
        result = func(*args, **kwargs)
        # print("日志添加成功")
        print("我是装饰器1")
        # return result

    return inner


def outer2(func):
    def inner(*args, **kwargs):
        # print("一条欢迎信息。。。")
        result = func(*args, **kwargs)
        # print("一条欢送信息。。。")
        print("我是装饰器2")
        # return result

    return inner


@outer1
@outer2
def f1():
    print("%s 正在连接业务部门1数据接口......")


'''
在装饰器修饰完的函数，在执行的时候先执行原函数的功能，然后再由里到外依次执行装饰器的内容。
总结：
一个函数在多个装饰器装饰时，它的执行顺序是:先执行原函数的功能，然后再由里到外一次执行装饰器的内容。
注：在执行顺序时，如果装饰器内部在先有输出，则按照代码顺序先执行输出，之后在执行原有函数、其次是执行装饰器的内容。
'''


# 带参数的装饰器
def logging(level):
    def outter(func):
        def inner(*args, **kwargs):
            print("[{0}]: enter {1}()".format(level, func.__name__))
            result = func(*args, **kwargs)
            return result

        return inner

    return outter


@logging(level="INFO")  # hello = outter(hello)
def hello(a, b, c):
    print(a, b, c)


# 类装饰器
# 装饰器也不一定只能用函数来写，也可以使用类装饰器，用法与函数装饰器并没有太大区别，实质是使用了类方法中的call魔法方法来实现类的直接调用。
class Log(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[DEBUG]: enter {}()".format(self.func.__name__))
        return self.func(*args, **kwargs)


@Log
def he(a, b, c):
    print(a, b, c)


# 带参数的类装饰器
class Lg(object):
    def __init__(self, level):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{0}]: enter {1}()".format(self.level, func.__name__))
            result = func(*args, **kwargs)
            return result

        return wrapper


@Lg(level='TEST')
def helo(a, b, c):
    print(a, b, c)

'''
为什么要有装饰器？
代码要遵循开放封闭原则，简单来说，已经实现的功能代码内部不允许修改，但在外部可以被扩展。

'''
if __name__ == '__main__':
    # 调用方法
    # f1()
    hello("hello,", "good", "morning")  # hello() 就相当于执行了 outter
    he("hello,", "good", "morning")
    helo("hello,", "good", "morning")
