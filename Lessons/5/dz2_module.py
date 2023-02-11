def step(n,s):
    return n**s

def t_to_d(n):
    s = ""
    while n!=1:
        s+=str(n%2)
        n//=2
    s+="1"
    s = s[::-1]
    return s