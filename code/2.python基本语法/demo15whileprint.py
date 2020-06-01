"""
要求：打印如下图形：

    *
    * *
    * * *
    * * * *
    * * * * *
"""
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("* ", end='')
        j += 1

    print("\n", end="")
    i += 1
