import time
import functools

'''

题目：
创建装饰器， 要求如下：
1.创建add_log装饰器， 被装饰的函数打印日志信息；
2.日志格式为: [字符串时间] 函数名: xxx， 运行时间：xxx,
运行返回值结果:xxx
'''


def add_log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('[%s] 函数名：%s，运行时间：%.6f,运行返回值结果:%d' % (time.ctime(), func.__name__, end_time - start_time, res))
        return res

    return wrapper


@add_log
def add(x, y):
    time.sleep(1)
    return x + y


'''
题目：
编写装饰器required_ints, 条件如下:
1). 确保函数接收到的每一个参数都是整数; # 如何判断变量的类型?
type(s), isinstance(s,str)
2). 如果参数不是整形数， 抛出异常raise TypeError(“参数必须为整形”)
'''


def required_list(func):
    def wrapper(*args, **kwargs):
        for arg in args + tuple(kwargs.values()):
            if not isinstance(arg, int):
                raise TypeError('参数必须为整型')
            else:
                return func(*args, **kwargs)

    return wrapper


@required_list
def sum_add(*args, **kwargs):
    return sum(args + tuple(kwargs.values()))


'''
题目：
编写装饰器required_types, 条件如下:
1).当装饰器为@required_types(int,float)确保函数接收到的
每一个参数都是int或者float类型;
2).当装饰器为@required_types(list)确保函数接收到的每一个
参数都是list类型;
3).当装饰器为@required_types(str,int)确保函数接收到的每
一个参数都是str或者int类型;
4).如果参数不满足条件,打印 TypeError:参数必须为xxxx类型
'''


def required_types(*kinds):
    def required_ints(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, kinds):
                    print('TypeError:参数必须为:', kinds)
                    break
                else:
                    res = func(*args, **kwargs)
                    return res

        return wrapper

    return required_ints


@required_types(int, int)
def judge_number(a, b):
    return a, b


if __name__ == '__main__':
    # print(add(1, 10))
    # print(sum_add(1, 2, 3, 65, 67, 5, a=1, b=2))
    print(judge_number(2, 'a'))
