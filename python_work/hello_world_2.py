# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 22:22
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : hello_world_2.py
# @Software: PyCharm
# __fileName__='Chapters hello_world_2'
# __create_data__='2020/1/16 22:22'
# @Description: python_work 文件根据《python 编程 从入门到实践》改编

# python_word 文件夹下面的文件，为书籍《python 编程 从人坑到实践》

# python 运行hello world 发生了什么

name = ' ada lovelace '
# title 方法将首字母转变成大写
print(name.title())
# upper 全部转变成大写
print(name.upper())
# lower 全部转变成小写
print(name.lower())

# 删除两端的空格
print(name.strip())
# lstrip 删除开头的空格
# rstrip 删除结尾的空格
# \t 空格 \n 换行

# 为什么带小数点的数叫浮点数
# 解决问题的办法有多个 Perl

# 在不知道列表长度的情况下，可以访问最后一个元素
# lists[-1] 访问最后一个元素 [-2] 倒数第二个元素

# lists.insert([],'')

# del lists[0] 删除元素

# pop 在原有list中弹出，并返回，可以返回，通过一个新的变量保存

# 根据值从list中删除：lists.remove('value') 只会删除在list中遇到的第一个值，如果要删除多个，需要循环删除

cars = ['toyota', 'byt', 'hq', 'bmw', 'bab']

cars.sort()
print(cars)  # 根据大小写字母排序

# sort 的参数 reverse =True 按照字母倒叙排序
cars.sort(reverse=True)
print(cars)

# sorted() 函数对列表进行临时排序，不影响原有列表中元素的位置




