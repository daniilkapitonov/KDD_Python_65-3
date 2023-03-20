import random
m2 = [[2,3,4],[5,6,7],[8,9,0]]
print(m2[0])
print(m2[1])
print(m2[2])
for i in range(len(m2)):
    for j in range(len(m2[0])):
         print(m2[i][j], end =" ")   
    print()

n = 7
matr = []
cash = []
for i in range(n):
    for j in range(n):
        cash.append(random.randint(-100,100))
    print(cash)
    matr.append(cash)
    cash = []
print(matr)

for i in range(n):
    for j in range(n):
         print(matr[i][j], end =" ")   
    print()