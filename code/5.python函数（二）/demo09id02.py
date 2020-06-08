a = [1, 2]
b = a
print(b)
print(id(b))
print(a)
print(id(a))
a.append(3)
print(b)
print(id(b))
print(a)
print(id(a))
