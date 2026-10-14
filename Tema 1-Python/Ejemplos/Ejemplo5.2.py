num1 = int(input("Ingrese un número: ")) 
num2 = int(input("Ingrese otro número: "))
op = input("Ingrese el operador (+, -, *, /): ")

if op == "+":
    print(f"El resultado de {num1} + {num2} es: {num1 + num2}")
elif op == "-":
    print(f"El resultado de {num1} - {num2} es: {num1 - num2}")
elif op == "*":
    print(f"El resultado de {num1} * {num2} es: {num1 * num2}")
else:
    print(f"El resultado de {num1} / {num2} es: {num1 / num2}")
    

