# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 11:36
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Day2.py
# @Software: PyCharm
# __fileName__='Chapters day2'
# __create_data__='2020/2/15 11:36'
# @Description: add Description

# 使用type检查变量类型
a = 100
b = 12.345
c = 1 + 5j
d = 'hello ,world'
e = True

print(type(a))  # 输出<class 'int'>

# 使用 内置函数对变量类型进行转换
# int() 将一个数值或字符串转换成整数
# float() 将一个字符串转换成浮点数
# str() 将制定的对象转换成字符串
# chr() 将整数转换成对于的字符串（一个字符）
# ord() 将字符串（一个字符）转换成对应的编码（整数）

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

# [] [:]	下标，切片
# **	指数
# ~ + -	按位取反, 正负号
# * / % //	乘，除，模，整除
# + -	加，减
# >> <<	右移，左移
# &	按位与
# ^ |	按位异或，按位或
# <= < > >=	小于等于，小于，大于，大于等于
# == !=	等于，不等于
# is is not	身份运算符
# in not in	成员运算符
# not or and	逻辑运算符
# = += -= *= /= %= //= **= &= `	= ^= >>= <<=`

a = 10
b = 3
a += b # 相当于：a = a + b
a *= a + 2 # 相当于：a = a * (a + 2)
print(a) # 想想这里会输出什么