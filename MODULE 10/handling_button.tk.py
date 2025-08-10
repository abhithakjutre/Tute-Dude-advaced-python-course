from tkinter import *

from wmi import connect

window = Tk()
window.title("Pack")
window.geometry("500x600")
def log_entry():
    print("Logged in")
button = Button(window, text = "LOGIN",command=log_entry,width=12, bg="red",fg="white",font=("bold",12),activebackground="darkgreen",activeforeground="white")
button.pack()
window.mainloop()