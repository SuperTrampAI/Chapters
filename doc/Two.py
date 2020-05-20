# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 16:02
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Two.py
# @Software: PyCharm
# __create_data__=2020/5/17 16:02
# @Description: add Description

one='全局变量'


def main():
    print("start")
    # one='外层嵌套变量'
    # if elif else 语句
    age = 18  # int(input("请输入年龄："))
    if age < 18:
        print("未成年")
    elif age > 18:
        print("已成年")
    else:
        print("这是个奇怪的年龄")

    # for语句
    words = ["hello", "python", "world"]
    for word in words:
        print(word, len(word),end=",")  # 这里会有一个问题，for循环里面的end会影响后面的那个print
    print()
    print(list(range(5, 10)))# 如上问题解决，和java中一样，如果问上面的pring语句中有一个替换了end的时候，会影响下一个print，至于为什么，情况不明。

    def test():
        # one='局部变量'
        print(one)
    test()
    print("end2")


if __name__ == '__main__':
    main()
