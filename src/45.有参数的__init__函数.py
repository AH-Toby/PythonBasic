# -*- coding: utf-8 -*-
# @Time    : 2023/8/22 23:46
# @Author  : toby
# @File    : 45.有参数的__init__函数.py
# @Software: PyCharm
# @Desc:

class Hero(object):
    def __init__(self, name, hp, atk, armor):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.armor = armor

    def move(self):
        print("move方法")

    def attack(self):
        print("attack方法")

    def info(self):
        """在类的实例方法中，通过self获取该对象的属性"""
        print("英雄 %s 的生命值 :%d" % (self.name, self.hp))
        print("英雄 %s 的攻击力 :%d" % (self.name, self.atk))
        print("英雄 %s 的护甲值 :%d" % (self.name, self.armor))


super_man = Hero("superman", 1000, 450, 200)
super_man.info()

spider_man = Hero("spiderman", 500, 400, 100)
spider_man.info()
