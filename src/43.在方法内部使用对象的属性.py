# -*- coding: utf-8 -*-
# @Time    : 2023/8/22 23:38
# @Author  : toby
# @File    : 43.在方法内部使用对象的属性.py
# @Software: PyCharm
# @Desc:通过self可以在方法的内部获取类属性
class Hero(object):
    def move(self):
        print("move方法")

    def attack(self):
        print("attack方法")

    def info(self):
        """在类的实例方法中，通过self获取该对象的属性"""
        print("英雄 %s 的生命值 :%d" % (self.name, self.hp))
        print("英雄 %s 的攻击力 :%d" % (self.name, self.atk))
        print("英雄 %s 的护甲值 :%d" % (self.name, self.armor))

# 实例化对象
super_man = Hero()
# 添加属性
super_man.name = "super_man"  # 名称
super_man.hp = 1000  # 血量
super_man.atk = 450  # 攻击力
super_man.armor = 200  # 防御力

# 实例化方法
super_man.move()
super_man.attack()
super_man.info()


