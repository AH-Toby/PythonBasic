# -*- coding: utf-8 -*-
# @Time    : 2023/8/22 23:49
# @Author  : toby
# @File    : 46.__str__方法.py
# @Software: PyCharm
# @Desc:
class Hero(object):
    """类的注释"""
    def __init__(self, name, hp, atk, armor):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.armor = armor

    def __str__(self):
        return f"英雄 <{self.name}> 数据： 生命值 {self.hp}, 攻击力 {self.atk}, 护甲值 {self.armor}"

    def move(self):
        print("move方法")

    def attack(self):
        print("attack方法")


super_man = Hero("superman", 1000, 450, 200)
spider_man = Hero("spiderman", 500, 400, 100)
print(super_man)
print(spider_man)

print(Hero.__doc__)

