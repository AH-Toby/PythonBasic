# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 14:51
# @Author  : toby
# @File    : 34.修改全局变量.py
# @Software: PyCharm
# @Desc: 修改全局变量

# 全局变量和局部变量名称相同例子
# 定义全局变量
a = 100


def test1():
    global a  # 声明全局变量
    print('-----test1----修改前---a=%d' % a)
    a = 200
    print('-----test1----修改后---a=%d' % a)


def test2():
    print('-----test2---a=%d' % a)


# 调用函数
test1()
test2()
