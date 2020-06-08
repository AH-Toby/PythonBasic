def test1():
    # 通过return将一个数据结果返回
    return 20


def test2():
    # 1. 先调用test1并且把结果返回来
    result = test1()
    # 2. 对result进行处理
    print(result)


# 调用test2时，完成所有的处理
test2()
