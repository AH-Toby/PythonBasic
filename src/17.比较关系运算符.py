# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 23:18
# @Author  : toby
# @File    : 17.比较关系运算符.py
# @Software: PyCharm
# @Desc:

a = 15
b = 20
# 1.比较运算符
# 等于：==
print(a == b)
# 不等于：!=
print(a != b)
# 大于：>
print(a > b)
# 小于：<
print(a < b)
# 大于等于：>=
print(a >= b)
# 小于等于：<=
print(a <= b)

# 2.逻辑运算符
# and：左右表达式都为True，整个表达式结果才为True
if (1 == 1) and (10 > 3):
    print("条件成立！")
# or : 左右表达式有一个为True，整个表达式结果就为 True
if (1 == 2) or (10 > 3):
    print("条件成立！")
# not：将右边表达式的逻辑结果取反，Ture变为False，False变为True
if not (1 == 2):
    print("条件成立！")

