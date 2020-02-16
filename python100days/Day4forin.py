# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 15:42
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Day4forin.py
# @Software: PyCharm
# __fileName__='Chapters day4forin'
# __create_data__='2020/2/15 15:42'
# @Description: add Description

# 如果明确的知道循环的次数，或要对一个容器进行迭代，推荐使用for-in循环

# range() 函数
# range(101) 可以产生一个0到1的整数序列
# range(1,100) 1-99
# range(1,100,2) 1-99 步长为2

"""
用for循环实现1~100之间的偶数求和
"""
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)

"""
猜数字游戏：计算机出一个1~100之间的随机数由人来猜，计算机根据人猜的数字来给出
对应的提示
"""
import random

answer = random.randint(1, 100)
answer=0 # 写死0
while True:
    number = int(input("请输入："))
    if number < answer:
        print("数再大一点")
    elif number > answer:
        print("数再小一点")
    else:
        print("猜对了！")
        break
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

from math import sqrt
print(int(sqrt(123)))
