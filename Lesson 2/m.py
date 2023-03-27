import math as m

print(all([5,1]))
print(all([True,False]))
print(all([False,False]))

print(any([0,1]))
print(any([True,False]))
print(any([False,False]))

numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]
result = all(map(lambda x: True if x > 10 else False, numbers))
print('Все числа больше 10' if result else 'Хотя бы одно число меньше или равно 10')
# if result:
#     print('Все числа больше 10')
# else:
#     print('Хотя бы одно число меньше или равно 10')

