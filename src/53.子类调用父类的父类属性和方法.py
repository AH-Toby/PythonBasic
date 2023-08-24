# -*- coding: utf-8 -*-
# @Time    : 2023/8/24 23:54
# @Author  : toby
# @File    : 53.子类调用父类的父类属性和方法.py
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

    def old_change(self):
        print(f"执行SaiYaMan类的__init__方法前，self.change_skill：{self.change_skill}")
        SaiYaMan.__init__(self)
        print(f"执行SaiYaMan类的__init__方法后，self.change_skill：{self.change_skill}")
        SaiYaMan.change(self)

    def old_change_red(self):
        print(f"执行GodOfSaiYaMan类的__init__方法前，self.change_skill：{self.change_skill}")
        GodOfSaiYaMan.__init__(self)
        print(f"执行GodOfSaiYaMan类的__init__方法后，self.change_skill：{self.change_skill}")
        GodOfSaiYaMan.change_red(self)


wukong = SuperSaiYaManSon()
print(wukong.change_skill)
wukong.change()
wukong.change_red()
wukong.old_change()
wukong.old_change_red()
print(SuperSaiYaManSon.__mro__)
