floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]

res1 = list(map(lambda x:x**2, floats))
print(res1)
print(list(map(round,res1,[1]*len(res1))))


print()
def s_r(x):
    return round(x**2,1)
print(list(map(s_r,floats)))