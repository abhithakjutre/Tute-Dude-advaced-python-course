from tkinter import *
window = Tk()
c = Canvas(window, width=500, height=500)
c.pack()
c.create_line(0,0,500,500, width=5, fill="green" ,dash =(3,3))
c.create_line(0,500,500,0, width=5, fill="red" ,dash =(3,3))
c.create_rectangle(150,125,450,375, fill = "blue",outline="yellow")
mainloop()
