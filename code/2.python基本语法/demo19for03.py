name = 'helllo world!'
for x in name:
    if x == 'e':
        print("不能使用字符 e")
        break
    else:
        print(x)
else:
    print('没有出现禁止使用的字符')