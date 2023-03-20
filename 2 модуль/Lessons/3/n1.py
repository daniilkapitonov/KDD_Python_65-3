from tkinter import *

def plus():
    l1['text'] = int(e1.get()) + int(e2.get())

main = Tk()
main.geometry("200x200")
l1 = Label(main)
l1.pack()
e1 = Entry(main)
e1.pack()
e2 = Entry(main)
e2.pack()
b1 = Button(main, text="Click", command=plus)
b1.pack()
main.mainloop()
