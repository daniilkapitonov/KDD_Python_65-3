def count_args(*args):
    print(args, type(args))
    for arg in args:
        print(type(arg), arg)
    return len(args)

def mean(*args):
    summ = 0
    count = 0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            # print(type(arg), arg)
            # print((type(arg) == int or float))
            summ+=arg
            count+=1

    return float(summ)/count

def greet(*args):
    ret_txt = 'Hello, '
    if len(args) == 1:
        ret_txt+=args[0]+'!'
    else:
        for i in range(0,len(args)-1):
            ret_txt += args[i]
            if i+1 !=len(args)-1:
                ret_txt+=', '
        ret_txt +=' and '+args[-1]+'!'
    return ret_txt


print(count_args(1,2,3,4,5,'213123123',-12,[1,2,3,4,5]))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) 
print(mean(-1, 2, 3, 10, ('5'))) 
print()
print(greet('Timur', 'Roman', 'Roman', 'Roman', 'Roman', 'Roman', 'Roman'))
print(greet('Timur'))
print(greet('Timur', 'Pasha'))
print(greet('Timur', 'Pasha', 'Daniil'))
mass = [[1,2,3],[4,5,6],[7,8,9]]
