# -*- coding: utf-8 -*-
# @Time    : 2023/8/17 23:12
# @Author  : toby
# @File    : 26.元组常见操作.py
# @Software: PyCharm
# @Desc:

# 元组查看元素
mylist = ('123', 1, "hhh", 1)
print(mylist[0])

# 元组不能修改元素
# mylist[0] = "修改元素"
# print(mylist)

# index
data_index = mylist.index(1)
print(data_index)

# count
data_count = mylist.count(1)
print(data_count)
