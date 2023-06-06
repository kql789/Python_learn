from collections.abc import Generator

'''
生成器（generator）是一种返回一个值的迭代器，每次从该迭代器取下一个值。
生成器两种创建方式：
1. 生成器表达式
2. 生成器函数
生成器分类:
    通用生成器
    协程生成器
    委托生成器
    子生成器
'''
# 创建生成器——生成器表达式
'''生成器表达式是用圆括号来创建生成器，其语法与推导式相同，只是将 [] 换成了 () 。 生成器表达式会产生一个新的生成器对象。'''
g1 = [i for i in range(10)]
print(type(g1))
print(isinstance(g1, Generator))
g2 = (i for i in range(10))
print(type(g2))
print(isinstance(g2, Generator))
'''这种生成器表达式被成为隐式生成器，他是禁止使用 yield 和 yield from 表达式。'''
g3 = (i for i in range(3))

# for x in range(3):
#     print(next(g3))  # 当比那里到最后一个时，再次遍历则进行报错

'''
1. 函数如果包含 yield 指令，该函数调用的返回值是一个生成器对象，此时函数体中的代码并不会执行，只有显示或隐示地调用 next 的时候才会真正执行里面的代码。
使用这个函数返回一个生成器对象并使用它才是真正的目的。
2. yield可以暂停一个函数并返回此时的中间结果。该函数将保存执行环境并在下一次恢复。
3. 在生成器函数中使用 return 对其并没有任何影响，这个函数返回的仍然是生成器对象。但是，如果没有 return 语句，则执行到函数完毕时将返回 StopIteration 异常。
如果在执行过程中遇到 return 语句，则直接抛出 StopIteration 异常，终止迭代。如果在 return 后返回一个值，那么这个值作为 StopIteration 异常的说明，
不是函数的返回值。
4. 也可以通过 close() 手动关闭生成器函数，后面再调用生成器会直接返回 StopIteration异常。
'''


def func2():
    for i in range(5):
        print("Start")
        receive = yield i
        print("->->->")
        print("当前receive:{}".format(receive))


def test3():
    f = func2()
    print("*************R")
    print(next(f))
    print(next(f))
    print(next(f))
    dc = f.send("hello")
    print("当前dc:{}".format(dc))
    # print(next(f))
    # print(next(f))


def test4():
    print("______>")
    f = func2()
    f.send(None)  # 首次启动生成器时，send只能是none 或者其他方法调用 next() __next__
    print(next(f))


# 斐波那契函数——生成器
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


def test5():
    f = fibonacci(10)
    while True:
        try:
            print(next(f), end=' ')
        except StopIteration:
            break


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    test5()
