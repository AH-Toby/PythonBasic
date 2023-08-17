# -*- coding: utf-8 -*-
# @Time    : 2023/8/17 23:27
# @Author  : toby
# @File    : 27.字典常见操作.py
# @Software: PyCharm
# @Desc:

my_dict = {"name": "lili", "height": 190}
print(my_dict)
# 字典：常见操作
# 一.增
my_dict["age"] = 11
print(my_dict)

# 二.删除
# 1.del删除指定的元素
del my_dict["name"]
print(my_dict)

# 2.pop取出元素并删除该元素
height = my_dict.pop("height")
print(height)

# 3.clear清除所有元素
my_dict.clear()
print(my_dict)

# 三.改
my_dict = {"name": "lili", "height": 190}
my_dict["height"] = 180
print(my_dict)

# 四.查
print(my_dict["name"])
print(my_dict.get("name"))

# len
print(len(my_dict))

# keys
print(my_dict.keys())

# values
print(my_dict.values())

# items
print(my_dict.items())
