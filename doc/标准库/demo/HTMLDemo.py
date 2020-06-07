# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 23:24
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : HTMLDemo.py
# @Software: PyCharm
# __create_data__=2020/6/2 23:24
# @Description: add Description
from html.entities import name2codepoint
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag :", tag)

    def handle_data(self, data):
        print("Data :", data)

    def handle_comment(self, data):
        print("comment:", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named end:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent :", c)

    def handle_decl(self, decl):
        print("Decl     :", decl)


def main():
    # 创建一个能解析无效标记的解析器实例
    # 参数：*    convert_charrefs=True（默认值为True，则所以字符引用都会自动转换为相应的unicode字符，script和style除外）
    parser = MyHTMLParser()  # 解析出尖括号中的标签
    # feed：田中一些问道到解析器中。如果包含完整的元素，则被处理.如果数据不完整，将被缓冲知道更多的数据被填充
    parser.feed('<html><head><title>Test</title></head><body><h1>Parse me !</h1></body></html>')
    # data = parser.feed('<中文></中文>') 中文无法识别。
    parser.feed("&gt;&#62;&#x3E;")


if __name__ == '__main__':
    main()
