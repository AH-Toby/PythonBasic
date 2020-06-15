# * 提供三个类，手机，电脑，程序员
# # # # * 手机-->通信打电话，电脑-->编程，人-->让手机和电脑工作
# # # # * 分别设计类，完成需求

# 添加一个电子产品的总类


class Ep(object):
    def work(self):
        pass


class Phone(Ep):
    def work(self):
        print("通信打电话")


class Computer(Ep):
    def work(self):
        print("编程")


# 新增一个Pad类
class Pad(Ep):
    def work(self):
        print("看书")


class Coder(object):
    def work_with_ep(self, ep):
        ep.work()


zhangsan = Coder()
zhangsan.work_with_ep(Phone())
zhangsan.work_with_ep(Computer())
zhangsan.work_with_ep(Pad())
