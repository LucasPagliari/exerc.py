# Guess Game Tkinter:

from tkinter import * 
from random import randint
 
def new(opc):

    x = randint(0,20)
    y = randint(0,20)
    resCorreta = x*y

    num1["text"]= str(x) 
    num2["text"]= str(y)
    oper["text"]= "X"
    return x*y
        
        
def send():
    res = ent.get()
    if  0 == res:
        dado["text"] = "Correto"
            
    else:
        dado["text"] = "Errado"

    
num1 = Label()
oper = Label()
num2 = Label()
dado = Label(text="0")

ent = Entry()

num1.pack()
oper.pack()
num2.pack()

ent.pack()

dado.pack()

num1.master.geometry("160x180")

btn1 = Button(text="New",command=new(1))
btn2 = Button(text="Send",command=new(2))

btn1.pack(side="bottom",fill="x")
btn2.pack(side="bottom",fill="x")

mainloop()
