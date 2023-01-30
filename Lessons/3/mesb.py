from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("300x300")
messagebox.showinfo('Info', "Information")
messagebox.showerror('Info', "Information")
messagebox.showwarning('Info', "Information")
print(messagebox.askokcancel('Info', "Information"))
main.mainloop()