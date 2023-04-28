a = [-2]

summ = []
c=0
s = 0
for n in a:
    if c and n>=0:
        s+=n
    if n<0 and c==0:
        c = 1
    elif n<0 and c==1:
        summ.append(s)
        s=0
if len(summ)>0:
    print (max(summ))
else:
    print(-1 )    