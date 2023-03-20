import random
a = []
for i in range(0,10):
    a.append(random.randint(0,100))
min_m = 0
max_m = 0
sum_m = 0
print(a)
for i in a: #Search max
    if i>max_m:
        max_m = i 
print("Max", max_m, max(a))

min_m = max_m
for i in a: #Search min
    if i<min_m:
        min_m = i
print("Min", min_m, min(a))

for i in a:
    sum_m+=i
print("Sum", sum_m, sum(a))