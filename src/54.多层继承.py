# -*- coding: utf-8 -*-
# @Time    : 2023/8/25 00:09
# @Author  : toby
# @File    : 54.多层继承.py
# @Software: PyCharm
# @Desc: 多层继承

class SaiYaMan(object):
    def __init__(self):
        self.change_skill = "一级变身"
        self.hair = "硬，直，短，黑"

    def transfiguration(self):
        self.hair = "硬，直，长，黄"
        print(f"{self.change_skill},头发会变的{self.hair}")


class GodOfSaiYaMan(SaiYaMan):
    def transfiguration_red(self):
        self.change_skill = "多级变身"
        self.hair = "硬，直，长，红"
        print(f"{self.change_skill},头发会变的{self.hair}")


class SuperSaiYaManSon(GodOfSaiYaMan):
    pass


wukong = SuperSaiYaManSon()
wukong.transfiguration()
wukong.transfiguration_red()
print(SuperSaiYaManSon.__mro__)
