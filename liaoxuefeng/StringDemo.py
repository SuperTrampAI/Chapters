# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 16:23
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : StringDemo.py
# @Software: PyCharm
# __create_data__=2020/6/5 16:23
# @Description: add Description
import functools


def main():
    print(len('e'.encode('utf-8')))  # 中文为三个字节，英文为一个字节。
    print(len("中"), len('B'))  # 而对于字节使用len方法来说，中英文是一样的。
    t = (1, 2, [3, 4])  # 元组本身不可变，而如果在元组中包含了可变的元素，该可变元素时可变的。
    t[2][0] = 5
    t[2][1] = 6
    import os
    print([d for d in os.listdir('..')])  # 列出某个目录下的文件和文件夹名。使用的应该是相对路径的定位方式。

    print('end')


# 带参数的装饰器
def log(text):
    def decorator(func):
        @functools.wraps(func)  # 把原始函数的__name__等属性复制到wrapper()函数中，放置依赖函数签名的代码执行报错
        def wrapper(*args, **kw):
            print("%s %s()" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log("text")
def now():
    print("now()")


if __name__ == '__main__':
    now()
    main()
