import roman
import random

for i in range(20):
    r = random.randint(0,1000)
    print(r,roman.int_to_roman(r))

print("CCLXXX", roman.roman_to_int("CCLXXX"))
print("DCCCXXXIX", roman.roman_to_int("DCCCXXXIX"))
print("DLXII", roman.roman_to_int("DLXII"))