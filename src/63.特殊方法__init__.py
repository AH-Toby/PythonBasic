# -*- coding: utf-8 -*-
# @Time    : 2023/8/29 20:04
# @Author  : toby
# @File    : 63.特殊方法__init__.py
# @Software: PyCharm
# @Desc:

class A(object):
    def __new__(cls, *args, **kwargs):
        print("调用了__new__方法")
        cls.type = "传递一下"
        return object.__new__(cls)

    def __init__(self):
        print(f"通过new方法传递下去：{self.type}")
        print("调用了__init__方法")


a = A()

