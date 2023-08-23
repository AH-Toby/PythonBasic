# -*- coding: utf-8 -*-
# @Time    : 2023/8/23 23:59
# @Author  : toby
# @File    : 51.__mro__方法.py
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
    pass


wukong = SuperSaiYaManSon()
print(SuperSaiYaManSon.__mro__)
