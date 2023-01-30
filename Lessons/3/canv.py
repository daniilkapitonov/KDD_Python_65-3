from tkinter import *

main = Tk()
main.geometry("300x300")
can = Canvas(main, height=200, width=200, bg="red")
can.pack()
can.create_line(10,10,80,80, width=5)
can.create_rectangle(100,100,150,200, width=5, dash=(4,2,2))
can.create_oval(10,10,75,100, width=5, fill = "green")
# can.create_rectangle(0,0,200,200, fill="white")
can.create_polygon(10,100, 10,150,75,150, fill="white", outline="blue", width=4)
main.mainloop()