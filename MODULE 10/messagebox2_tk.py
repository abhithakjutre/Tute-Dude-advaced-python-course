from tkinter import *

window = Tk()
window.geometry("500x500")
'''message = Message(window, text = "python")
message.pack()
var = StringVar()
message = Message(window, textvariable=var,relief=RAISED, padx=20, pady=20)
var.set("Welcome")
message.pack()
'''
var = StringVar()
entvar = StringVar()
def insert():
    result = entvar.get()
    var.set(result)
message = Message(window,textvariable=var, relief=RAISED, padx=50,pady=50)
entry = Entry(window,textvariable=entvar)
button = Button(window, text="Ok",command=insert)
message.pack()
entry.pack()
button.pack()


mainloop()
