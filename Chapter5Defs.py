# __author__ = 'lxh800109@gmail.com'
# __fileName__='Chapters Chapter5-defs'
# __create_data__='2020/1/5 19:33'

def add(a, b): # def 引入一个函数定义，后面跟函数名和带括号的形式参数列表。函数体从下一个开始
    """可选的文档说明

    如果有多行，第二行为空行
    """
    # 在方法中的变量为局部变量
    # 变量的引用顺序：局部变量> 外层函数的局部符号表>全局符号表>内置名称的符号表
    #全局变量和外层函数的变量不能再函数内部赋值，可以引用。除非使用globle或nonlocal
    return a + b;
print(add(1,2))
print(add.__doc__)

def fib(n):
    """Return a list containing the Fibonacci series up to n."""
    result =[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result

def ask_ok(prompt,retries=4,reminder="Please try again!"):
    while True:
        ok=input(prompt)
        if ok in('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):# in 是否包含一个值
            return False
        retries=retries-1
        if retries<0:
            raise  ValueError('invalid user response')
        print(reminder)

i=3
def f (arg=i):
    print(arg)
i=4;
f()

# 使用关键字参数调用函数
#d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
def parrot(voltage,state="a stiff",action="voom",type="Norwegian Blue"):
    print(voltage)
    print(state)
    print(action)
    print(type)
parrot("a million","beraft of life","jump")# 参数类型必须匹配，顺序不重要

def cheesesshop(kind,*arguments,**keywords):
    for arg in arguments:
        print(arg)
    print("-"*40)
    for kw in keywords:
        print(kw,":",keywords[kw])
# *arguments 为可变参数。**keywords 当该函数接受的参数使用key-value形式接受时，同时该方法没有
# 同名的形参时，**keywords 接受所有的参数
cheesesshop("sdf","test","sdf","sdfss",test="testS")

def concat(*args,sep="/"):
    return sep.join(args)

print(concat("a","b",'c',sep="."))

args=[3,5]
print("*"*20)
print(list(range(*args)))

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

print(parrot(**d))

# lambda
def make_incrementor(n):
    return lambda x:x+n
f=make_incrementor(42)
print(f(0))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

#函数标注 形参的标注为在形参后面:str，返回结果的标注为在函数的冒号前标注
def f(ham:str,eggs:str="eggs")->str:
    return ham+"and"+eggs;
