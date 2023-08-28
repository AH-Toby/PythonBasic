# -*- coding: utf-8 -*-
# @Time    : 2023/8/28 23:00
# @Author  : toby
# @File    : 58.特殊方法获取私有属性和方法.py
# @Software: PyCharm
# @Desc:
class Privater(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__salary = 100

    def __get_salary(self):
        return self.__salary

    def get_salary(self):
        """间接方法获取类属性值"""
        return self.__salary

    def set_salary(self, new_salary):
        """
        设置内部私有属性
        :param new_salary:
        :return:
        """
        self.__salary = new_salary

    def get_base_info(self):
        base_info = {
            "name": self.name,
            "age": self.age,
            "salary": self.__salary
        }
        return base_info


lili = Privater("lili", 18)
# 通过下面方法也可以访问到但是不推荐使用
print(lili._Privater__salary)
print(lili._Privater__get_salary())
lili._Privater__salary = 180
print(lili._Privater__salary)
