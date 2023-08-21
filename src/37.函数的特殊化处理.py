# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 22:22
# @Author  : toby
# @File    : 37.函数的特殊化处理.py
# @Software: PyCharm
# @Desc:

# 1.拆包
# 直接对函数的返回值进行拆包
def get_my_info():
    high = 178
    weight = 100
    age = 18
    return high, weight, age


my_high, my_weight, my_age = get_my_info()
print(my_high)
print(my_weight)
print(my_age)

# 2.交换变量值
a = 4
b = 5
a, b = b, a
print(a)
print(b)
