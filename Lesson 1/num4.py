import math
a = int(input('a - '))
b = int(input('b - '))
c = int(input('c - '))

d = b**2 - 4*a*c
print('D =',d)
if d<0:
    print('Решения нет')
elif d==0:
    print('Корень уравнения =', -(b/(2*a)))
elif d>0:
    print('Корень №1 -', ((-b+math.sqrt(d))/(2*a)),
          'Корень №2 -',((-b-math.sqrt(d))/(2*a)))