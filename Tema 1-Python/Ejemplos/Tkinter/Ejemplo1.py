from tkinter import *

window = Tk()
window.title("Bienvenido a mi App")
window.geometry('360x250')

lbl = Label(window, text="Hello", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="", font=("Arial Bold", 20))
lbl2.grid(column=1, row=0)

txt = Entry(window, width=12)
txt.grid(column=1, row=0)

def clicked():
    resultado = txt.get()
    lbl2.configure(text= "Bienvenido " + resultado)


window.mainloop()
