# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 23:37
# @Author  : toby
# @File    : 20.whlie循环.py
# @Software: PyCharm
# @Desc:
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("* ", end='')
        j += 1
    print("\n")
    i += 1

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d " % (j, i, i * j), end='')
        j += 1
    print('\n')
    i += 1
