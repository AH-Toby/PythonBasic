# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 22:27
# @Author  : toby
# @File    : 38.函数引用.py
# @Software: PyCharm
# @Desc:函数之间的引用

a = 1
b = a
print(f"a:{a},b:{b}")
print(f"id(a):{id(a)},id(b):{id(b)}")
a = 2
print(f"a:{a},b:{b}")
print(f"id(a):{id(a)},id(b):{id(b)}")


a = [1, 2]
b = a
print(f"a:{a},b:{b}")
print(f"id(a):{id(a)},id(b):{id(b)}")
a.append(3)
print(f"a:{a},b:{b}")
print(f"id(a):{id(a)},id(b):{id(b)}")

