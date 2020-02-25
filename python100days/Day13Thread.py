# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 16:14
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Day13Thread.py
# @Software: PyCharm
# __create_data__=2020/2/23 16:14
# @Description: add Description

# 在python中实现并发编程主要有三种方式：多进程，多线程，多进程+多线程

# multiprocessing 模块的Process类来创建子进程。还可以创建进程池，队列，和管道
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print("启动下载，进程号：%d" % getpid())
    print("开始下载%s.." % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("%s下载完成，耗时%d秒" % (filename, time_to_download))# 如果%后面有多个以上的参数，需要用括号括起来


def main():
    start = time()
    p1 = Process(target=download_task, args=("挤挤都会有的.pdf",))# args参数需要使用括号括起来，并在引号后面有逗号
    p1.start()
    p2 = Process(target=download_task, args=("SuperTrampAI.avi",))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("总共耗时了%.2f秒" % (end - start))

# 使用multiprocessing 模块中的Queue类实现多个进程共享的队列，底层是通过管道和信号量机制来实现的

# 目前都线程的开发推荐使用threading模块
# 导入包：from threading import Thread
# 创建线程：t1=Thread(target=download,args=('filename.pdf',)) t1.start() t1.join()
# 通过继承的方式创建线程：from threading import Thread
# class DownloadTask(Thread):  重写__init__()方法和run()方法

# 在python中使用锁机制
# 导包：from threading import Thrad ,Lock
# self._lock.acquire() 获取锁
# self_lock.release() 释放锁

# 

if __name__ == '__main__':
    main()
