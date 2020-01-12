#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/11 17:29
# @Author  : Marko Li
# @Site    : 
# @File    : Chapter7Ipop.py
# @Software: PyCharm
# @Description: add Description

# ip:input op:output
# 方式一 使用{} 占位符输出
year = 2020
month = 11
day = 11
print(f"today:{year}，{month}，{day}")
# 方式二：使用str.format()方法
yes_votes = 42_572_654
no_votes = 43_123_343
print(yes_votes)
percentage = yes_votes / (yes_votes + no_votes)
# 前面一个{}里面的看似没用，通过第二个{}里面的.3 来控制输出的小数点后面的几位：四舍五入
print("{:-1} YES votes  {:.3%}".format(yes_votes, percentage))
# 字符串切片和连接操作完成所有的字符串处理，任何可以想到的任何连接方式
# 把其他类型的转换成字符串：repr() 和str()
# str和repr的区别：str函数返回人类可读的值表示的，repr生成解释器可读的表示。

# :.3f 取float小数点后面多少位
import math

print(f"the value of pi is pproxmately {math.pi:.3f}")

table = {'Sjoed': 123, 'teaf': 34, '2345': 34345}
for name, phone in table.items():
    print(f'{name:10}==> {phone:10d}')

# !a !s !r
animals = 'eels'
# 把‘’输出
print(f'my hovercraft is full of {animals!r}')

# 字符串的format方法
print('we are the {} who say "{}!"'.format("Marko", " Li"))
print('{0} nad {1}'.format("spam", "eggs"))
print('thie {} is {} .'.format("123", "456"))
print('thie {food} is {adj} .'.format(food="123", adj="456"))
print('Sjoed:{[Sjoed]}'.format(table))

for x in range(1, 11):
    print('{:2d},{:3d},{:4d}'.format(x, x * x, x * x * x))
# str.zfill()
print('12'.zfill(4))
print('-12'.zfill(4))
# 如果位数足够了，就不在填充
print('3,12314123123'.zfill(5))

print("the vale of pi is approximately %.3f" % math.pi)

# 读写文件
# open(filename ,mode) 第一个参数是包含文件名的字符串，第二个参数包含一些描述文件使用方式
# mode可以是r：只读，w：只能写入；a：打开文件在文件末尾以追加内容 r+：打开文件进行读写。
# mode默认为r
# f=open("D:\software_learn\PycharmProjects\Chapters\key.txt",'r')
with open("key.txt",'r',encoding='UTF-8') as f:
    # 当size被省略或者为负数时，将读取并返回整个文件的内容，文件大小是机器内存的两倍时，出现问题
    read_data = f.read()
f.closed

# rb+
f=open("D:\software_learn\PycharmProjects\Chapters\key.txt",'a',encoding='UTF-8')
# print(f.read())
# print(f.readline())
#f.closed
# 从文件中读取行
#for line in f:
 #   print(line,end='')

# 在写入其他类型的对象以前，需要把他们转换成字符串（在文本模式下）或字节对象（在二进制模式下）
value=("the answer",42)
s=str(value)

# f.write("test write text")
#for line in f:
 #   print(line,end='')
 # tell返回一个整数，给出文件对象在文件中的当前位置，表示为二进制下时从文件开始的字节数，以及文本模式下的意义不明的数字
print(f.tell())
# 改变文件的对象的位置 f.seek(offset,whence) whence :0文件开头/1当前文件/2文件末尾：
# whence 表示从文件的哪个位置开始
f.closed

# json
import  json
# 将对象转换成json对象
print(json.dumps([1,'simple','list']))
# 将对象序列号成text file
json.dump(x,f)
# 将json返序列化成字典
# x=json.loads()

test_dict = {'a': 1, 'b': 2}

# 把字典转成json字符串
json_text = json.dumps(test_dict)
print(json_text)

# 把json字符串转成字典
json_dict = json.loads(json_text)
print(json_dict)