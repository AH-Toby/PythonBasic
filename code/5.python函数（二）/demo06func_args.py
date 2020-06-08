def func(a, b, *args, **kwargs):
    """可变参数演示示例"""
    print("a=%s" % a)
    print("b=%s" % b)
    print("args:", end="")
    print(args)
    print("kwargs:", end="")
    for key, value in kwargs.items():
        print("key=%s," % key, end="")
        print("value=%s" % value, end="\n")


# 注意参数对应
func(1, 2, 3, 4, 5, m=6, n=7, p=8)
print("---------------------------")

c = (3, 4, 5)
d = {"m": 6, "n": 7, "p": 8}
# 注意元组和字典的传参方式
func(1, 2, *c, **d)

print("---------------------------")
# 不加*比较
func(1, 2, c, d)
