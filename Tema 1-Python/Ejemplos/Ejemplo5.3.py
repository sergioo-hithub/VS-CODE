#Adivina el valor 

import random

num_adivinar = random.randint(1, 10)

val = int(input("Introduce un valor del 1 al 10 tienes 3 intentos: "))

if val == num_adivinar:
    print("Has adivinado !!!!")
else:
    print(f"NO has adivinado te quedan 2 intentos!!!")
    val = int(input("Vuelve a intentarlo: "))
              
    if val == num_adivinar:
        print("Has adivinado !!!!")
    else:
        print(f"No has adivinado te queda 1 intento!!")
        val = int(input("Que lástima intentalo otra vez: "))
    if val == num_adivinar:
        print("Has adivinado !!!!")
    else:
        print(f"Se te accedido a mas intentos no te preocupes: ")
    if val == num_adivinar:
        print("Felicidades has acertado menos mal esto iba para largo")
    elif val < num_adivinar:
        print(f"El numero es mayor intentalo de nuevo")
        val = int(input("Que lástima intentalo otra vez: "))

    if val == num_adivinar:
        print("Ya esta se acabó bien dicho!!!")
    elif val > num_adivinar:
        print(f"No has adivinado otra pista el numero es menor:")
        val = int(input("Que lástima intentalo otra vez: "))

    if val == num_adivinar:
        print("VAMOOOOOOO ESO ES!!!!")
    else:
        print("Se acabó el juego no hay mas intentos")

