# __author__ = 'lxh800109@gmail.com'
# __fileName__='Chapters Chapter2'
# __create_data__='2019/12/29 17:04'

# 加减乘除  混合类型运算会将结果的类型转换成最高的那个。比如有int和double，运算的结果会是double
print(2+2)
print(50-4*5)
print((50 - 5*6) / 4)
print(8 / 5)
# // 双斜杠忽略小数部分
print(9//4)
# 取得余数
print(9%4)
# 乘方
print(2**3)

# 变量
num=1
num1=2
print(num+num1)

# 字符串  在前面加一个r，可以使得\不在转义 字符串不能修改
text="ABCDEFGHIJKLMNOPKRSTUVWXYZ"
print(r'C:\some\name')

# 该位置的\可以去掉换行
print("""\
    test
    testtest
    test
""")

# 使用* 可以对字符串进行重复
print(3*'un'+"ium")

# 两个相邻的会自动连接在一起, 只能是字面量，不能是变量，不能是表达式，连接的不是两个字面量时，使用+号连接
prefix="1"
print("test" "test2")

print(prefix+"test")

# 根据下标去字符串是的值
# 字符串的下标从0开始（0和-0是一样的），也可以从负数开始，起点为-1
print(text[-1])
# 字符串的切片：从字符串中获得子字符串
# 下标也是从0开始
print(text[0:4])# 从哪个下标开始，第二个参数为截止的下标
print(len(text))# 返回字符串长度


