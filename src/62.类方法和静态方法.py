# -*- coding: utf-8 -*-
# @Time    : 2023/8/29 19:57
# @Author  : toby
# @File    : 62.类方法和静态方法.py
# @Software: PyCharm
# @Desc:

# 定义类方法
class Dog(object):
    __type = "狗"

    @classmethod
    def get_type(cls):
        return cls.__type


# 获取类私有属性
print(Dog.get_type())


# 静态方法
class Dog(object):
    __type = "狗"

    @staticmethod
    def print_info():
        print("输出信息")


# 获取类私有属性
Dog.print_info()


class Dog:
    def demo_method(self):
        print("对象方法")

    @classmethod
    def demo_method(cls):
        print("类方法")

    @staticmethod
    def demo_method():  # 被最后定义,调用时优先执行
        print("静态方法")


dog1 = Dog()
Dog.demo_method()  # 结果: 静态方法
dog1.demo_method()  # 结果: 静态方法
