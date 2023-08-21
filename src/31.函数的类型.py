# -*- coding: utf-8 -*-
# @Time    : 2023/8/21 14:17
# @Author  : toby
# @File    : 31.函数的类型.py
# @Software: PyCharm
# @Desc: 函数的类型

# 1.无参数无返回值

def print_menu():
    print("无参数无返回值的函数")


print_menu()


# 2.无参数有返回值
def get_temperature():
    return 24


temperature = get_temperature()
print(f"当前的温度是{temperature}")


# 3.有参数无返回值
def print_temperature(temperature):
    """
    打印当前温度
    :param temperature:
    :return:
    """
    print(f"当前的温度是{temperature}")


print_temperature(23)


# 4.有参数，有返回值函数
# 计算1~num的累积和
def calculateNum(num):
    result = 0
    i = 1
    while i <= num:
        result = result + i
        i += 1
    return result


result = calculateNum(100)
print(f'1~100的累积和为:{result}')
