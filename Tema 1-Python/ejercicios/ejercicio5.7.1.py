usuario = "root"
contrasenia = "toor"

intentos = 3

while (intentos > 0):
    usuario_ingresado = input("Introduce el nombre de usuario: ")
    contrasenia_ingresada = input("Introduce la contraseña: ")
    intentos = intentos-1

    if usuario_ingresado == usuario and contrasenia_ingresada == contrasenia:
        print("¡¡¡Bienvenido!!!")
        break
    else:
        print("Acceso fallido")
        print(f"Te quedan {intentos} intentos")
if intentos < 1:
    print("Ya no te quedan mas intentos lleve el dispositivo a un técnico")



