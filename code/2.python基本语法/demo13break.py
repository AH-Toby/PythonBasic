i = 10

while i > 0:
    print("妈，还要我刷啊~~~~~~~~~")
    if i == 5:
        print('好了，不用刷了')
        break

    print("正在刷 %d 个碗" % i)
    i -= 1

print('程序结束')