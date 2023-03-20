num = int(input())
if num>=2 and num>=4 and num<=8 and num <=10:
    print("Принадлежит всем отрезкам")
else:
    print("Не принадлежит всем отрезкам")
    if num>=2:
        print("Принадл. отрезку 2+")
    if num>=4:
        print("Принадл. отрезку 4+")
    if num<=8:
        print("Принадл. отрезку -8")
    if num<=10:
        print("Принадл. отрезку -10")