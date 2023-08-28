# -*- coding: utf-8 -*-
# @Time    : 2023/8/28 23:41
# @Author  : toby
# @File    : 60.多态的应用场景2.py
# @Software: PyCharm
# @Desc:

class Ep(object):
    def work(self):
        pass


class Phone(Ep):
    def work(self):
        print("打电话")


class Computer(Ep):
    def work(self):
        print("编程")


# 新增一个类
class Pad(Ep):
    def work(self):
        print("看书")


class Coder(object):
    def work_with_ep(self, ep):
        ep.work()


lili = Coder()
lili.work_with_ep(Phone())
lili.work_with_ep(Computer())
lili.work_with_ep(Pad())
