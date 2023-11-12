
# RGB Button

import tkinter as tk

def red():
    label1.config(bg="red",font=("Elephant",18,"bold"),text="RED BUTTON IS PRESSED")
    button1.config(bg="red")

def green():
    label1.config(bg="green", font=("Elephant", 18, "bold"), text = "GREEN BUTTON IS PRESSED")
    button2.config(bg="green")

def blue():
    label1.config(bg="blue", font=("Elephant", 18, "bold"), text = "BLUE BUTTON IS PRESSED")
    button3.config(bg="blue")

windows=tk.Tk()
windows.geometry("600x300")

label1=tk.Label(windows,text="pls change my color",bg="yellow")
button1=tk.Button(windows,fg="#1e81b0",text="RED",command=red,activebackground="red",height=2,width=40,font=("elephant",18))
button2 = tk.Button(windows,fg="#1e81b0",text="GREEN",command=green,activebackground="red",height=2,width=40,
                        font=("Arial",18))
button3 = tk.Button(windows,fg="#1e81b0",text="BLUE",command=blue,activebackground="red",height=2,width=40,
                        font=("Consolas",18))


label1.pack()
button1.pack()
button2.pack()
button3.pack()

windows.mainloop()

