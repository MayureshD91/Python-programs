# Calculator Working program/project

import tkinter as tk
from tkinter import messagebox



def oneclick_add():
    messagebox.showinfo("+",message="Addition is"+str(t1.get()+t2.get()))
def oneclick_sub():

    messagebox.showinfo("+",message="Substraction is"+str(t1.get()-t2.get()))
def oneclick_mul():

    messagebox.showinfo("+",message="Multiplication is"+str(t1.get()*t2.get()))
def oneclick_div():
    try:
        messagebox.showinfo("+",message="Division is"+str(t1.get()/t2.get()))
    except:
        messagebox.showinfo("error",message="Divide by zero is not possible, pls enter correctly")




def oneclick_CD():
    t1.set("0")
    t2.set("0")




window=tk.Tk()
window.geometry("300x150")
t1=tk.IntVar()
t2=tk.IntVar()
e1=tk.Entry(window,textvariable=t1,width=30,fg="blue")
e2=tk.Entry(window,textvariable=t2,width=30,fg="blue")
l1=tk.Label(window,text="VALUE 1")
l2=tk.Label(window,text="VALUE 2")

b1=tk.Button(window,text="+",command=oneclick_add)
b2=tk.Button(window,text="-",command=oneclick_sub)
b3=tk.Button(window,text="*",command=oneclick_mul)
b4=tk.Button(window,text="/",command=oneclick_div)
b5=tk.Button(window,text="CLEAR DATA",command=oneclick_CD)


l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=3,column=0)
b4.grid(row=3,column=1)
b5.grid(row=4,column=0)



window.mainloop()











