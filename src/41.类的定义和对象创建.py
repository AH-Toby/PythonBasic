# -*- coding: utf-8 -*-
# @Time    : 2023/8/22 20:04
# @Author  : toby
# @File    : 41.类的定义和对象创建.py
# @Software: PyCharm
# @Desc: 定义类

# 一.创建类
# 1.旧式类
class HeroOld:
    def info(self):
        print("英雄莫问出处")


# 2.新式类
class HeroNew(object):
    def info(self):
        print("英雄莫问出处")


# 二.创建对象
class Hero(object):
    def info(self):
        print(f"self:{self}")


# 实例化一个对象
super_man = Hero()
super_man.info()

print(super_man)
print(id(super_man))

