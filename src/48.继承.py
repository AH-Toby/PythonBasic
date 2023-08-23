# -*- coding: utf-8 -*-
# @Time    : 2023/8/23 23:45
# @Author  : toby
# @File    : 48.继承.py
# @Software: PyCharm
# @Desc:


# 基类
class A(object):
    def __init__(self):
        self.num = 10

    def print_num(self):
        print(self.num + 20)


# 派生类
class B(A):
    pass


b = B()
print(b.num)
b.print_num()
