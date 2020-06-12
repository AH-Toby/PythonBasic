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
        self.__init__()
        print("利用自己的新的技术抓鱼")

    def kanmen(self):
        self.__init__()
        print("利用自己本领看门")

    def makehappy(self):
        self.__init__()  # 执行本类的__init__方法，做属性初始化 self.kongfu = "猫氏...."
        print("利用%s讨主人开心" % self.kongfu)

    def old_make_fish(self):
        # 不推荐这样访问父类的实例属性，相当于创建了一个新的父类对象
        # print("直接调用Cat类的kongfu属性：%s" % Cat().kongfu)

        # 可以通过执行Cat类的__init__方法，来修改self的属性值
        print("执行Cat类的__init__方法前，self.kongfu属性：%s" % self.kongfu)
        Cat.__init__(self)
        print("执行Cat类的__init__方法后，self.kongfu属性：%s" % self.kongfu)
        Cat.make_fish(self)

    def old_kanmen(self):
        # 不推荐这样访问父类的实例属性，相当于创建了一个新的父类对象
        # print("直接调用Dog类的kongfu属性：%s" % Dog().kongfu)

        # 可以通过执行Dog类的__init__方法，来修改self的属性值
        print("执行Dog类的__init__方法前，self.kongfu属性：%s" % self.kongfu)
        Dog.__init__(self)
        print("执行Dog类的__init__方法后，self.kongfu属性：%s" % self.kongfu)
        Dog.kanmen(self)


xiaohua = MinCat()
print(xiaohua.kongfu)  # 子类和父类有同名属性，则默认使用子类的
xiaohua.make_fish()  # 子类和父类有同名方法，则默认使用子类的
print("-"*30)
xiaohua.old_make_fish()
print("="*30)

xiaohua.kanmen()
print("-"*30)
xiaohua.old_kanmen()
print("="*30)

xiaohua.makehappy()
# 子类的魔法属性__mro__决定了属性和方法的查找顺序
print(MinCat.__mro__)
