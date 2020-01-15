# __author__ = 'lxh800109@gmail.com'
# __fileName__='Chapters Chapter3-List'
# __create_data__='2020/1/5 17:49'

# 一组列表可以包含不同类型的元素，但是通常使用时哥哥元素类型相同 ,列表的值可以通过下标改变
squares = [1, 2, 3, 4, 5, 6, 7]
# 索引
print('根据索引取值：', squares[0])
# 切片 所有的切片都返回一个新列表
print('获取所有元素：', squares[0:])
# 如下会返回列表的一个的新的浅拷贝
print('浅拷贝：', squares[:])
# 使用+做拼接操作
print('拼接list：',squares + [8, 9, 0])
# 使用append()做拼接操作
squares.append(10)
print(squares)
# 把第三个到六个替换 ；从下标2开始的的三个，包含下标为2的
squares[2:5] = [12, 13, 14]
print(squares)
# 清空下标2开始的三个
squares[2:5] = []
# 清空整个list
squares[:] = []
print(len(squares))

# 多层集合
letters = [[1, 2, 3, 4], ['a', 'b', 'c', 'd']]
print(letters[0])
print(letters[1])

a, b = 0, 1
while a < 10:  # 任何非零整数都为真，零为假。
    print(a)  # print()方法的参数end=',' 可以用来取消后面的换行，或者可以用其他字符来分割
    a, b = b, a + b
