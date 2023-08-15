# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 23:35
# @Author  : toby
# @File    : 19.break和continue.py
# @Software: PyCharm
# @Desc:
i = 10

while i > 0:
    print("妈，还要我刷啊~~~~~~~~~")
    if i == 5:
        print('好了，不用刷了')
        break

    print("正在刷 %d 个碗" % i)
    i -= 1

print('程序结束')


i = 10

while i > 0:
    print("妈，还要我刷啊~~~~~~~~~")
    if i == 5:
        print('好了，不用刷了')

        i -= 1  # continue 之前要注意修改 i 的值，否则容易导致死循环
        continue

    print("正在刷 %d 个碗" % i)
    i -= 1

print('程序结束')

