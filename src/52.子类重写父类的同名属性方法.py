# -*- coding: utf-8 -*-
# @Time    : 2023/8/24 00:01
# @Author  : toby
# @File    : 52.子类重写父类的同名属性方法.py
# @Software: PyCharm
# @Desc:
class SaiYaMan(object):
    def __init__(self):
        self.change_skill = "一级变身"

    def change(self):
        print(f"{self.change_skill}")


class GodOfSaiYaMan(object):
    def __init__(self):
        self.change_skill = "多级变身"

    def change(self):
        print(f"{self.change_skill}")

    def change_red(self):
        print(f"{self.change_skill}")


class SuperSaiYaManSon(SaiYaMan, GodOfSaiYaMan):
    def __init__(self):
        self.change_skill = "4级变身"

    def change(self):
        print(f"{self.change_skill}")

    def change_red(self):
        print(f"{self.change_skill}")


wukong = SuperSaiYaManSon()
print(wukong.change_skill)
wukong.change()
wukong.change_red()
print(SuperSaiYaManSon.__mro__)
