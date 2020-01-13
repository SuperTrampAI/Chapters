#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 15:24
# @Author  : Marko Li
# @Site    : 
# @File    : Chapter9Class.py
# @Software: PyCharm
# @Description: add Description

# 关于类的定义：
# 组合数据和功能的方法，每个类的实例可以保存自己状态的属性。一个类的实例也可以有改变自己状态的方法
# python的提供面向对象的所有标准特性，类继承机制运行多个基类。派生类可以覆盖它基类的任何方法
# 一个方法可以调用基类中相同名称的方法
# 对象可以包含任意数量的数量和类型的数据
# 在运行时创建，可以在创建后修改

# 名称和对象
# 对象具有个性，多个名称（在多个作用域内）可以绑定到同一个对象。

# 作用域和命名空间
# namespace（命名空间）是一个从名字对对象的映射。
# 命名空间买例子：专放内置函数的集合，模块中的全局名称，函数调用中的局部变量。从某种意义来说，对象的属性集合也是一种命名空间的形式
# 在不同时刻创建的命名空间拥有不同的生存期
# 包含内置名称的命名空间是在python解释器启东时创建，永远上被删除。
# 模块的全局命名空间在模块定义被读入时创建。通常，模块命名空间也会持续到解释器退出
# 一个函数的本地命名空间在这个函数被调用时创建，并在函数返回或抛出一个不再函数内部处理的错误时被删除

# 一个作用域是一个命名空间可直接访问的python程序的文本区域，
# 对于 可直接访问意味着对名称的非限定引用会尝试在命名空间中查找名称
# 查找顺序：
# 1.最先搜索的最内部作用域包含局部名称
# 2.从最近的封闭作用域开始搜索的任何封闭函数的范围包含非局部名称，也包括非全局名称
# 3. 倒数第二个作用域包含当前模块的全局名称
# 4.最外面的范围是包含内置名称的命名空间

# 使用nonlocal 声明为非本地变量
# 如果不存在生效的global语句--对名称的赋值总是进入最内层作用域。

# global语句可被用来表明特定变量生存于全局变量并且在其他被重新绑定。
# nonlocal语句表明特定变量生存与外层作用域中并且在其他被重新绑定

def test():
    b = 200
    def test2():
        b = 100
        print(b)
    test2()
    print(b)

b = 300
print(b)

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# ---------------------------
# 类

class MyClass:
    """A sim[le example class"""
    i=12345
    def f(self):
        return 'hello world'
    def __init__(self):
        self.data=[]

# 类的实例化
x=MyClass()

class Complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart

x=Complex(3,2)
print(x.i,x.r)

x.counter=1
while x.counter<10:
    x.counter=x.counter*2
print(x.counter)
del x.counter

# 继承
# 如果请求的属性在类中找不到，搜索将转到基类中进行查找，如果基类本身也派生自其他类
# 则此规则将递归地应用
# python有两个内置函数可被用于继承机制
# isinstance() 检查一个实例的类型isinstanc(obj,int)仅会在obj.__class__为int或某个派生自int的类时为True
# 使用issubclass()来检查类的继承关系，issubclass(bool,int)为True，因为bool是int的子类，但是，issubclass(float,int)为float不是int的子类

# 多重继承：在最简单的情况下，你可以认为搜索从父类所继承属性的操作是：
# 深度优先，从左至右的。

# python中不存在私有变量
# 使用约定来定义私有变量：_ 下划线

# 名称改写：去掉下划线，名称改写有助于让子类重载方法而不破坏类内方法调用
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

# 创建一个空类，用于把一些命名数据绑定在一起
class Employee:
    pass
john=Employee()
john.name=""
john.salary=""



# 各种list 的迭代方式：
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
#for line in open("myfile.txt"):
 #   print(line, end='')


# for语句会调用容器对象的iter()，该函数返回一个__next__方法的迭代器对象
# 改方法会逐一访问容器中的元素，当元素用尽时，__next__()将会引发StopInteration异常来通知充值for循环

s='abc'
it=iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
#print(next(it))

class Reverse:
    """Interator for looping over a sequence backvards."""
    def __init__(self,data):
        self.data=data
        self.index=len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index=self.index-1
        return self.data[self.index]

r=Reverse("span")
print(iter(r))

for char in r:
    print(char)

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse("golf"):
    print(char)



sum(i*i for i in range(10))                 # sum of squares


xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product


from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

unique_words = set(word  for line in page  for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
