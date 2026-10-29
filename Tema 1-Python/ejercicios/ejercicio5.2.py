# Contador con el while

print("Programa que devuelve los números comprendidos entre dos valores. ")

var1 = int(input("Introduce el primer número: "))
var2 = int(input("Introduce el segundo número: "))

contador = var1 +1 
# añadiendo este +1 hace que el valor empiece por el siguiente numero que tu le indiques por ejemplo eliges 4 pues empieza por el 5.

while (contador < var2):
# Quitando el = arriba hace que el ultimo numero no lo diga
    print(f"Valor: {contador}")

    contador += 1

# Contador con el "for in range"

print("Programa que devuelve los números comprendidos entre dos valores. ")

var1 = int(input("Introduce el primer número: "))
var2 = int(input("Introduce el segundo número: "))

var2 += 1

for i in range(var1,var2):
   
    print(f"Valor: {i}")

# Lo mismo con sumatorio

print("Programa que devuelve los números comprendidos entre dos valores. ")

var1 = int(input("Introduce el primer número: "))
var2 = int(input("Introduce el segundo número: "))

suma = 0
var2 += 1

for i in range(var1,var2):

    suma += i
    print(f"Valor: {i}")


else:
    print(f"El sumatorio es: {suma}")

