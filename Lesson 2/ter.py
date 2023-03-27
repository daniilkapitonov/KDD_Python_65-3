a = 20
b = 20
res1 = 'Greater' if a > b else 'Lower'
res2 = 'Equal' if a == b else 'Not equal' 
print(res1) 
print(res2) 

a = 25
b = 20
res1 = 'Greater' if a > b else 'Lower'
res2 = 'Equal' if a == b else 'Not equal' 
print(res1) 
print(res2) 

def func(elem):
    return elem < 0
numbers = [-1, 2, -3, 4, 0, -20, 10]
positive_numbers = list(filter(func, numbers))
print(positive_numbers)


