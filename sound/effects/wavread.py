print("wavread.py")

# __author__ = 'lxh800109@gmail.com'
# __fileName__='Chapters Chapter6method'
# __create_data__='2020/1/11 14:04'

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

