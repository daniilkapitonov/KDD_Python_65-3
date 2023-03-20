import random

for i in range(10):
    for j in range(10):
        print(str(random.randint(0,20)).ljust(2), end = " ")
    print()