# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 10:59
# @Author  : toby
# @File    : 29.函数介绍.py
# @Software: PyCharm
# @Desc: 函数介绍


# 定义一个函数，能够完成打印信息的功能
def printInfo():
    print('------------------------------------')
    print('         人生苦短，我用Python')
    print('------------------------------------')


# 调用函数
printInfo()


# 函数的文档说明
def test(a: int, b: int):
    """
    用来完成2个数的求和
    :param a:
    :param b:
    :return:
    """
    print(f"{a + b}")


print(help(test))
