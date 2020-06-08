def sum_nums_3(a, *args, b=22, c=33, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


sum_nums_3(100, 200, 300, 400, 500, 600, 700, b=1, c=2, mm=800, nn=900)
