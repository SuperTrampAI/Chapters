# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 15:27
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Day11FileAndError.py
# @Software: PyCharm
# __create_data__=2020/2/23 15:27
# @Description: add Description

def main():
    f = None
    try:
        # r 读取 默认
        # w 写入 会先截断之前的内容
        # x 写入，如果文件存在会产生异常
        # a 追加 将内容写入到已有文件末尾
        # b 二进制模式
        # t 文本模式 默认
        # + 更新 既可以读又可以写
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
        # 如果不在finally代码块中关闭文件对象释放资源，可以使用上下文语法：通过with关键字来实现自动释放资源
        # with open('致橡树.txt', 'r', encoding='utf-8') as f:
        #     print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


# 复制文件
def copyImage():
    try:
        with open('D:\Dropbox\image\IMG_6827.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('D:\Dropbox\image\IMG_6828.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象
import json


def wJson():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()
