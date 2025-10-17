print("======================")
print("SOMBRERO SELECCIONADOR")
print("======================")
print("1. Seleccionar casa para un alumno.")
print("2. Mostrar estadísticas.")
print("Elige una opción. Si quieres salir del programa, escribe la opción 1 y el nombre del personaje innombrable.")

usuario= int(input("Selecciona un número del menú: "))
while usuario != 1 and usuario != 2:
    usuario= int(input("Número inválido, selecciona otro número del menú: "))

if usuario == 1:
    print("Ejecutando y seleccionando casa.")
elif usuario == 2:
    print("Ejecutando y mostrar estadísticas.")