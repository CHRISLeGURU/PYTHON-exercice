import tkinter as tk
from tkinter import ttk
from tkinter import *
Chris = tk.Tk()
Chris.geometry("400x250")
Chris.title("PROGRAMMATION EVENEMENTIELLE: PYTHON")
def my_upd(*args):
    total=sel1.get()+int(t1.get('1.0',END))
    l1.config(text=total)
sel1 = tk.IntVar()
sel1.set(0)
data=[5,3,15,22]
cb1=ttk.Combobox(Chris, values = data,height=3, width=5, 
                   font=22, textvariable=sel1)
cb1.grid(row=0, column=0, padx=10,pady=10)
t1=tk.Text(Chris,width=10, height=1, bg='yellow', font=22)
t1.grid(row=0,column=1,padx=5)
t1.insert(tk.END,0)
l1=tk.Label(Chris, text='Total', font=22,fg='blue')
l1.grid(row=0,column=2,padx=5)
b1=tk.Button(Chris,text='Sum',font=22,command=lambda:my_upd())
b1.grid(row=1,column=1)
sel1.trace('w',my_upd)
Chris.mainloop()