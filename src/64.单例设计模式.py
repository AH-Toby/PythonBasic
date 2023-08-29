# -*- coding: utf-8 -*-
# @Time    : 2023/8/29 20:11
# @Author  : toby
# @File    : 64.单例设计模式.py
# @Software: PyCharm
# @Desc:


class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            print("创建一个对象")
            cls.__instance = object.__new__(cls)
        return cls.__instance


a = Singleton()
b = Singleton()

print(id(a))
print(id(b))


# 创建单例时，只执行一次init方法
class Singleton(object):
    __instance = None
    __is_first = True

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            print("创建一个对象")
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, name, age):
        if self.__is_first:
            print(name)
            print(age)
            Singleton.__is_first = False


a = Singleton("lili", 18)
b = Singleton("xiaoxiao", 20)  # 这个init是不会加载的

print(id(a))
print(id(b))
