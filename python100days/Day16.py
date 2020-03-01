# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 15:22
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Day16.py
# @Software: PyCharm
# __create_data__=2020/2/28 15:22
# @Description: add Description

# comp=lambda x,y:x<y
# 上文这种语法叫匿名函数，既没有具体名称的函数，允许快速定义单行函数，
# lambda的使用场景：该表达式所写的函数不能给其他程序调用，只能定义简单的函数，：后面只能有一个表达式
# lambda会返回一个函数对象，需要一个变量接受，如果没有变量接受，会很快被丢弃。
# 冒号前是参数，可以有多个，用逗号隔开。冒号右边的是返回值。
def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(origin_items, comp=lambda x, y: x > y):
    """高质量冒泡排序(搅拌排序)"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def merge_sort(items, comp=lambda x, y: x <= y):
    """归并排序(分治法)"""
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


# ----------------------------
def merge(items1, items2, comp):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


# ----------------------------
def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


# 在方法中测试lambda表达式：把lambda表达式赋值给comp变量，在lambda关键字后，写表达式
def comp_show(x, y, comp=lambda x, y: x < y):
    foo = [2, 18, 9, 22, 17, 24, 8, 12, 17]
    print((lambda x: x % 3 == 0, foo))
    if x < y:
        print(x)
    if (comp(x, y)):
        print(x)


def main():
    items = [1, 6, 4, 2, 1, 56, 43, 445, 2, 0]
    items_sort = select_sort(items)
    for i in items_sort:
        print(i)
    # 使用生成式（推导式）语法
    prices = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }
    # 用股票价格大于100元的股票构造一个新的字典
    prices2 = {key: value for key, value in prices.items() if value > 100}
    print(prices2)

    # 嵌套的列表：
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    # 录入五个学生三门课程的成绩
    # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
    # scores = [[None] * len(courses)] * len(names)
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for col, course in enumerate(courses):
            scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
            print(scores)

    """
    从列表中找出最大的或最小的N个元素
    堆结构(大根堆/小根堆)
    """
    import heapq

    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

    """
    迭代工具 - 排列 / 组合 / 笛卡尔积
    """
    import itertools

    itertools.permutations('ABCD')
    itertools.combinations('ABCDE', 3)
    itertools.product('ABCD', '123')

    """
    找出序列中出现次数最多的元素
    """
    from collections import Counter

    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = Counter(words)
    print(counter.most_common(3))

    # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
    # 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
    # B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
    # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
    fish = 6
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 5

    """
    快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
    """

    def quick_sort(origin_items, comp=lambda x, y: x <= y):
        items = origin_items[:]
        _quick_sort(items, 0, len(items) - 1, comp)
        return items

    def _quick_sort(items, start, end, comp):
        if start < end:
            pos = _partition(items, start, end, comp)
            _quick_sort(items, start, pos - 1, comp)
            _quick_sort(items, pos + 1, end, comp)

    def _partition(items, start, end, comp):
        pivot = items[end]
        i = start - 1
        for j in range(start, end):
            if comp(items[j], pivot):
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[end] = items[end], items[i + 1]
        return i + 1


if __name__ == '__main__':
    main()
    comp_show(2, 4)
