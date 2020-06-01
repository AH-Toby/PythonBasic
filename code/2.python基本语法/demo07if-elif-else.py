height = int(input("请输入你的身高（cm）："))
if height > 150:
    print("身高超过150cm需要买票！")
elif height >0 and height <= 150:
    print("身高在150cm以下免费！")
else:
    print("输入的数值有问题")