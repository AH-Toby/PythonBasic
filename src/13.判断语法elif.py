# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 22:38
# @Author  : toby
# @File    : 13.判断语法elif.py
# @Software: PyCharm
# @Desc:

# 判断成绩
score = int(input("输入考试成绩:"))
if 90 <= score <= 100:
    print('本次考试，等级为A')
elif 80 <= score < 90:
    print('本次考试，等级为B')
elif 70 <= score < 80:
    print('本次考试，等级为C')
elif 60 <= score < 70:
    print('本次考试，等级为D')
elif 0 <= score < 60:
    print('本次考试，等级为E')

# if-elif-else一起用
height = int(input("请输入你的身高:"))
if height > 150:
    print("身高超过150cm需要买票！")
elif 0 < height <= 150:
    print("身高在150cm以下免费！")
else:
    print("输入的数值有问题")