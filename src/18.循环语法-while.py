# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 23:28
# @Author  : toby
# @File    : 18.循环语法-while.py
# @Software: PyCharm
# @Desc:

# 循环5次
i = 1
while i <= 5:
    print(f"这是第{i}次循环")
    i += 1

# 计算1~100的和
i = 1
sum_100 = 0
while i <= 100:
    sum_100 += i
    i += 1
print(sum_100)

# 计算1~100之间的偶数和
i = 1
sum_100 = 0
while i <= 100:
    if i % 2 == 0:
        sum_100 += i
    i += 1
print(sum_100)
