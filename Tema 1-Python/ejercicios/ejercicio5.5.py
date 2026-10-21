# Adivina el número
import random

num_adivinar = random.randint(1, 100)
Intentos = 5

print("Bienvenido al juego de adivinar el número del 1 al 100")

while (Intentos > 0):

    val = int(input("Introduce un valor del 1 al 100: "))
    Intentos -= 1

    if num_adivinar == val:

        print(f"Has adivinado el número {num_adivinar}")
        break
    elif num_adivinar < val:
        print("El número introducido es mayor")

    else:
        print("El número introducido es menor")

    print(f"No has adivinado el número, tienes {Intentos} intentos")

print("No has adivinado el número")

