import sqlite3
from Tkinter import *
import tkMessageBox
from tkMessageBox import *

window1 = Tk()
window1.attributes("-fullscreen",True)
window1.configure(bg='dark grey')
window1.title("Welcome")
image1=PhotoImage(file="theye2.gif")
lb=Label(window1 ,image=image1,bg='black',bd=15)
lb.pack()
Label(window1,text='',bg='dark grey').pack()
Label(window1 , text="Name: Amartya Singh",font="Arial 18 bold",bg='dark grey').pack()
Label(window1 , text="Enroll no. : 171B169",font="Arial 18 bold",bg='dark grey').pack()
Label(window1 , text="Email id: singhamartya@gmail.com",font="Arial 18 bold",bg='dark grey').pack()
Label(window1 , text="Mobile: 7692084936",font="Arial 18 bold",bg='dark grey').pack()

def fun(e):
    window1.destroy()
    import the_eye
    


lb.bind('<Motion>',fun)

window1.mainloop()

