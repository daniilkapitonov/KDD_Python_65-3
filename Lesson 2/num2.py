import time
x = [5,7,3,6,8,0,3,4,7,9,0,2,7,3,6,8,0,3,4,7,9,0,2,7,3,6,8,0,3,4,7,9,0,2,7,3,6,8,0,3,4,7,9,0,2,7,3,6,8,0,3,4,7,9,0,2]
y = [9,6,3,6,8,3,6,8,4,5,7,4,6,3,6,8,3,6,8,4,5,7,4,6,3,6,8,3,6,8,4,5,7,4,6,3,6,8,3,6,8,4,5,7,4,6,3,6,8,3,6,8,4,5,7,4]
start = time.time()
print(list(map(lambda a: 'a' if a%10>5 else 'b', [(x[i]+y[i]) for i in range(len(x))])))
print(time.time()-start)

start = time.time()
print(list(map(lambda x,y: "a" if (x+y)%10>5 else "b", x,y)))
print(time.time()-start)

