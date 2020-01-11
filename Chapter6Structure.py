# __author__ = 'lxh800109@gmail.com'
# __fileName__='Chapters Chapter6-structure'
# __create_data__='2020/1/7 18:29'
# 数据结构

list = [1, 2, 3, 4, 5, 6]
list.append(7)

print(list)
# 使用可迭代对象中的所以元素来扩展列表：把一个list增加到一个list中(增加多个)
list.extend([8, 9, 0])
print(list)

# 增加一个到list中
list.insert(len(list), 10)
list.insert(0, 11)
list.insert(0, 0)
list.insert(0, 2)
print(list)
# 删除值为X的元素
list.remove(0)
print(list)
# 删除给定位置的元素
list.pop(1)
print(list)
# 清空列表中的所以元素
# list.clear();
# 返回列表中的第一个值为X的元素的从零开始的索引，如果没有，抛出valueError异常
# index中还可以指定参数：从哪个下标开始and结束，并在这个子集中返回下标
print(list.index(4))
print(list.index(2, 0, 4))
# 返回元素X在列表中出现的次数
print("2出现的次数：", list.count(2))
# 排序
print(list.sort())
# 翻转列表中的元素
print(list.reverse())
# 浅拷贝
list.copy()
print(list)
# pop方法为删除该值，并返回该下标的值。取得最后一个值
# 列表作为栈使用:先进后出
print(list.pop())
# 列表作为队列使用：先进先出。
# 这种方法现在很慢，如果要删除前一位，要把改元素后面的所以元素往前移动一位
from collections import deque

queue = deque(["1", "2", "3"])
queue.append("4")
queue.append("5")
print("使用collections 实现队列：删除的元素为：", queue.popleft())
print(queue)
# 通过列表推导式来创建列表 语法：一个表达式，后面跟一个for子句，然后是零个或多个for或if子句。
squares = []
# for x in range(10):
#   squares.append(x**2)
# squares = list(map(lambda x: x**2, range(10)))
squares = [x ** 2 for x in range(10)]  # 这三种方法等同
print(squares)
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
# 上一行等同于等同于如下：
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

# 实例：
vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec])  # 如果表达式是一个元祖，那么就必须加上括号
print([x for x in vec if x >= 0])  # 第一个x为表达式 一个x的值为for 后面x的值
freshfruit = ['  banana', '  loganberry', "passion fruit  "]
print([weapon.strip() for weapon in freshfruit])  # 使用str类型的strip方法去掉前后空格
print([(x, x ** 2) for x in range(6)])
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])
from math import pi

print([str(round(pi, i)) for i in range(1, 6)])

matix = [[1, 2, 3, 4], [5, 6, 7, 8, 9], [9, 10, 11, 12]]
print([[row[i] for row in matix] for i in range(4)])
# 实际应用不会使用如上的方式，而是使用如下的方式：
# print(list(zip(*matix)))# 在该文件中，由于上面已经有了一个list变量，所以有冲突
a = [1, 2, 3, 4, 5, 6, 7, 8]
del a[0]
print(a)
del a[2:4]  # 删除从下标2开始，包含该下标，到下标为4的，不包含该下标
print(a)
del a[:]  # 清空列表
del a  # 删除变量

# 元组 一个元组有几个逗号分隔的值组成
# 赋值时圆括号可有可无；在元组是更大一个表达式的一部分时，就需要圆括号。
# 给元组中的一个单独的元素赋值时不允许的，接口办法是创建一个包含可变对象的元组。比如list
# 创建一个空元组：empty()
# 创建一个包含一个元素的元组：singltion='1', 在元素后面加一个逗号
t = 1, 2, 3, 4, 5, 6, '123'
print(t)

# 列表和元组的区别
# 元组是immutable ，通常包含不同类型的元素，并且通过解包或索引来访问，如果是namedtuples可以通过属性访问
# 列表是mutable 一般是同类型的元素，通过迭代访问

