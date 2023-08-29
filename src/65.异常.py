# -*- coding: utf-8 -*-
# @Time    : 2023/8/29 23:14
# @Author  : toby
# @File    : 65.异常.py
# @Software: PyCharm
# @Desc:
# 捕获异常
try:
    open('123.txt', 'r')  # 此代码单独运行会报IOError错误
except IOError:
    pass

# 捕获多个异常
try:
    open('123.txt', 'r')  # 此代码单独运行会报IOError错误
    print(num)
except (IOError, NameError):
    if IOError:
        print(f"捕获IOError：{IOError}异常")
    if NameError:
        print(f"捕获NameError：{NameError}异常")

# 捕获多个异常
try:
    print(num)  # 只会捕获一次
    print(111)
    open('123.txt', 'r')
except IOError:
    print(f"捕获IOError：{IOError}异常")
except NameError:
    print(f"捕获NameError：{NameError}异常")

# 捕获异常else,没有捕获到异常运行else中内容
try:
    num = 100
    print(num)
except NameError as errorMsg:
    print(f'产生错误了:{errorMsg}')
else:
    print('没有捕获到异常，真高兴')
