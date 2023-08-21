# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 14:29
# @Author  : toby
# @File    : 32.函数的嵌套调用.py
# @Software: PyCharm
# @Desc:函数的嵌套调用

def testB():
    print('---- testB start----')
    print('这里是testB函数执行的代码...(省略)...')
    print('---- testB end----')


def testA():
    print('---- testA start----')
    testB()
    print('---- testA end----')


testA()
