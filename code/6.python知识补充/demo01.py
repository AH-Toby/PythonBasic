# 计算n的阶乘!n = 1*2*3*4*....*n
def calNum(n):
    if n >= 1:
        print(n)
        result = n * calNum(n - 1)
    else:
        result = 1
    return result


if __name__ == '__main__':
    n = int(input("请输入n:"))
    print(calNum(n))
