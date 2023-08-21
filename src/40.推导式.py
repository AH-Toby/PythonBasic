# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 22:58
# @Author  : toby
# @File    : 40.推导式.py
# @Software: PyCharm
# @Desc: 函数推导式


# 一.列表推导式
a = [i for i in range(3)]
print(a)

# 2.推导式使用if
a = [i for i in range(3) if i % 2 == 0]
print(a)

# 3.for循环嵌套式
a = [(x, y) for x in range(1, 3) for y in range(3)]
print(a)


# 二.字典推导式
keys = ['a', 'b', 'c']
values = [1, 3, 5]
d = {k: v for k, v in zip(keys, values)}
print(d)