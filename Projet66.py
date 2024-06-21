from tkinter import *

def add_numbers():
    res=float(e1.get())+float(e2.get())
    res=round(res,4)
    lab4.config(text=res)

def sustract_numbers():
    res=float(e1.get())-float(e2.get())
    res=round(res,4)
    lab4.config(text=res)

def multiply_numbers():
    res=float(e1.get())*float(e2.get())
    res=round(res,4)
    lab4.config(text=res)

def divide_numbers():
    res=float(e1.get()) / float(e2.get())
    res=round(res,4)
    lab4.config(text=res)

    #Star of program
window =Tk()
window.title('TP PYTHON ')
window.config(background='#4065A4')
lab1=Label(window, text="Entrez le premier nombre")
lab1.grid(row=0,column=0)
lab2=Label(window, text="Entrez le deuxieme nombre")
lab2.grid(row=1,column=0)
lab3=Label(window, text="Resultat")
lab3.grid(row=2,column=0)

lab4=Label(window, text="")
lab4.grid(row=2,column=1)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b1 = Button(window,text="Ajouter",width=10,command=add_numbers)
b1.grid(row=0, column=2,padx=5,pady=5)

b2 = Button(window,text="Soustraire",width=10,command=sustract_numbers)
b2.grid(row=0, column=3,padx=5,pady=5)

b3 = Button(window,text="Multiply",width=10,command=multiply_numbers)
b3.grid(row=1, column=2,padx=5,pady=5)

b4 = Button(window,text="Divide",width=10,command=divide_numbers)
b4.grid(row=1, column=3,padx=5,pady=5)

window.mainloop()



















