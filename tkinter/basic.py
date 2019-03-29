from tkinter import *


"""
class Interface(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.msg = Label(self, text="Hello World").pack()
        self.bye = Button(self, text="Bye", command=self.quit).pack()
        self.pack()    
        
app = Interface()
app.master.title("Exemplo")
app.master.geometry("200x200+100+100")


mainloop()
"""


top = Frame()
top.pack(fill="both", expand=True)

a = Label(top, text="a"); a.pack(side="left",
                                 expand=True, fill="y")
b = Label(top, text="b"); b.pack(side="bottom",
                                 expand=True, fill="both")
c = Label(top, text="c"); c.pack(side="right")
d = Label(top, text="d"); d.pack(side="top")



for widget in (a,b,c,d):
    widget.configure(relief="groove", border=5,
                     font="Times 24")

top.mainloop()
