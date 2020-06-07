# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 15:20
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : AsyncioDemo.py
# @Software: PyCharm
# __create_data__=2020/6/3 15:20
# @Description: add Description


import asyncio
import datetime
import time


# 方法使用关键字：async声明
async def Asyncio1():
    print("Hello")
    await asyncio.sleep(1)
    print("world")


# ----------------------------------


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    # 调用进程
    await say_after(1, "Hello")
    await say_after(2, "World")

    print(f"finished at {time.strftime('%X')}")


# ----------------------------------------
# 并发执行多个进程
async def main2():
    task1 = asyncio.create_task(
        say_after(1, 'hello')
    )
    task2 = asyncio.create_task(
        say_after(2, 'World')
    )
    print(f"started at {time.strftime('%X')}")

    # 调用进程
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


# 休眠
async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


# 并发运行任务
async def factorial(name, number):
    f = 1
    # range:从2开始，叠加1
    for i in range(2, number + 1):
        print(f"Task{name}: Compute factorial ({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task{name}:factorial ({number})={f}")


async def main3():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4)
    )


# 超时：asyncio.wait_for(aw,timeout,*,loop=None)
# 指定timeout秒数后超时，可以为float或int型数值表示的等待秒数，如果timeout为None，则没有超时，会一直等待
# 如果在指定秒数内超时，任务将引发TimeoutError。加上shield()可以避免任务取消。
async def eternity():
    await asyncio.sleep(3600) # 休眠3600秒
    print("yay!")


async def main4():
    try:
        # 参数1：可等待对象；timeout：超时时间
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print("timeout!")
# 简单等待：wait（aws,*,loop=None,timeout=None,return_when=ALL_COMPLETED）
# 并发运行aws指定的可等待对象并阻塞线程知道满足return_when指定的条件，该条件为常量。
# 常量如下:FIRST_COMPLETER,FIRST_EXCEPTION,ALL_COMPLETE



# 通过asyncio.run 方法执行进程。
asyncio.run(main4())
