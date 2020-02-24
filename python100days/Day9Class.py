# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 0:05
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Day9Class.py
# @Software: PyCharm
# __create_data__=2020/2/23 0:05
# @Description: add Description
from time import time, localtime, sleep


class Person(object):
    # doc
    # 动态语音可以在程序运行时，给对象绑定新的属性和方法。也可以对已经绑定的进行解绑，
    # 通过__slots__ 变量来限定对象只能绑定某些类型
    # 该限定只对当前类的对象生效。对子类并不起任何作用
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    __slots__ = ("_name", "_age", "_gender")

    @staticmethod
    def is_test(self):
        return True

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # get 方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # set方法
    @age.setter
    def age(self, age):
        self._age = age

    def print(self):
        print(self._name, self._age)
    # is-a 继承或泛化，学生和人的关系，手机和电子产品的关系
    # has-a 关联 部门和员工，汽车和引擎
    # use-a  依赖  司机有一个驾驶的行为（方法），其中的参数使用到了汽车，那么司机和汽车就是依赖关系

    # 重写语法： class Student(Person):

    # 使用abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果


from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


def main():
    person = Person("李小璐", 34)
    person.print()
    print(person.name)
    person.age = 22
    person.print()


if __name__ == '__main__':
    main()
