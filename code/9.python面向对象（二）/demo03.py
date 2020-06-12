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
    def __init__(self):
        self.kongfu = "厉害的黏人本领"

    def make_fish(self):
        print("利用自己的新的技术抓鱼")

    def kanmen(self):
        print("利用自己本领看门")

    def makehappy(self):
        print("利用%s讨主人开心" % self.kongfu)


xiaohua = MinCat()
print(xiaohua.kongfu)  # 子类和父类有同名属性，则默认使用子类的
xiaohua.make_fish()  # 子类和父类有同名方法，则默认使用子类的
xiaohua.kanmen()
xiaohua.makehappy()
# 子类的魔法属性__mro__决定了属性和方法的查找顺序
print(MinCat.__mro__)