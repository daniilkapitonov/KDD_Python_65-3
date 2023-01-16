import random
n = 7
matr = []
cash = []
for i in range(n):
    for j in range(n):
        cash.append(random.randint(-100,100))
    matr.append(cash)
    cash = []

sum =0
for i in range(n):
    for j in range(n):
         print(matr[i][j], end =" ")   
         sum += matr[i][j]
        
    print(", sum =", sum)
    sum = 0