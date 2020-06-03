# 定义变量A，默认有3个元素
A = ['xiaoWang', 'xiaoZhang', 'xiaoHua']

print("-----修改之前，列表A的数据-----")
for tempName in A:
    print(tempName)

# 修改元素
A[1] = 'xiaoLu'

print("-----修改之后，列表A的数据-----")
for tempName in A:
    print(tempName)