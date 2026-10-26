#busqueda de alumno en el registro

alumnos = ("Sergio", "Dani", "Ivan", "Isra","Ibra","Luismi")

nombre = input("Introduce el nombre del alumno: ")

for alumno in alumnos: 

    if alumno == nombre:
        print(f"El alumno {nombre} está matriculado")
        break

else:
    print(f"El alumno {alumnos} no está matriculado")
