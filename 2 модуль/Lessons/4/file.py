f = open(r'C:\Users\dan-1\Desktop\Pr_2035\KDD_Python_65-3\Lessons\4\text.csv','r')
print(f.readlines())
f.close()

f = open(r'C:\Users\dan-1\Desktop\Pr_2035\KDD_Python_65-3\Lessons\4\text.csv','a+')
f.write("\nText")
f.close()

f = open(r'C:\Users\dan-1\Desktop\Pr_2035\KDD_Python_65-3\Lessons\4\text.csv','r')
print(f.readlines())
f.close()
