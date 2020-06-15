class Master(object):
    def __init__(self):
        self.kongfu = "古法煎饼果子配方"
    def make_cake(self):
        print("[古法] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

class School(object):
    def __init__(self):
        self.kongfu = "现代煎饼果子配方"

    def make_cake(self):
        print("[现代] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

class Prentice(School, Master):
    def __init__(self):
        self.kongfu = "猫氏煎饼果子配方"
        # 私有属性，可以在类内部通过self调用，但不能通过对象访问
        self.__money = 10000


    # 现代软件开发中，通常会定义get_xxx()方法和set_xxx()方法来获取和修改私有属性值。

    # 返回私有属性的值
    def get_money(self):
        return self.__money

    # 接收参数，修改私有属性的值
    def set_money(self, num):
        self.__money = num


    def make_cake(self):
        self.__init__()
        print("[猫氏] 按照 <%s> 制作了一份煎饼果子..." % self.kongfu)

    def make_old_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_new_cake(self):
        School.__init__(self)
        School.make_cake(self)

class PrenticePrentice(Prentice):
    pass


damao = Prentice()
# 对象不能访问私有权限的属性和方法
# print(damao.__money)
# damao.__print_info()

# 可以通过访问公有方法set_money()来修改私有属性的值
damao.set_money(100)

# 可以通过访问公有方法get_money()来获取私有属性的值
print(damao.get_money())