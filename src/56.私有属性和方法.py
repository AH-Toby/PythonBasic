# -*- coding: utf-8 -*-
# @Time    : 2023/8/28 22:44
# @Author  : toby
# @File    : 56.私有属性和方法.py
# @Software: PyCharm
# @Desc:

# 类的私有权限
class Privater(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__salary = 100

    def __get_salary(self):
        return self.__salary

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
# print(lili.__salary)  # 私有属性外层无法获取
print(lili.get_base_info())  # 获取基本信息
# print(lili.__get_salary())  # 私有方法外层无法获取
