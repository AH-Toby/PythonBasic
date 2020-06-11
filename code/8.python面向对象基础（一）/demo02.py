class Hero(object):
    """定义了一个英雄类，可以移动和攻击"""

    def __init__(self, name, skill, hp, atk, armor):
        """ __init__() 方法，用来做变量初始化 或 赋值 操作"""
        # 英雄名
        self.name = name  # 实例变量
        # 技能
        self.skill = skill
        # 生命值：
        self.hp = hp  # 实例变量
        # 攻击力
        self.atk = atk
        # 护甲值
        self.armor = armor

    def move(self):
        """实例方法"""
        print("%s 正在前往事发地点..." % self.name)

    def attack(self):
        """实例方法"""
        print("发出了一招强力的%s..." % self.skill)

    # def info(self):
    #     print("英雄 %s 的生命值 :%d" % (self.name, self.hp))
    #     print("英雄 %s 的攻击力 :%d" % (self.name, self.atk))
    #     print("英雄 %s 的护甲值 :%d" % (self.name, self.armor))

    def __str__(self):
        """
            这个方法是一个魔法方法 (Magic Method) ，用来显示信息
            该方法需要 return 一个数据，并且只有self一个参数，当在类的外部 print(对象) 则打印这个数据
        """
        return "英雄 <%s> 数据： 生命值 %d, 攻击力 %d, 护甲值 %d" % (self.name, self.hp, self.atk, self.armor)


taidamier = Hero("泰达米尔", "旋风斩", 2600, 450, 200)
gailun = Hero("盖伦", "大宝剑", 4200, 260, 400)

# 如果没有__str__ 则默认打印 对象在内存的地址。
# 当类的实例化对象 拥有 __str__ 方法后，那么打印对象则打印 __str__ 的返回值。
print(taidamier)
print(gailun)

# 查看类的文档说明，也就是类的注释
print(Hero.__doc__)
