from tkinter import *

window = Tk()
window.title("Pack")
window.geometry("500x600")
label1 =Label(window, text="Label1",bg="red",fg="white")
label2 =Label(window, text="Label2",bg="blue",fg="white")
label3 =Label(window, text="Label3",bg="green",fg="white")
label4 =Label(window, text="Label4",bg="yellow",fg="black")
label1.pack(side=TOP,fill=X,expand=False)
label2.pack(side=LEFT,fill=Y,expand=False)
label3.pack(side=RIGHT,fill=Y,expand=False)
label4.pack(side=BOTTOM,fill=X,expand=False)

window.mainloop()