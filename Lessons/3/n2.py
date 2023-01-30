from tkinter import *
def change():
    global check
    if check:
        can.itemconfig(l1, fill = "red")
        can.itemconfig(l2, fill = "black")
        check = False
    else:
        can.itemconfig(l1, fill = "black")
        can.itemconfig(l2, fill = "yellow")
        check = True
check = True
main = Tk()
main.geometry("300x300")
can = Canvas(main, height=200, width=200, bg="red")
can.pack()
s = can.create_rectangle(80,20,120,100, fill="black")
l1 = can.create_oval(82,22,118,42, outline="red", width=2, fill="black")
l2 = can.create_oval(82,45,118,65, outline="yellow", width=2)
b = Button(main, text="Click", command=change)
b.pack()
main.mainloop()