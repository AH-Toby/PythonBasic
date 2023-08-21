# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 22:34
# @Author  : toby
# @File    : 39.递归函数和匿名函数.py
# @Software: PyCharm
# @Desc:

# 一.递归函数
# 计算n的阶乘!n = 1*2*3*4*....*n
def calNum(n):
    if n >= 1:
        result = n * calNum(n - 1)
    else:
        result = 1
    return result


print(calNum(2))

# 二.匿名函数
lambda_func = lambda x, y: x + y
print(lambda_func(1, 2))


# 等价于
def lambda_func(x, y):
    return x + y


print(lambda_func(1, 2))
