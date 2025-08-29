from tkinter import *

from Demos.BackupSeek_streamheaders import win32_stream_id_size

window = Tk()
window.title("Calculator")
window.resizable(False,False)
window.geometry("300x460")


# Entry Box Section
entry_box = Entry(window,width=300, font=("Lacquer Static",25),bg="#d1d0cd",justify="right")
entry_box.pack(ipady=40)

# Button Section
def click(num):
    result = entry_box.get()
    entry_box.delete(0,END)
    entry_box.insert(0, str(result) + str(num))

def clear():
    entry_box.delete(0,END)


b = Button(window,width=8, height=4,text="7",command=lambda:click(7))
b.place(x=10,y=140)
b = Button(window,width=8, height=4,text="8",command=lambda:click(8))
b.place(x=80,y=140)
b = Button(window,width=8, height=4,text="9",command=lambda:click(9))
b.place(x=150,y=140)



b = Button(window,width=8, height=4,text="➗",command=lambda:click("/"))
b.place(x=220,y=140)
b = Button(window,width=8, height=4,text="4",command=lambda:click(4))
b.place(x=10,y=220)
b = Button(window,width=8, height=4,text="5",command=lambda:click(5))
b.place(x=80,y=220)
b = Button(window,width=8, height=4,text="6",command=lambda:click(6))
b.place(x=150,y=220)



b = Button(window,width=8, height=4,text="✖️",command=lambda:click("*"))
b.place(x=220,y=220)
b = Button(window,width=8, height=4,text="1",command=lambda:click(1))
b.place(x=10,y=300)
b = Button(window,width=8, height=4,text="2",command=lambda:click(2))
b.place(x=80,y=300)
b = Button(window,width=8, height=4,text="3",command=lambda:click(3))
b.place(x=150,y=300)



b = Button(window,width=8, height=4,text="➖",command=lambda:click("-"))
b.place(x=220,y=300)
b = Button(window,width=8, height=4,text="C",command=clear,bg="#ff3512",fg="white")
b.place(x=10,y=380)
b = Button(window,width=8, height=4,text="0",command=lambda:click(0))
b.place(x=80,y=380)

def equal():
    expersion = entry_box.get()
    if expersion and expersion[-1] in "+/-*":
       expersion =  expersion[0:-1]

    try:
       result =  eval(expersion) # This eval function use for solve equations and it gives final result
       entry_box.delete(0,END)
       entry_box.insert(0,result)

    except:
        entry_box.delete(0,END)
        entry_box.insert("Error!")

# def equal2():
#     expr = entry_box.get()
#
#     # If last char is operator, remove it
#     if expr and expr[-1] in "+-*/":
#         expr = expr[:-1]
#
#     # Find and process operator
#     for op in ["+", "-", "*", "/"]:
#         if op in expr:
#             pos = expr.find(op)
#             try:
#                 first = int(expr[:pos])      # Before operator
#                 second = int(expr[pos+1:])   # After operator
#
#                 # Perform operation
#                 if op == "+":
#                     result = first + second
#                 elif op == "-":
#                     result = first - second
#                 elif op == "*":
#                     result = first * second
#                 elif op == "/":
#                     if second != 0:
#                         result = first / second
#                         float(result)
#                     else:
#                         result = "Error"
#
#             except ValueError:
#                 result = "Error"
#
#             # Show result
#             entry_box.delete(0, END)
#             float(result)
#             entry_box.insert(0, result)
#             break
#


b = Button(window,width=8, height=4,text="🟰",command=equal,bg="#e89356")
b.place(x=150,y=380)


b = Button(window,width=8, height=4,text="➕",command=lambda:click("+"))
b.place(x=220,y=380)


mainloop()
