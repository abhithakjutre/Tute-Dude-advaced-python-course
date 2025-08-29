from tkinter import *


window = Tk()
window.title("ABHI PORTAL")
window.geometry("500x700")


signup_text = Label(text="SIGNUP PAGE",font=("Arial Bold",25,))
signup_text.place(x=130,y=20)

username = Label(text="USER NAME",font=("Arial",16,))
username1 = Entry(window,width=50,borderwidth=5)
email = Label(text="EMAIL ID",font=("Arial",16,))
dob = Label(text="DATE OF BIRTH",font=("Arial",16,))
password = Label(text="PASSWORD",font=("Arial",16,))
cpassword = Label(text="CONFORM PASSWORD",font=("Arial",16,))
username.place(x=100,y=150)
username1.place(x=100,y=180)
email.place(x=100,y=250)

mainloop()