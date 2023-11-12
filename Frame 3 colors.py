
# 3 color frames

import tkinter as tk
from tkinter import colorchooser

def cg_color():
    color=colorchooser.askcolor()
    print(color)
    win.config(bg=color[1])
    b1.config(fg=color[1])

win=tk.Tk()

win.geometry("250x250")

b1=tk.Button(win,text="Red",command=cg_color)
b1.pack()

b1=tk.Button(win,text="Green",command=cg_color)
b1.pack()

b1=tk.Button(win,text="Pink",command=cg_color)
b1.pack()
win.mainloop()
