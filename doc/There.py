# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 23:12
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : There.py
# @Software: PyCharm
# __create_data__=2020/5/18 23:12
# @Description: add Description

def main():
    print('start')

    lists = [1, 2, 3, 4, 5, 6, 7]
    lists.extend([8, 9, 0])  # 插入另外一个list
    lists.insert(0, 0)  # 在某个下标插入某个值。
    lists.remove(0)  # 删除列表中第一个值为x的元素
    # lists.pop() # 如果pop
    print(lists)
    print(lists.index(1, 0, 5))  # 返回1所在位置的下标。

    # 元组
    people = 1, 2, 3, 4, 5
    print(people.index(2))

    # 集合
    # 创建多个元素的集合
    basket = {'apple', 'orange', 'apple', 'pear'}

    # 创建单个元素的集合
    a = set('abcabcabc')
    b = set('abcdefgabc')
    print(a^b)
    print('end')


if __name__ == '__main__':
    main()
