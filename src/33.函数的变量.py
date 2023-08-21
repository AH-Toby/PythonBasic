# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 14:43
# @Author  : toby
# @File    : 33.函数的变量.py
# @Software: PyCharm
# @Desc: 函数变量

# 1.局部变量
def local_val():
    """
    局部变量
    :return:
    """
    a = 100
    print(f"局部变量：{a}")


# 2.全局变量
global_value = 100


def global_val():
    print(f"全局变量：{global_value}")


local_val()
global_val()


# 全局变量和局部变量使用相同名称
# 定义全局变量
a = 100

def test1():
    a = 300  # 定义局部变量
    print('-----test1----修改前---a=%d' % a)
    a = 200
    print('-----test1----修改后---a=%d' % a)


def test2():
    print('-----test2---a=%d' % a)


# 调用函数
test1()
test2()
