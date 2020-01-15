# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 21:47
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Chapter11Classlib2.py
# @Software: PyCharm
# __fileName__='Chapters Chapter11Classlib2'
# __create_data__='2020/1/14 21:47'
# @Description: add Description

# 格式化输出
import reprlib

print(reprlib.repr(set('supercalifragilisticexpialidocious')))

# pprint 提供更复杂的打印控制
import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
                                                        'yellow'], 'blue']]]
pprint.pprint(t, width=30)

# textwrap 能够格式化文本段落，以适应给定的屏幕宽度
import textwrap

doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))

# locale 模块处理与特定地域文化相关的数据格式。locale模块的format函数的grouping属性，可以直接将数字格式化为带有组分隔符的样式
import locale

locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv()  # get a mapping of conventions
x = 1234567.8

locale.format_string("%s%.*f", (conv['currency_symbol'],
                                conv['frac_digits'], x), grouping=True)

# string 模块的Template类，具有适用于最终用户的简化语法。它允许用户在不更改应用逻辑的情况下，定制自己的应用
# 通过占位符实现，格式为$+字母+数字+下划线 $$ 两个$转换为一个$.
from string import Template

t = Template("test test $test1 send $$10 to $test2")
t = t.substitute(test1='test111', test2='test222')
print(t)

# 在使用substitute 方法时，如果对于占位符未赋值，则会抛出KeyError
# 使用safe_substitute 方法，如果占位符未赋值，则保留变量名
t = Template("tes test $test3 send $test4")
d = t.safe_substitute(test3='test3')
print(d)

# Template 的子类可以自定义占位符，把原有数组里面的名字，更改为以%号作为日期，照片需要和照片格式的占位符
import time, os.path
photoflies=['img1029.jpg','img1030.jpg','img1031.jpg']
class BatchRename(Template):
    delimiter='%'

# fmt=input('enter reanme style(%d-date $n-seqnum % f-formar):')
fmt='Ashley_%n%f'
t=BatchRename(fmt)
date=time.strftime('%d%b%y')
for i,filename in enumerate(photoflies):
    base,ext=os.path.splitext(filename)
    newname=t.substitute(d=date,n=i,f=ext)
    print('{} --> {}'.format(filename,newname))

# struct模块提供了pack和unpack函数，用于处理不定长度的二进制记录格式。

# 多线程
# 对于多任务协作的首选方法时将对资源的所以请求集中到一个线程中，然后使用queue模块箱该线程供应来自其他线程的请求

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')


# 日志记录
# 默认情况下，info debug消息会被压制，输出会发送到标准错误流。其他错误选项包括将消息转发到电子邮件
# 优先级：debug info warning error critical
import logging
logging.debug('debugging information')
logging.info('informational message')
logging.warning('warning:config file %n not found','server.conf') # 输出
logging.error('error occurred') # 输出
logging.critical('critical error--shutting down') # 输出

# 弱应用：python会自动进行内存管理
# weakref模块提供了可以不必创建引用就能跟踪对象。

import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']                # fetch the object if it is still alive

del a                       # remove the one reference
gc.collect()                # run garbage collection right away

d['primary']                # entry was automatically removed

# 操作列表的工具
# array 的array对象，类似于列表，但是只能存储类型一致并且存储密度更高
from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)

a[1:3]

# collections 的 deque 对象，类似于列表，从左端添加和查找的速度较快,从重建查找较慢
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

# bisect 模块 操作列表的排序

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
scores


# heapq 实现了最小值总是在位置零
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
[heappop(data) for i in range(3)]  # fetch the three smallest entries

# 十进制浮点运算：适用于精度较高的运算
from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)

round(.70 * 1.05, 2)

Decimal('1.00') % Decimal('.10')

1.00 % 0.10


sum([Decimal('0.1')]*10) == Decimal('1.0')

sum([0.1]*10) == 1.0



getcontext().prec = 36
Decimal(1) / Decimal(7)




