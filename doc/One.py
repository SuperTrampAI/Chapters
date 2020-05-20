# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 14:43
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : One.py
# @Software: PyCharm
# __create_data__=2020/5/17 14:43
# @Description: add Description


def main():
    print(11)
    print(26//3)
    print(r"c:\some\nest")
    print("""
        sdf
        sdf
        zxv
        sdf
    """)
    print("1"+"2")
    print('3','4')
    print("5",2*"6")
    str1='gg'
    print("sdf" "gg") # 使用场景为字符串很长的时候使用。只能最两个字面值这样操作，变量或表达式不行。
    print("sdf"[0]) # 通过索引获取字节
    print("sdfgasdzv"[0:3]) # 通过切片获取子字符串，切片的开始索引是被包含在结果中的，而结束的索引是不被包含在索引中的。
    print("切片Python"[1:4]) # 从下标1开始（结果集中包含1）到下标3结束（结果集中不包含3）
    # print("Python"[23]) 不能使用过大的索引，在切片中的索引不会报错。直接获取字符串的最大长度。
    # 使用len()函数返回字符串的长度
    lists=[1,2,3,4,5,6]
    lists.append(9)




if __name__ == '__main__':
    main()

