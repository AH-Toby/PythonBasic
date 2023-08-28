# -*- coding: utf-8 -*-
# @Time    : 2023/8/28 22:54
# @Author  : toby
# @File    : 57.修改私有属性的值.py
# @Software: PyCharm
# @Desc: 修改私有属性的值，由于私有属性无法在外层获取所以只能通过间接修改的方法来修改他的值

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
print(lili.name)
print(lili.age)
# 间接方法获取私有属性
print(lili.get_salary())

# 设置私有属性
lili.set_salary(180)
print(lili.get_salary())
