# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 19:54
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Chapter10ClassLib.py
# @Software: PyCharm
# __fileName__='Chapters Chapter10ClassLib'
# __create_data__='2020/1/13 19:54'
# @Description: add Description

# 操作系统接口 一定要使用import os ，而不是from os import *
import os
# 当前项目路径
print(os.getcwd())

# 对于日常文件和目录管理任务
import shutil
# 复制test1文件为test2.txt
# shutil.copyfile('F:\TestPython\/test1.txt','F:\TestPython\/test2.txt')

# 将1移动到2
# shutil.move("F:/TestPython/test2.txt",'F:/')

# 文件通配符
import glob
# 在项目目录下，查找py文件
path=os.getcwd()+"\\"
print(glob.glob(path+'*.py'))

import  sys
# 打印当前文件
print(sys.argv)

# argparse 模块 可以提取一个或多个文件名，并个选择要显示的行数
import argparse
parser=argparse.ArgumentParser(prog='top',description='show top lines from each file')

# 错误输出重定向和程序终止
# sys.stderr.write('warning og file not found starting a new one\n')
# 终止脚本的最直接的方式是使用sys.exit()

# 字符串模式匹配
import re
print(re.findall(r'\bf[a-z]*','which foot or hand fell fastest'))

print(re.sub(r'(\b[a-z]+) \1',r'\1','cat in the the hat'))

print('tea for too'.replace('too','two'))

# 数学 math模块提供对浮点数学的底层c库函数的访问
import math
print(math.cos(math.pi/4))
print(math.log(1024,2))

# 随机数
import random
# 随机返回其中的一个
print(random.choice(['apple','pear','banana']))
# 随机输出100内的，10个数
print(random.sample(range(100),10))
# 随机数：大于0，小于1
print(random.random())
# 小于六大于等于0的数
print(random.randrange(6))

# statistics 统计函数
import statistics
data=[1,2,3,4,5,6.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

# 互联网访问
# urllib.request 用户从url检索数据
# smtplib 用户发送邮件

from urllib.request import urlopen
# with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
#     for line in response:
#         line =line.decode('uft-8')
#         if 'EST' in line or 'EDT' in line:
#             print(line)

import smtplib
# server=smtplib.SMTP("smtp.aliyun.com")
# server.sendmail('lxh800109@gmail.com','3KAqDjcK3yMFN-jLps..','test python mail msg')
# server.send("test")
#
# server.quit()

from datetime import date
print(date.today())
print(date.today().strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'))
print(date.today()-date(1987,2,2))

# 数据压缩
import zlib
s=b'witch which has which witches wrist watch'

print(len(s))
print(len(zlib.compress(s)))
z=zlib.compress(s)
print(zlib.decompress(z))
print(zlib.crc32(s))

# 性能测试 timeit 模块可以在快速演示方面有优势
# profile 和pstats 模块在较大的代码块中有优势
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

print(Timer('a,b=b,a','a=1;b=2').timeit())

# 测试方法 ：用于扫描模块并验证城市文档字符串中嵌入的测试。
def average(values):
    """Computes the arithmetic mean a list of numbers

    >>> print(average([20,30,40]))
    40
    :param values:
    :return:
    """
    return sum(values)/len(values)

import doctest
doctest.testmod()

# 方法测试：unittest
import  unittest
class TestStatisticalFunction(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20,30,70]),40.0)
        self.assertEqual(round(average([1,5,7]),1),4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20,30,70)

unittest.main()


# xmlrpc.client 和 xmlrpc.server 模块实现远程过程调用
# email 包是一个用于管理电子邮件的库，用于发送和接受消息。用于构建和解码复杂的消息结构，包含附件
# json 包 用于解析json ，
# csv 模块支持逗号分隔值格式直接读取和写入文件。
# sqlite3 是sqlite数据库库的包装器，可以sql语法更新和访问数据库
# gettext,locale codecs 国际化的支持