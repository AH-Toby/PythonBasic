# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 23:05
# @Author  : toby
# @File    : 16.判断语法补充.py
# @Software: PyCharm
# @Desc:

# 1.区间比较
a = 10
print(1 < a < 20)
print(11 < a < 20)

# 2.三元运算
b = 20
c = a if a > b else b
print(c)

# 3.数字的逻辑
# and运算,只要有一个值为0 则结果为0，否则结果为最后一个非0 数字
a = 0
b = 1
c = 3
print(a and b)
print(b and a)
print(a and c)
print(b and c)

# or运算，只有所有值为0 则结果为0，否则结果为第一个非0 数字
print(a or a)
print(a or b)
print(b or a)
print(c or b)
print(b or c)

# 4.is用法
