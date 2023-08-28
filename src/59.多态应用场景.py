# -*- coding: utf-8 -*-
# @Time    : 2023/8/28 23:33
# @Author  : toby
# @File    : 59.多态应用场景.py
# @Software: PyCharm
# @Desc:


class Phone(object):
    def call_someone(self):
        print("打电话")


class Computer(object):
    def coding(self):
        print("编程")


# 新增一个类
class Pad(object):
    def reading(self):
        print("看书")


class Coder(object):
    def work_with_phone(self, phone):
        phone.call_someone()

    def work_with_computer(self, computer):
        computer.coding()

    def work_with_pad(self, pad):
        pad.reading()


lili = Coder()
lili.work_with_phone(Phone())
lili.work_with_computer(Computer())
lili.work_with_pad(Pad())
