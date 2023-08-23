# -*- coding: utf-8 -*-
# @Time    : 2023/8/23 23:53
# @Author  : toby
# @File    : 50.多继承.py
# @Software: PyCharm
# @Desc: 多继承，派生类继承多个父类
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
print(wukong.change_skill)
wukong.change()
wukong.change_red()