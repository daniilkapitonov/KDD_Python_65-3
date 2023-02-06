from tkinter import *
from tkinter import messagebox

def plus(n1,n2,o):
    res = 0
    if n1!="" and n2!="" and o!="":
        n1 = float(n1)
        n2 = float(n2)
        if o=="+":
            res = n1+n2
        elif o=="-":
            res = n1-n2
        elif o=="*":
            res = n1*n2
        elif o=="/":
            if n2!=0:
                res = n1/n2
            else:
                messagebox.showerror("Zero","Делить на 0 нельзя")
                return
        messagebox.showinfo("Результат", res)
    else:
       messagebox.showerror("Пусто","Одно из значений отсуствует")
       return 

main = Tk()
main.geometry("200x200")

e1 = Entry(main)
e1.pack()
e2 = Entry(main)
e2.pack()
e3 = Entry(main)
e3.pack()
b1 = Button(main, text="Click", command=lambda:plus
            (e1.get(), e2.get(), e3.get()))
b1.pack()
main.mainloop()
