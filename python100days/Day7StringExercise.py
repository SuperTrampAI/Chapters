# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 16:17
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Day7StringExercise.py
# @Software: PyCharm
# __fileName__='Chapters Day7StringExercise'
# __create_data__='2020/2/16 16:17'
# @Description: add Description

# 打印杨辉三角
def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()


