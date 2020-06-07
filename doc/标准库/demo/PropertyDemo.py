# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 15:23
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : PropertyDemo.py
# @Software: PyCharm
# __create_data__=2020/5/31 15:23
# @Description: add Description


class C:
    def __init__(self):
        self._x = None

    # 在一个方法上面，定义如下注解，在后续方法中，会自动生成set，get，doc，del等方法、注解
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


def main():
    print('end')


if __name__ == '__main__':
    main()