# 集合：集合是有不重复组成的无序的集。基本用法包括成员检测和消除重复元素。支持各种数学运算
# 创建方式：花括号或set()  创建空集合只能使用set() 而不能{}，后者是创建一个空字典
# 例子：
# 创建集合 set和{} 是有区别的
baskst = {'1', '2', '3', '4', '5', '6', '7'}
basket2 = {1, 2, 3, 4, 5, 6, 7, 8}
# 集合中是否包含一个元素
print('12' in baskst)

a = set("11234567890")
b = set("1890")
print(a)  # 输出{'1', '9', '2', '0', '7', '6', '8', '3', '5', '4'} 去除掉重复元素
print(a - b)  # 输出不同的元素
print(a & b)  # 输出相同的元素
print(a ^ b)  # 输出在两个集合中，只出现过一次的
# 集合的推导式形式
a = {x for x in "asdfglkjzcv" if x not in 'agf'}
print(a)

# 字典：在其他语言里可能被叫做联合内存或联合数组or Map：键值对的集合，键必须唯一
# 字典以关键字为索引，关键字可以是任意不可变类型，通常是字符串或数字。
# 可以改变的不能用来做为字典的关键字
# 创建方式： 创建一个空字典：{}；创建键值对：{1:2,3:4}
# 创建方式：dict([("",""),("","")])
# 常用方法：del ；默认使用插入顺序排序，字母排序：sorted。使用in判断该键
# 常用方法：使用list将会返回包含该字典所以键的列表
# 使用同一个键来存储新值，原有的值会被覆盖。如果键不存在，会报错。
dict([("", ""), ("", "")])
{x: x ** 2 for x in (2, 4, 6)}
dict(sape=123, guido=123, jack=123)

# 遍历字典map 使用items方法
knights = {'gallahad': 'the qure', 'roin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 使用enumerate 方法把索引位置和对应的值取出
for i, v in enumerate(knights):
    print(i, v)

# 循环多个map，把下标相同的输出到一列
questions = ['name', 'quest', 'favorite clolr']
answers = ['lancelot', 'the holy grail', 'blue']
for q, z in zip(questions, answers):
    print("{0}，{1}".format(q, z))
# 逆向循环
for i in reversed(range(1, 10, 2)):
    print(i, end=",")
# sorted()：按照某个指定顺序循环一个序列，可以在不改动原序列的基础上返回一个新的排好序的序列
baskset = ['apple', 'orange', 'apple', 'pear', 'banana']
print()
print(baskset)
print(sorted(baskset))
print(sorted(set(baskset)))  # 把basket放入到set中，去处重复元素，并按照字母排序

# 循环时修改列表内容，创建一个新列表是比较安全和简单的
# 把原有列表中的值，经过筛选以后，加入到另一个新列表中
import math
raw_data=[45.2,float("NaN"),12.2,34.2,float("NaN"),236.6]
filtered_date=[]
for value in raw_data:
    if not math.isnan(value):
        filtered_date.append(value)

print(filtered_date)

# 条件控制
# in or not in 校验一个值是否在或不在一个序列里
# is or is not 比较两个对象是不是同一个对象，这只对像列表这样的可变对象比较重要。
# 比较操作可以传递：a<b==c 会校验是否a小于b并且b相等于c

# 可以通过and 和or来组合 称为短路运算符，他们的参数从左到右解析，一旦可以确定结果解析就会停止
# 使用not来取反 这些操作符的优先级低于比较操作符，他们之中
# not优先级最高，or优先级最低。因此a and not b or c 等价于(a and (not b)) or c
# 当用作普通值而非布尔值时，短路操作符的返回值通常是最后一个变量
non_null="1" or "2" or "c"
print(non_null)
# 比较序列和其他类型
print((1, 2, 3)< (1, 2, 4))
print([1,2,3]<[1,2,4])
print('ABC'<'C'<'Pascal'<'Python')
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)