# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 16:40
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Day8Class.py
# @Software: PyCharm
# __create_data__=2020/2/22 16:40
# @Description: add Description

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正在学习%s." % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print("%s 只能看动画片。" % self.name)
        else:
            print("%s 看非动漫电影" % self.name)


def main():
    stu1 = Student("name1", 23)
    stu1.study("python")


# 双下划线开头的为私有的变量和方法，而这种方法不被推荐。使用单下划线来表示属性是受保护的。
class Test:
    def __init__(self,foo):
        self.__foo=foo
    def __bar(self):
        print(self.__foo)
        print("__bar")


def main2():
    stu1 = Student("name2", 23)
    stu1.study("java")
    test =Test("hello")
    # 通过改变名字的规则访问私有变量
    test._Test__bar()
    print(test._Test__foo)


# 为什么需要main这个
# 当py文件被直接运行时，if下的方法被执行，当py文件以模块导入时，if下的方法不会被执行
# name 是一个内置变量。在直接运行python .py 文件时，输出结果为__main__。所以，if判断为main时，才会运行。
if __name__ == '__main__':
    main()
    main2()
