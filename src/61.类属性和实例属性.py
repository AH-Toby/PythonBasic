# -*- coding: utf-8 -*-
# @Time    : 2023/8/29 19:43
# @Author  : toby
# @File    : 61.类属性和实例属性.py
# @Software: PyCharm
# @Desc:


class Dog(object):
    type = "狗"  # 类属性

    def __init__(self):
        self.name = "小黄"  # 实例属性


dog = Dog()
print(dog.name)
print(dog.type)  # 类属性可以通过对象获取
print(Dog.type)  # 类属性可以通过对象获取


# print(Dog.name)  # 实例属性不能通过类获取


class Cat(object):
    type = "猫"  # 类属性

    def __init__(self):
        self.type = "小猫"  # 实例属性


# 如果有同名对象属性，实例对象会优先访问对象属性
cat = Cat()
print(cat.type)

# 类属性只能通过类对象修改属性，不能通过实例属性修改
dog.type = "小狗"
print(dog.type)  # 注意这个是修改的实例对象的属性不是类属性
print(Dog.type)  # 类属性并为修改

Dog.type = "大狗"  # 修改了类属性
print(dog.type)
print(Dog.type)


# 类属性私有化
class Human(object):
    name = "lili"
    __type = "人"


print(Human.name)
# print(Human.__type)  # 获取不到
