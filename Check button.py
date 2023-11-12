# CHeck button

import tkinter as tk
from tkinter import messagebox

win=tk.Tk()
def check():

    if x.get()==1:
        messagebox.showinfo("Check","checkbutton is ON")
    if x.get()==0:
        messagebox.showinfo("Check", "checkbutton is OFF")
def check1():

    if x1.get()==4:
        print("b2 on")

    if x1.get()==5:
        print("b2 off")


x = tk.IntVar()
x1 = tk.IntVar()

#ch_image=tk.PhotoImage(file="check.png") # need to provide PNG Image only

check_b=tk.Checkbutton(win,text="i am check button",variable=x,onvalue=1,offvalue=0,
                       command=check,font=('Arial',20),fg="red",bg="black")
check_b2=tk.Checkbutton(win,text="i am check button2",variable=x1,onvalue=4,offvalue=5,
                       command=check,font=('Arial',20),fg="red",bg="black").pack()


# check_b1=tk.Checkbutton(win,text="i am check button",variable=x,onvalue=1,offvalue=0,
#                        command=check,font=('Arial',20),fg="yellow",bg="black")

check_b.pack()
# check_b1.pack()
