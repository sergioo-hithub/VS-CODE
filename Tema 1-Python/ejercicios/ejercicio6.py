# Cálculo Mental Contrarreloj

import random
import time

aciertos = 0
tiempo_incio = time.time()


for ronda in range (5):

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    resultado_correcto = num1 *num2

    print(f"Ronda {ronda +1} Multiplica {num1} * {num2}")

    resultado_usuario = int(input("Introduce resultado: "))

    if resultado_correcto == resultado_usuario:
        print("Correcto!!!")
        aciertos += 1
    else:
        print("Incorrecto!!!")

else:
    tiempo_final = time.time()

tiempo_total = tiempo_final - tiempo_incio

print(f"Tu puntuacion es: {aciertos} con un tiempo de {tiempo_total} segundos")


 