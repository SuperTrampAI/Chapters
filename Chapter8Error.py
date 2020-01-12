#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 13:07
# @Author  : Marko Li
# @Site    : 
# @File    : Chapter8Error.py
# @Software: PyCharm
# @Description: add Description

# 错误和异常 在pycharm中将无法通过编译，在未编译前，就已经出现问题
# 而异常则是出现在运行时

# python中的异常处理
# try except
# 语法：try: 语句 break except ValueError: 语句
# 含义：首先执行try中的代码，如果没有发生异常，则跳过except中的代码
# 如果发生了异常，则跳过发生错误那行代码以后的代码，和except异常类型匹配的代码继续执行
# 然后继续执行try中的代码
# 如果和except中的异常类型没有匹配到的，则抛出异常。如果没有找到处理的程序，则ta就是一个未处理的异常
# 一个try可以包括多种异常，但是最多只会处理一种异常，一个except写多个error的语法：except(RuntimeError,TypeError,NameError)
while False:
    try:
        num = int(input("Please enter a number:"))
        break  # 跳出当前循环
    except:
        print("Oops! that was no valid number ,try again..")


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

import sys

# else 语句必须放在所有的except子句后面，用途：对于在try子句不引发异常时，必须执行的代码
# 如果try中发生异常，则else中的代码不执行
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# 异常参数的设置
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    x, y = inst.args
    print('x=', x)
    print('y=', y)


# 处理调用方法内部的错误
def this_fails():
    x = 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print("handling run-time error:", err)


# 抛出异常
# 强制发生指定的异常：raise的唯一一个参数是一个异常实例，或是一个异常类：派生至exception的类
# raise NameError('HiThere')

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('an exceptioin flew by')
#     raise  # 重新引发异常


# 自定义异常类
# 常用做法：在创建可能应发多个不同错错误的模块时，通常的做法是为该模块定义的异常创建基类
# 并为不同错误条件创建特定的异常类的子类
class Error(Exception):
    """Base class for exceptions in this module"""
    pass


class InputError(Error):
    """Ecxeption raised for error in the input

    Arrtibutes:
        exexpression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Arrtibutes:
        previous -- state at beginning of transtion
        next --
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


# finally语句
# 关于finally的一些复杂情况：
# 1.在try发生异常，如果异常没有在except中处理，则异常在finally中重新引发
# 2.异常可能在except和else中发生，同样的，该异常会在finally执行后被重新应发
# 3.try语句中，遇到一个break，continue 或return语句，则finally子句则在执行这三个语句之前被执行
# 4.finally 中有return语句时，则finally子句的return语句将在只看try子句的return语句之前取代后者被执行

# 关于情况4的例子：
def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())  # 输出finally中的false

def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is',result)
    finally:
        print('executing finally clause')
# 预定义的清理操作：with语句的使用
# 使得类似于像文件对象，确保它们得到及时和正确的清理
with open('filepath.txt') as f:
    for line in f:
        print(line,end='')
# 在执行完语句后，记事在处理时遇到问题，文件f也始终会被关闭


