# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 23:39
# @Author  : toby
# @File    : 21.循环语法for.py
# @Software: PyCharm
# @Desc:
name = 'helllo world!'

for x in name:
    print(x)

name = 'hello world!'
for x in name:
    if x == 'e':
        print("不能使用字符 e")
    else:
        print(x)

name = 'hello world!'
for x in name:
    if x == 'e':
        print("不能使用字符 e")
        break
    else:
        print(x)
else:
    print('没有出现禁止使用的字符')