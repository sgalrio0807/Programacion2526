def pintamenu():
    print("=============================")
    print("  SOMBRERO SELECCIONADOR")
    print("=============================")
    print("1. Seleccionar casa para un alumno")
    print("2. Mostrar estadísticas")
    print("Elige una opción. Si quieres salir del programa, escribe la opción 1 y el nombre del personaje innombrable")

def eligeopcion():
    opcion = input("Introduce una opción del menú: ")
    while opcion != "1" and opcion != "2":
        opcion = input("Opción incorrecta, introduce una opción del menú: ")
    
    if opcion == "1":
        print("Ejecutando y seleccionando casa")
    else:
        print("Ejecutando y mostrar estadísticas")
    return opcion

menu = pintamenu()
print(menu)

opcion = eligeopcion()
print(opcion)