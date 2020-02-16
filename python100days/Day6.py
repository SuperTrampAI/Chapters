# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 14:07
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Day6.py
# @Software: PyCharm
# __fileName__='Chapters Day6'
# __create_data__='2020/2/16 14:07'
# @Description: add Description

import math
m=int(input("m="))
n=int(input("n="))
print(math.factorial(m)//math.factorial(n)//math.factorial(m-n))

# 函数的参数可以有默认值，也支持使用可变参数，python不需要想其他语言一样支持函数的重载
# 在定义春城额函数的时候就可以让它有多种不用的使用方式

from random import randint

def roll_dice(n=2):
    """

    :param n:
    :return:
    """
    total=0
    for _ in range(n):
        total+=randint(1,6)
    return total

def add (a=0,b=0,c=0):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    return a+b+c

# 使用：
# 如果没有指定参数，则默认摇两颗色子
print(roll_dice())
# 可以传入参数摇动指定的色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))

# 使用可变参数来进行n个参数的相加
def add_angae(*args):
    totle=0
    for val in args:
        totle+=val
    return totle

# python 中每个文件就代表了一个模块
# 使用import 导入指定的模块
# 比如在module1.py中有一个函数foo()
# 在要调用的文件中，使用该语法调用：from module1 import foo
# foo()
# 可以在import导入时，给模块取个别名
# import module1
from python100days.Module1 import foo
foo()