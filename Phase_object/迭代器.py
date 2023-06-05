from collections.abc import Iterable

# Iterable 用来判定一个对象是否可迭代
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))

'''
迭代器是一种可以被遍历的对象，并且能作用于next()函数。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
迭代器只能往后遍历不能回溯，不像列表，你随时可以取后面的数据，也可以返回头取前面的数据。迭代器通常要实现两个基本的方法：
iter() 和 next()。
字符串，列表或元组对象，甚至自定义对象都可用于创建迭代器：
'''
lis = [1, 2, ]
lt = iter(lis)

print(next(lt))
print(next(lt))
# print(next(lt))  # 当后面没有元素可以next的时候，弹出错误
# 或者使用for循环遍历迭代器：
for x in lt:
    print(x, end=' ')


# 为了让我们自己写的类成为一个迭代器，需要在类里实现__iter__()和__next__()方法
class Fib(object):
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.b
        raise StopIteration


def test1():
    iten = Fib(10)
    print(next(iten))
    print(next(iten))
    print(next(iten))


# 自定义迭代器
class MyIter(object):
    def __init__(self, m):
        self.data = m
        self.length = len(m)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.length - 1:
            self.index += 1
        else:
            raise StopIteration
        return self.data[self.index]


def test2():
    itew = MyIter(['A', 'B', 'C', 'D'])
    # print(next(itew))
    # print(next(itew))
    for i in itew:
        print(i)


'''
迭代器总结:
Python的迭代器表示一个元素流，可以被next()函数调用并不断返回下一个元素，直到没有元素时抛出StopIteration错误。
可以把这个元素流看做是一个有序序列。但不能提前直到序列的长度，只能不断通过next()函数得到下一个元素，所以迭代器可以节省内存和空间。
迭代器和可迭代的区别:
1. 可迭代（iterable）对象，凡是可以作用于for循环的对象都是可迭代类型，即字符串、列表、元组、集合、字典、生成器、都可以放到 
for 循环里被加以处理，所以被称为可迭代对象。
2. 迭代器可以被next函数加以处理和调用，不能被其加以处理的，不是迭代器。 list,dict,str等是可迭代的但不是迭代器，
因为next()函数无法调用他们。可以通过iter()函数将它们转换成迭代器。即：迭代器一定是可迭代对象，但是可迭代对象不一定是迭代器。 
3. Python的for循环本质上就是通过不断调用next()函数实现的
'''

if __name__ == '__main__':
    test1()
    test2()
