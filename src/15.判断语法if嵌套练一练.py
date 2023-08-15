# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 22:52
# @Author  : toby
# @File    : 15.判断语法if嵌套练一练.py
# @Software: PyCharm
# @Desc: 输入公交卡当前的余额，只要超过2元，就可以上公交车；如果车上有空座位，就可以坐下。
balance = int(input("当前余额:"))
seat_ok = int(input("是否有座位:"))  # 0:没有座位，1:有座位
if balance > 2:
    print("余额大于2可以上车")
    if seat_ok:
        print("有座位可以坐下")
    else:
        print("无座位不可以坐下")
else:
    print("余额小于2不可以上车")