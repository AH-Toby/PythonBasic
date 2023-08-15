# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 22:32
# @Author  : toby
# @File    : 12.判断语法if-else练一练.py
# @Software: PyCharm
# @Desc:从键盘输入身高，如果身高没有超过150cm，则进动物园不用买票，否则需要买票。

height = int(input("请输入身高:"))
if height <= 150:
    print("不用买票")
else:
    print("买票")
