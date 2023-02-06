from tkinter import *
import time

def blink(c_type_on,c_type_off, col):
    can.itemconfig(yel_l,fill = "yellow")
    main.after(1500, lambda:off_yel_c(c_type_on,c_type_off, col))
    
def off_yel_c(c_type_on,c_type_off,col):
    can.itemconfig(yel_l,fill = "white")
    can.itemconfig(c_type_off,fill = "white")
    can.itemconfig(c_type_on,fill = col)
    


def change_light(t):
    if t == "stop":
        main.after(10, lambda:blink(red_l,gr_l,"red"))    
    else: 
        main.after(10, lambda:blink(gr_l,red_l,"green"))       
        

main = Tk()
main.geometry("300x300")
main.title("Светофор ДЗ2")
can = Canvas(main, height=250, width=250, bg="white")
can.pack()
red_l = can.create_oval(115,20,135,40, width=3, fill="white")
yel_l = can.create_oval(115,45,135,65, width=3, fill="white")
gr_l = can.create_oval(115,70,135,90, width=3, fill="green")
b1 = Button(main, text="Поехали", command= lambda:change_light("go"))
b1.pack()
b2 = Button(main, text="Стоп", command= lambda:change_light("stop"))
b2.pack()



main.mainloop()
