# -*- coding: utf-8 -*-
# @Time    : 2023/8/17 23:55
# @Author  : toby
# @File    : 28.公共方法.py
# @Software: PyCharm
# @Desc:

# 一.运算符
# 1.+
print([1, 2] + [3, 4])

# 2.*
print([1, 2] * 3)

# 3.in
print(1 in [1, 2])

# not in
print("name" not in {"name": "Doron", "age": 24})

for i, value in enumerate([1, 2, 3, 4]):
    print(i)
    print("-" * 30)
    print(value)
