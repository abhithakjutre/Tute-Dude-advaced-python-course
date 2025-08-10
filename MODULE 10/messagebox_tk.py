
from tkinter import *
import tkinter.messagebox


window = Tk()
tkinter.messagebox.showwarning("Info", "Running out time")
question =  tkinter.messagebox.askokcancel("window","do you want to exit or not")
if question == True:
    print("window closed")
    
else:
    print("okay")

mainloop()