# __author__ = 'lxh800109@gmail.com'
# __fileName__='Chapters Chapter4-process'
# __create_data__='2020/1/5 18:47'

# 各类语句
# if语句
x = 1#int(input("Please enter an integer:"))
if x<0:
    x=0
    print("Negative changed to zero")
elif x ==0:
    print("Zero")
elif x == 1:
    print("One")
else:
    print("More")

y= 'y' #input("输入姓名：")
if y=='x':
    print("该用户存在："+y)
elif y=='y':
    print("该用户存在,欢迎VIP:"+y)
else:
    print("查证你的用户再操作")

# for循环
text=['cat','window','defenestrate']
for t in text:
    print(t,len(t),end='==')
for t in text[:]: # 如果text[:]写成text,程序无法停止
    if len(t)>6:
        text.insert(0,t)
print()
print(text)

# 遍历一个数字序列
for i in range(10):
    print(i,end=",")
# range() 多参数用法：
# range(5,10) 从5开始到10截止
# range(1,20,3) 从1开始到20截止，以三步进
# enumerate()
print()
print(list(range(10)))

for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        print(n,'is a prime number')

for num in range(0,10):
    if num%2==0:
        print("取余为零：",num)
        continue
    else:
        print("取余非零：",num)

#pass 语句 该语句什么也不做。在语法上需要一个语句，但程序需要什么动作也不做时，可以使用
# 通常用于创建最小的类 另一个使用场景：在你编写新代码时，可以作为一个函数或条件子句体的占位符
# 可以让你保持更抽象的层次上进行思考
#while True:
 #   pass

a=add


