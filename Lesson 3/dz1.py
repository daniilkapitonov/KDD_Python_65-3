def print_all(*a, sep = " ", end = "\n"):
    return sep.join([str(i) for i in a])+end


print(print_all(1,2,3,4))
print(print_all(1,2,3,4,sep="|", end='end'))
print(print_all(1,2,3,4, end = '|'))