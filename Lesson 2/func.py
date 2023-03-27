def standard_function(x):#стандартное объявление функции
    return x*2


lambda_function = lambda x: x*9# объявление анонимной функции

print(standard_function(10), lambda_function(10))

print(list(map(standard_function,[1,2,3,4,5,6])))

def f(*a):
    return a*4
print()
print(list(map(f,[1,2,3,5])))
print()
circle_areas = [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]
mas = [1]*len(circle_areas)
result1 = list(map(round, circle_areas,mas)) 
result2 = list(map(round, circle_areas, [i for i in range(1,len(circle_areas)+1)]))
print(circle_areas)
print(result1)
print(result2)

round(circle_areas[0],mas[0])
round(circle_areas[1],mas[1])
round(1.231, 2)


