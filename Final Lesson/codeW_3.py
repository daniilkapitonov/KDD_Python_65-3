value = 153
print(sum([int(i)**len(str(value)) for i in str(value)]))