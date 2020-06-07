# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 17:20
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : TurtleDemo.py
# @Software: PyCharm
# __create_data__=2020/6/2 17:20
# @Description: add Description
import turtle
import time

def Image():
    # 同时设置pencolor=color1, fillcolor=color2
    turtle.color("red", "yellow")

    turtle.begin_fill()
    for _ in range(50):
        turtle.forward(200)
        turtle.left(170)
        turtle.end_fill()

    turtle.mainloop()


def main():
    turtle.right(90)
    turtle.forward(200)

    turtle.left(90)
    turtle.forward(200)

    turtle.mainloop()
    print("end")


if __name__ == '__main__':
    main()
