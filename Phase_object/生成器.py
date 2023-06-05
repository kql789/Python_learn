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
for x in range(4):
    print(next(g3))  # 当比那里到最后一个时，再次遍历则进行报错
