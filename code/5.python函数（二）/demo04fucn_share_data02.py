def test1():
    # 通过return将一个数据结果返回
    return 50


def test2(num):
    # 通过形参的方式保存传递过来的数据，就可以处理了
    print(num)


# 1. 先调用test1得到数据并且存到变量result中
result = test1()

# 2. 调用test2时，将result的值传递到test2中，从而让这个函数对其进行处理
test2(result)