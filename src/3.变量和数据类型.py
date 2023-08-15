# -*- coding: utf-8 -*-
# @Time    : 2023/8/14 22:20
# @Author  : toby
# @File    : 3.变量和数据类型.py
# @Software: PyCharm
# @Desc: 变量和数据类型


int_var = 1111
# Python 2中有`long`类型来表示长整型，而Python 3中的整数类型就已经默认支持长整型的范围，没有了`long`类型。
long_var = 1234567890123456789012345678901234567890
float_var = 3.1415926
bool_var = True
string_var = "hello world!"
list_var = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3, 4, 5)
set_var = {1, 2, 3, 4, 5}
dict_var = {"name": "toby"}

print(type(int_var))
print(type(long_var))
print(type(float_var))
print(type(bool_var))
print(type(string_var))
print(type(list_var))
print(type(tuple_var))
print(type(set_var))
print(type(dict_var))
