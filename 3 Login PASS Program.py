# 3 Login pass program

import tkinter as tk
from tkinter import messagebox

def onclick_SUB():
    if t1.get()=="vikas" and t2.get()=="kadam":
        messagebox.showinfo("LOGIN","CORRECT DATA")
    elif t1.get()=="mayuresh" and t2.get()=="donde":
        messagebox.showinfo("LOGIN","CORRECT DATA")
    elif t1.get()=="purva" and t2.get()=="dongre":
        messagebox.showinfo("LOGIN","CORRECT DATA")
    else:
        messagebox.showinfo("LOGIN", "IN-CORRECT DATA")


def onclick_CD():
    t1.set("")
    t2.set("")

window=tk.Tk()
window.geometry("350x200")
t1=tk.StringVar()
t2=tk.StringVar()
e1=tk.Entry(window,textvariable=t1,width=20, fg="red",relief="sunken")
e2=tk.Entry(window,textvariable=t2,width=20,fg="red",show="@")
l1=tk.Label(window,text="USER NAME")
l2=tk.Label(window,text="PASSWORD")
b1=tk.Button(window,text="SUBMIT",command=onclick_SUB)
b2=tk.Button(window,text="CLEAR DATA",command=onclick_CD)


l1.pack()
e1.pack()
l2.pack()
e2.pack()
b1.pack()
b2.pack()

window.mainloop()