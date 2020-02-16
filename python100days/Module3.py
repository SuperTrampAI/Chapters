# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 15:36
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Module3.py
# @Software: PyCharm
# __fileName__='Chapters Module3'
# __create_data__='2020/2/16 15:36'
# @Description: add Description

def foo():
    pass


def bar():
    pass


# __name__ 是python中一个隐含的变量 他代表了模块的名字
# 只有被python解释器直接执行的模块的名字才是__main__
if __name__ == "__main__":
    print("call foo()")
    foo()
    print("call bar()")
    bar()


# python查找标量的顺序：局部作用域，嵌套作用域，全局作用域，内置作用域
# 使用关键字：global 来指明函数中变量是全局变量
# 使用nonlocal 关键字指明变量是嵌套作用域

# 减少对全部变量的使用：全局变量比局部变量拥有更长的生命周期，导致无法被垃圾回收。同时也是在较低代码之间的耦合。

# 按照下面的格式进行书写：
def main():
    # Todo:Add your code here
    pass


if __name__ == "__main__":
    main()

