# -*- coding: utf-8 -*-
# @Time    : 2023/8/25 00:22
# @Author  : toby
# @File    : 55.super方法来调用父类的方法和属性.py
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
        super().__init__()
        self.change_skill = "4级变身"

    def change(self):
        print(f"{self.change_skill}")

    def change_red(self):
        print(f"{self.change_skill}")

    def father_change(self):
        # 1.用老式的方法
        # SaiYaMan.__init__(self)
        # SaiYaMan.change(self)
        #
        # GodOfSaiYaMan.__init__(self)
        # GodOfSaiYaMan.change(self)
        # GodOfSaiYaMan.change_red(self)

        # 2.使用带类名的super方法
        # super(SuperSaiYaManSon, self).__init__()
        # super(SuperSaiYaManSon, self).change()
        # super(SuperSaiYaManSon, self).change()
        # super(SuperSaiYaManSon, self).change_red()

        # 3.使用super方法
        super().__init__()
        super().change()
        super().change_red()


wukong = SuperSaiYaManSon()
wukong.father_change()
print(SuperSaiYaManSon.__mro__)
