# -*- coding: utf-8 -*-
# @Time    : 2023/8/22 20:11
# @Author  : toby
# @File    : 42.添加和获取对象的属性.py
# @Software: PyCharm
# @Desc: 添加和获取对象的属性

class Hero(object):
    def move(self):
        print("move方法")

    def attack(self):
        print("attack方法")


# 实例化对象
super_man = Hero()
# 添加属性
super_man.name = "super_man"  # 名称
super_man.hp = 1000  # 血量
super_man.atk = 450  # 攻击力
super_man.armor = 200  # 防御力

# 获取属性
print(f"{super_man.name}的HP为{      super_man.hp},攻击力为{super_man.atk},防御力为{super_man.armor}")

# 实例化方法
super_man.move()
super_man.attack()

