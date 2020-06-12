# 老猫将自己的一身本领传给小猫,同时狗狗也将自己看家的本事传给了小猫

# 定一个父类

class Cat(object):
    def __init__(self):
        self.kongfu = "厉害的捉鱼本领"

    def make_fish(self):
        print("利用%s抓鱼" % self.kongfu)


# 定义第二个父类
class Dog(object):
    def __init__(self):
        self.kongfu = "厉害的看家本领"

    def kanmen(self):
        print("利用%s看家" % self.kongfu)


# MinCat，继承了Cat、Dog，Cat、Dog是父类。
class MinCat(Cat, Dog):
    pass


xiaohua = MinCat()
print(MinCat.__mro__)

