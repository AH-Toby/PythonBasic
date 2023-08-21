# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 22:05
# @Author  : toby
# @File    : 35.python函数的特性.py
# @Software: PyCharm
# @Desc:

# 一.函数之间共享数据
# 1.使用全局变量
g_num = 0


def test1():
    global g_num
    # 将处理结果存储到全局变量g_num中
    g_num = 100


def test2():
    # 通过获取全局变量g_num的值，从而获得test1函数处理之后的结果
    print(g_num)


# 1.先调用test1得到数据保存到全局变量中
test1()
# 2.在调用test2，处理test1函数执行之后的这个值
test2()


# 2.使用函数的返回值作为参数
def test1():
    return 30


def test2(num):
    print(num)


num = test1()
test2(num)


# 3.函数嵌套调用
def test1():
    return 20


def test2():
    num = test1()
    print(num)


test2()


# 4.函数作为回调参数
def test1():
    return 10


def test2(num=test1):
    print(num())


test2()


# 二.函数的返回值
def divid(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


result = divid(5, 2)
print(result)
