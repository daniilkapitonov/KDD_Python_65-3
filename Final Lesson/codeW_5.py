a = [1,2,2,2,3]
b = [2]
for n in b:
    while n in a:
        a.pop(a.index(n))

print(a)