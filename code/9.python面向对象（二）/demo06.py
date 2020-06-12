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
        self.kongfu = "用工具的本领"

    def make_fish(self):
        print("利用%s抓鱼" % self.kongfu)


# MinCat，继承了Cat、Dog，Cat、Dog是父类。
class MinCat(Cat, Dog):
    def __init__(self):
        self.kongfu = "厉害的黏人本领"

    def make_fish(self):
        self.__init__()
        print("利用自己的新的技术抓鱼")

    def make_all_fish(self):
        # 1.调用父类的方法1 代码很臃肿
        Cat.__init__(self)
        Cat.make_fish(self)

        Dog.__init__(self)
        Dog.make_fish(self)
        print("-"*30)
        # 方法2. super() 带参数版本，只支持新式类
        super(MinCat, self).__init__()
        super(MinCat, self).make_fish()

        print("="*30)
        # 方法3. super()的简化版，只支持新式类
        super().__init__()
        super().make_fish()



xiaohei = MinCat()
xiaohei.make_fish()
xiaohei.make_all_fish()
print(MinCat.__mro__)

