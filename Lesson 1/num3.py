txt = input('Введите строку - ')

count = 0
mass = []
for l in txt:
    if l == "Р":
        count += 1
    else:
        mass.append(count)
        count = 0
mass.append(count)
print(mass)
print(max(mass))