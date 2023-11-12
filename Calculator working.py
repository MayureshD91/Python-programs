# Calculator extra

import tkinter as tk
from tkinter import messagebox

a=input("Please enter value A")
b=input("Please enter Value B")



def oneclick_add():
    c=a+b
    messagebox.showinfo("+",message="Addition is"+str(c))
def oneclick_sub():
    d=a-b
    messagebox.showinfo("+",message="Substraction is"+str(d))
def oneclick_mul():
    x=a*b
    messagebox.showinfo("+",message="Multiplication is"+str(x))
def oneclick_div():
    y=a/b
    messagebox.showinfo("+",message="Division is"+str(y))




window=tk.Tk()
window.geometry("300x150")

b1=tk.Button(window,text="+",command=oneclick_add)
b2=tk.Button(window,text="-",command=oneclick_sub)
b3=tk.Button(window,text="*",command=oneclick_mul)
b4=tk.Button(window,text="/",command=oneclick_div)


b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)

window.mainloop()

