from tkinter import *

window = Tk()

menu = Menu(window)
file = Menu(menu, tearoff=0)
file.add_command(label = "New tab")
file.add_command(label = "New window")
file.add_command(label = "New Markdown tab")
file.add_command(label = "Open")
file.add_command(label = "Recent")
file.add_command(label = "Save")
file.add_command(label = "Save As")
file.add_command(label = "Open")
file.add_separator()
file.add_command(label = "Page setup")
file.add_command(label = "Print")
file.add_separator()
file.add_command(label = "Close tab")
file.add_command(label = "Close window")
file.add_command(label = "Exit", command=window.quit)

menu.add_cascade(label="File", menu= file)
window.config(menu = menu)




window.mainloop()
