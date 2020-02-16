# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 15:51
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Day7String.py
# @Software: PyCharm
# __fileName__='Chapters Day7String'
# __create_data__='2020/2/16 15:51'
# @Description: add Description

# 使用三个引号的可以换行
str1 = """
123
345
567
"""
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = 'hello ' * 3
print(s1)  # hello hello hello
s2 = 'world'
s1 += s2
print(s1)  # hello hello hello world
print('ll' in s1)  # True
print('1234' in s1)  # False
str2 = '456789'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2])  # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])  # c12
print(str2[2:])  # c123456
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 654321cba
print(str2[-3:-1])  # 45

str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1))  # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize())  # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title())  # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper())  # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or'))  # 8
print(str1.find('shit'))  # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He'))  # False
print(str1.startswith('hel'))  # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))  # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = '345677'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = ' lxh800109@gmail.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

# list = [] 列表
# t=( '',123,True) 元组
# set ={} 集合
# 字典： scores={"age":12}
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    print(content[1:])
    print(content[0])
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()

import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def max2(x):
    """
    传入列表并返回列表中最大和第二大的元素的值
    :param x:
    :return:
    """
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


# ---------------------------
def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))

