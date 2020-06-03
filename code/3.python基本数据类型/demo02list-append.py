# 定义变量A，默认有3个元素
A = ['xiaoWang', 'xiaoZhang', 'xiaoHua']

print("-----添加之前，列表A的数据-----")
for tempName in A:
    print(tempName)

# 提示、并添加元素
temp = input('请输入要添加的学生姓名:')
A.append(temp)

print("-----添加之后，列表A的数据-----")
for tempName in A:
    print(tempName)