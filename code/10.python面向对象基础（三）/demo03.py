# * 提供三个类，手机，电脑，程序员
# # # # * 手机-->通信打电话，电脑-->编程，人-->让手机和电脑工作
# # # # * 分别设计类，完成需求


class Phone(object):
    def call_someone(self):
        print("通信打电话")


class Computer(object):
    def coding(self):
        print("编程")


class Coder(object):
    def work_with_phone(self, phone):
        phone.call_someone()

    def work_with_computer(self, computer):
        computer.coding()


zhangsan = Coder()
zhangsan.work_with_phone(Phone())
zhangsan.work_with_computer(Computer())
