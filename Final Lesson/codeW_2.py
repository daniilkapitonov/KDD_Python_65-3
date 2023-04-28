n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
n = list(map(str,n))
print(f"({''.join(n[0:3])}) {''.join(n[3:6])}-{''.join(n[6:])}")