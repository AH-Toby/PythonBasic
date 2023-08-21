# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 11:36
# @Author  : toby
# @File    : 30.函数的参数和返回值.py
# @Software: PyCharm
# @Desc:函数的参数和返回值

def add2num(a, b):
    c = a + b
    print(c)


# 调用1
add2num(1, 2)

# 调用2
add2num(a=1, b=2)


# 缺省参数
def printinfo(name, age=35):
    # 打印任何传入的字符串
    print("name: %s" % name)
    print("age %d" % age)


# 调用printinfo函数
printinfo(name="miki")  # 在函数执行过程中 age去默认值35
printinfo(age=9, name="miki")


# 不定长参数
def fun(a, b, *args, **kwargs):
    """可变参数演示示例"""
    print(f"a:{a}")
    print(f"b:{b}")
    print(f"args:{args}")
    print(f"kwargs:{kwargs}")
    for key, value in kwargs.items():  # 遍历字典
        print(f"key={key},value={value}")  # 输出字典


fun(1, 2, 3, 4, 5, m=6, n=7, p=8)  # 调用函数


# 带返回值的函数
def add2num(a, b):
    c = a + b
    return c


result = add2num(100, 98)
print(result)
