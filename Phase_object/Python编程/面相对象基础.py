class Student(object):
    # 初始化操作
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % (self.name))
        else:
            print('%s正在观看爱情大电影.' % (self.name))


# 创建对象和使用对象
def main():
    stu = Student("张三", 25)
    stu.study("程序设计")
    stu.watch_movie()


# 访问可见性问题，属性和方法的访问权限只有两种，分别为公开和私有的
class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main1():
    test = Test('hello')
    # 不可访问内部方法
    # test.__bar()
    # 不可访问内部属性
    # print(test.__foo)

    # 私有属性和方法只是更换了一个名字和方法来妨碍对他们的访问
    test._Test__bar()
    print(test._Test__foo)


if __name__ == '__main__':
    # main()
    main1()
