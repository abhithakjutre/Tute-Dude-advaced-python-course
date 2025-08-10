from tkinter import *

window = Tk()
window.geometry("500x500")
check_box1 = IntVar()
check_box2 = IntVar()
check_box3 = IntVar()
chk_btn_1 = Checkbutton(window, text = "Python",offvalue=0,height=2,width=10)
chk_btn_2  = Checkbutton(window, text = "C Language",offvalue=0,height=2,width=10)
chk_btn_3 = Checkbutton(window, text = "Java",offvalue=0,height=2,width=10)

chk_btn_1.pack()
chk_btn_2.pack()
chk_btn_3.pack()


mainloop()