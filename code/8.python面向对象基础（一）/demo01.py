class Hero(object):
    def info(self):
        """info 是一个实例方法，类对象可以调用实例方法，实例方法的第一个参数一定是self"""
        print(self)
        """当对象调用实例方法时，Python会自动将对象本身的引用做为参数，传递到实例方法的第一个参数self里"""
        print("self各不同，对象是出处")


# Hero这个类 实例化了一个对象
super_man = Hero()
# 对象调用实例方法info()，执行info()里的代码
# . 表示选择属性或者方法
super_man.info()

print(super_man)  # 打印对象，则默认打印对象在内存的地址，结果等同于info里的print(self)
print(id(super_man))  # id(super_man)则是内存地址的十进制形式表示
