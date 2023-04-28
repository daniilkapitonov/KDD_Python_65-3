text = "The_Stealth_Warrior"
t = list(text)
c = ['-','_']
for cc in c:
    while cc in t:
        t[t.index(cc)+1] = t[t.index(cc)+1].upper()
        t.pop(t.index(cc))

print(''.join(t))
