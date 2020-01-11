print("Hello Python World")

# 类名不能使用-，现在导致的后果是无法在另一个类中无法import。
# 类名使用UpperCamelCase命名 UpperCamelCase
#
import Chapter6method
Chapter6method.fib(1000)
print(Chapter6method.fib2(100))
print(Chapter6method.__name__)
# 把一个函数赋值给一个变量
fib = Chapter6method.fib;
fib(1000)

# 从Chapter6method导入fib2，fib方法
from Chapter6method import fib2,fib
# 从Chapter6method导入其中的所有方法,该用法不被推荐，因为这通常会导致代码的可读性很差。
from Chapter6method import *
# as 给导入的类名取个别名
import  Chapter6method as chapt

import sys
# sys dir() 用于查找模块定义的名称，返回一个排序过的字符串列表
print(dir(Chapter6method))
print(dir(sys))

# 列出内置函数和标量的名称
import  builtins
print(dir(builtins))
# 导入模块方法1
import sound.effects.wavread
print("sound.effects.wavread 包下的方法调用：")
sound.effects.wavread.fib(1000)
# 导入模块方法2
from sound.effects import  wavread
wavread.fib(1000)
# 导入模块方法3
from sound.effects.wavread import fib,fib2
fib(800)

