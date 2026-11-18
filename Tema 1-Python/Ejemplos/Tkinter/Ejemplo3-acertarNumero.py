from tkinter import *
window = Tk()
window.title("Adivina el número")
window.geometry('500x300')


lblTitle = Label(window, text="Juego de adivinar ", font=("Arial",18))
lblTitle.grid(column=0, row=0)

lblNumbrer = Label(window, text="Introduce un número ", font=("Arial,14"))
lblNumbrer.grid(column=0, row=1)

lblResult = Label(window, text="", font=("Arial,18"))
lblResult.grid(column=1, row=2)

txtNumbre = Entry(window, width=10)
txtNumbre.grid(column=1, row=1)

def clicked():

    print("Hola")




btn = Button(window, text="Resultado", command=clicked)
btn.grid(column=2, row=1)


window.mainloop()