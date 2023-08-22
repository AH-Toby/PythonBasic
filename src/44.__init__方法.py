# -*- coding: utf-8 -*-
# @Time    : 2023/8/22 23:41
# @Author  : toby
# @File    : 44.__init__方法.py
# @Software: PyCharm
# @Desc:

class Hero(object):
    def __init__(self):
        self.name = "superman"
        self.hp = 1000
        self.atk = 450
        self.armor = 200

    def move(self):
        print("move方法")

    def attack(self):
        print("attack方法")

    def info(self):
        """在类的实例方法中，通过self获取该对象的属性"""
        print("英雄 %s 的生命值 :%d" % (self.name, self.hp))
        print("英雄 %s 的攻击力 :%d" % (self.name, self.atk))
        print("英雄 %s 的护甲值 :%d" % (self.name, self.armor))


super_man = Hero()
super_man.info()
super_man.move()
super_man.attack()
