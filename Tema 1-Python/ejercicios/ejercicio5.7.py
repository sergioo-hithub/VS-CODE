usuario = "root"
contrasenia = "toor"

usuario_ingresado = input("Introduce el nombre de usuario: ")
contrasenia_ingresada = input("Introduce la contraseña: ")


if usuario_ingresado == usuario and contrasenia_ingresada == contrasenia:
    print("¡¡¡Bienvenido!!!")
else:
    print("Acceso fallido")

