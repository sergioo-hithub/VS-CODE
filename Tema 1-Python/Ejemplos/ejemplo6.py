# Sentencia For

alumnos = ["a","b","c","d"]

for alumno in alumnos:
    print(alumno)

# Tambien se puede hacer un registro de numeros:

numeros = [4,8,2,7,1,9,3,5]
total = 0

for n in numeros:
    total += n 
    if total > 10:
        break

# La función range()

for i in range(3):
    print(i)

