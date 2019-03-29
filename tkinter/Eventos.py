from tkinter import *

'''
def inc():
 n = int(rotulo.configure("text")[4])+1
 rotulo.configure(text=str(n))

b = Button(text="Incrementa",command=inc)
b.pack()
rotulo = Label(text="0")
rotulo.pack()


# Alterando Propriedades
a = Button()
a["text"]= "Botão"
a.pack()
'''


def clica(e):
    txt = "Mouse Clicado em: \n {}, {}".format(e.x,e.y)
    r["text"] = txt

r = Label()
r.pack(expand=True, fill="both")
r.master.geometry("200x200")

# Bind = Apertar
r.bind("<Button-1>", clica)

mainloop()


