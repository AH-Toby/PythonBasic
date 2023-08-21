# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 22:13
# @Author  : toby
# @File    : 36.函数的参数.py
# @Software: PyCharm
# @Desc:  函数的参数

# 1.缺省参数
def printInfo(name, age=30):
    """
    打印人名和年龄
    :param name:
    :param age:
    :return:
    """
    print(f"姓名{name},年龄{age}")


printInfo("Toby")
printInfo("lili", 18)


# 2.不定长参数
def func(a, b, *args, **kwargs):
    """可变参数演示示例"""
    print(f"a:{a},b:{b},args:{args},kwargs:{kwargs}")


func(1, 2, 3, 4, 5, m=6, n=7, p=8)
c = (3, 4, 5, 6)
d = {"m": 6, "n": 7, "p": 8}
func(*c, **d)
func(c, d)  # 与不加*对比


# 3.缺省参数在*args之后
def sum_nums_3(a, *args, b=22, c=33, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


sum_nums_3(100, 200, 300, 400, 500, 600, 700, b=1, c=2, mm=800, nn=900)
