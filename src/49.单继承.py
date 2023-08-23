# -*- coding: utf-8 -*-
# @Time    : 2023/8/23 23:47
# @Author  : toby
# @File    : 49.单继承.py
# @Software: PyCharm
# @Desc: 单继承，派生类只继承一个父类
class SaiYaMan(object):
    def __init__(self):
        self.change_skill = "变身"

    def change(self):
        print(f"{self.change_skill}")


class SuperSaiYaManSon(SaiYaMan):
    pass


wukong = SuperSaiYaManSon()
print(wukong.change_skill)
wukong.change()
