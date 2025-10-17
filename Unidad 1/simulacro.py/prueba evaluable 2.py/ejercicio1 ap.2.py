print("======================")
print("SOMBRERO SELECCIONADOR")
print("======================")
print("1. Seleccionar casa para un alumno.")
print("2. Mostrar estadísticas.")
print("Elige una opción. Si quieres salir del programa, escribe la opción 1 y el nombre del personaje innombrable.")

usuario= int(input("Selecciona un número del menú: "))
while usuario != 1 and usuario != 2:
    usuario= int(input("Número inválido, selecciona otro número del menú: "))

import random
random.randint(1, 4)
while usuario != 2:
        
    alumno= input("Dime tu nombre: ")
    if random.randint == 1:
        print("El sobrero dice que", alumno, "pertenece a Gryffindor")
    elif random.randint == 2:
        print("El sobrero dice que", alumno, "pertenece a Slytherin ")
    elif random.randint == 3:
        print("El sobrero dice que", alumno, "pertenece a Hufflepuff")
    elif random.randint == 4:
        print("El sobrero dice que", alumno, "pertenece a Ravenclaw")
        
print("Ejecutando y mostrar estadísticas.")

