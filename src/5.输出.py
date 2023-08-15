# -*- coding: utf-8 -*-
# @Time    : 2023/8/14 22:54
# @Author  : toby
# @File    : 5.输出.py
# @Software: PyCharm
# @Desc: 输出

# 输出
print("输出内容")
name = "Toby"

# 换行输出
print("1234567890\n-------")

# 格式化输出
# 旧版格式化输出
print("my name is %s" % name)

# 3.6版本以后格式化输出
print(f"my name is {name}")

# str.format_map()和vars()
print("my name is {name}".format_map(vars()))

# format
print("my name is {}".format(name))
