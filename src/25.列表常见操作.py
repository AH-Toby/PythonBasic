# -*- coding: utf-8 -*-
# @Time    : 2023/8/17 22:52
# @Author  : toby
# @File    : 25.列表常见操作.py
# @Software: PyCharm
# @Desc:

# 定义变量A，默认有3个元素
var_list = [1, 2, 3]

# 一.列表增加数据
# 1.append增加元素
var_list.append("append添加")
print(var_list)

# 2.insert增加元素
var_list.insert(0, "insert添加")
print(var_list)

# 3.extend合并另外一个列表
extend_list = [4, 5, 6]
var_list.extend(extend_list)
print(var_list)

# 二.删除数据
# 1.del删除列表元素
del var_list[2]
print(var_list)

# 2.pop删除最后一个元素
var_list.pop()
print(var_list)
var_list.pop(-2)
print(var_list)

# 3.remove按值删除
var_list.remove(3)
print(var_list)

# 三.修改元素
var_list[3] = "5"
print(var_list)

# 四.查看元素
# 1.in / not in
print(1 in var_list)
print(5 not in var_list)

# 2.index
print(var_list.index("5"))

# 3.count
print(var_list.count(1))

# 五.排序
var_list = [5, 1, 3, 6, 2, 4]
var_list.sort()  # 默认正序
print(var_list)
var_list.sort(reverse=True)  # 逆序
print(var_list)
