movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']

print('------删除之前------')
for tempName in movieName:
    print(tempName)

movieName.remove('指环王')

print('------删除之后------')
for tempName in movieName:
    print(tempName)