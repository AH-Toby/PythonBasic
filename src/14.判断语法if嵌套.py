# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 22:45
# @Author  : toby
# @File    : 14.判断语法if嵌套.py
# @Software: PyCharm
# @Desc: 检票场景

# 1，代表有车票
# 0，代表没有车票
ticket = int(input("是否有车票:"))
knife = int(input("刀子长度:"))

if ticket == 1:
    print("有车票，可以进车站！")
    if knife < 10:
        print("刀子长度小于规定10cm，可以通过安检")
    else:
        print("刀子长度大于规定10cm，不可以通过安检")
else:
    print("没有车票，不能进站")
