from tkinter import *

window = Tk()

window.title("Login")
window.geometry("500x600")
label1 = Label(window,text= "mail")
label2 = Label(window,text= "password")
e1 = Entry(window, width=40, borderwidth=5)
e2 = Entry(window, width=40, borderwidth=5)
label1.grid(row=0, column=1)
label2.grid(row=1,column=1)
e1.grid(row=0, column=2)
e2.grid(row=1, column=2)


mainloop()