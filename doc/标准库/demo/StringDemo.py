# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 15:26
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : StringDemo.py
# @Software: PyCharm
# __create_data__=2020/6/1 15:26
# @Description: add Description


def main():
    """
    String 字符串操作
    :return:
    """

    str = "{},{},{}".format("a", "b", "c")
    str = "{0},{1},{2}".format("a", "b", "c")
    str = "{2},{1},{0}".format("a", "b", "c")
    str = "{1},{2},{1}".format("a", "b", "c")
    str = "{a},{b},{c}".format(a=1, b=2, c=3)
    strs = {"a": "1", "b": "2"}
    str = "{a},{b}".format(**strs)
    # 可以的花括号中，使用.点的方式，访问参数的属性
    str = "{0[0]},{0[1]}".format((3, 5))  # 访问参数的项，
    str = '{:<30}'.format("text")  # 对其方式，以及制定宽度
    str = '{:>30}'.format("text")
    str = '{:^30}'.format("text")
    str = '{:*^30}'.format("text")
    # 0:d 0 位数 d:类型
    # 整数可用类型：b,c,d,o,x,X,n none
    # 浮点数可用类型：e,E,f,F,g,G,n % None
    str = '{0:b}'.format(42)  # 可以直接使用该方法进行一个二进制的转换。在类型前面b加个#号可以默认在前面加一个0x
    str = '{:,}'.format(1234567890)  # 使用千位分隔符
    str = "{:.2%}".format(19 / 22)  # 使用百分号
    import datetime
    str = '{:%Y-%m-%d %M:%M:%S}'.format(datetime.datetime(2020, 3, 5, 1, 2, 12))

    print(str)
    print("end")


if __name__ == '__main__':
    main()
