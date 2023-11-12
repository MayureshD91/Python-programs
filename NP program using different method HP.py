
import tkinter as tk   #import function
from tkinter import messagebox

num=0
def onclick_CD(): #Clear Data command
    e1.delete(0, len(t1.get())) #start and end
    e2.delete(0, 'end')

def save_notepad():   # Save command
    for j in range(1,12):
        sum=num+j
    f=open("savenotepad.txt","a")
    f.write("SAVE" + str(num)+": "+t1.get()+","+t2.get()+"\n")
    f.close()
    messagebox.showinfo("Info recorded","SAVE" +str(num)+": "+t1.get()+","+t2.get()+"is added to NP")







window=tk.Tk()  # geometry measurement box code
window.geometry("300x200")
t1=tk.StringVar()
t2=tk.StringVar()
e1=tk.Entry(window,textvariable=t1,width=22,fg="brown")
e2=tk.Entry(window,textvariable=t2,width=22,fg="brown")
l1=tk.Label(window,text=" USER NAME ")
l2=tk.Label(window,text=" PASSWORD ")
b1=tk.Button(window,text="SAVE TO NP",command=save_notepad)
b2=tk.Button(window,text="CLEAR DATA",command=onclick_CD)

l1.pack()
e1.pack()
l2.pack()
e2.pack()
b1.pack()
b2.pack()

window.mainloop()
