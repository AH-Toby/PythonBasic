# 从键盘输入身高，如果身高没有超过150cm，则进动物园不用买票，否则需要买票。
height = int(input("请输入你的身高（cm）："))
if height > 150:
  print("身高超过150cm需要买票！")
else:
  print("身高不超过150cm不需要买票！")