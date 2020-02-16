# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 13:33
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Day5.py
# @Software: PyCharm
# __fileName__='Chapters day5'
# __create_data__='2020/2/16 13:33'
# @Description: add Description

"""
找出100~100的水仙数
"""
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

"""
正整数的反转
"""
num = int(input("num="))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

"""
百钱百鸡
"""
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (x, y, z))

