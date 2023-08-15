# -*- coding: utf-8 -*-
# @Time    : 2023/8/14 23:26
# @Author  : toby
# @File    : 8.数据类型转换.py
# @Software: PyCharm
# @Desc: 数据类型转换

str_var = "10"
num1 = int(str_var)
print(num1)

# int() 处理浮点数，只留下整数部分，舍弃小数部分（并不是四舍五入操作）
float_var = 3.1415926
num2 = int(float_var)
print(num2)

# 按8进制转换
num3 = int(str_var, 8)
print(num3)
# 按16进制转换
num4 = int(str_var, 16)
print(num4)

