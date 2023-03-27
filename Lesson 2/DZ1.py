def matrix(*a):
    s = len(a)
    if s==0:
        return [0]
    elif s==1:
        return [0]*a[0]
    elif s==2:
        m = []
        for i in range(0,a[0]):
            c = []
            for j in range(0,a[1]):
                c.append(0)
            m.append(c)
        return m
    elif s == 3:
        m = []
        for i in range(0,a[0]):
            c = []
            for j in range(0,a[1]):
                c.append(a[2])
            m.append(c)
        return m
    else:
        return "err"
    
print(matrix())
print(matrix(2))
print(matrix(3,5))
print(matrix(5,6,7))

