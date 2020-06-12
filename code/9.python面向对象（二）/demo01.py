# 老猫将自己的一身本领传给小猫

# 定一个父类


class Cat(object):
    def __init__(self):
        self.kongfu = "厉害的捉鱼本领"

    def make_fish(self):
        print("利用%s抓鱼" % self.kongfu)


# MinCat，继承了Cat，Cat是父类。
class MinCat(Cat):
    pass


xiaohua = MinCat()
print(xiaohua.kongfu)
xiaohua.make_fish()
