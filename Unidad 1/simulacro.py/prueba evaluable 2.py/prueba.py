import random
alumno =""
print("======================")
print("SOMBRERO SELECCIONADOR")
print("======================")
print("1. Seleccionar casa para un alumno.")
print("2. Mostrar estadísticas.")
print("Elige una opción. Si quieres salir del programa, escribe la opción 1 y el nombre del personaje innombrable.")
opcion= int(input("Selecciona un número del menú: "))
while opcion != 1 and opcion != 2:
        opcion= int(input("Selecciona un número del menú: "))
while not(opcion == 1 and alumno == "Voldermort") :
    if opcion ==1:
        alumno= input("Nombre del alumno: ")
        casa = random.randint(1, 4)
        if casa == 1:
            print("El sobrero dice que", alumno, "pertenece a Gryffindor")
        elif casa == 2:
            print("El sobrero dice que", alumno, "pertenece a Slytherin ")
        elif casa == 3:
            print("El sobrero dice que", alumno, "pertenece a Hufflepuff")
        else:
            print("El sobrero dice que", alumno, "pertenece a Ravenclaw")
    else:   
        print("Estadisticas")
        alumno=""
    print("======================")
    print("SOMBRERO SELECCIONADOR")
    print("======================")
    print("1. Seleccionar casa para un alumno.")
    print("2. Mostrar estadísticas.")
    print("Elige una opción. Si quieres salir del programa, escribe la opción 1 y el nombre del personaje innombrable.")
    if alumno != "Voldermort":
        opcion= int(input("Selecciona un número del menú: "))
        while opcion != 1 and opcion != 2:
            opcion= int(input("Selecciona un número del menú: "))
        
print("Apparition")