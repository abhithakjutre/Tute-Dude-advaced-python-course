from tkinter import *

root = Tk()

entry  = Entry()
entry.pack()
listbox = Listbox(root)
listbox.pack()
entry.pack(side=BOTTOM)
button = Button(root, text="Send")
button.pack(side=BOTTOM)
root.mainloop()


