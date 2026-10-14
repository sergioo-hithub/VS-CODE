num1 = int(input("Ingrese un número: "))
num2 = int(input("Introduce un número: "))
operador = input("Elija el símbolo de la operación: ")

res = int(eval(f"{num1} {operador} {num2}"))

print(f"El resultado de la operación es: {res}")


