print("Listado de habitaciones de la Casa Rural:\n")
print("1 - Habitación Azul (2 camas, planta 1)")
print("2 - Habitación Roja (1 cama, planta 1)")
print("3 - Habitación Verde (3 camas, planta 2)")
print("4 - Habitación Rosa (2 camas, planta 2)")
print("5 - Habitación Gris (1 cama, planta 3)")

numHabitacion = int(input("\nDime el número de habitación: "))

match numHabitacion:
    case 1:
        print("La habitación Azul está en la planta 1 y tiene 2 camas.")
    case 2:
        print("La habitación Roja está en la planta 1 y tiene 1 cama.")
    case 3:
        print("La habitación Verde está en la planta 2 y tiene 3 camas.")
    case 4:
        print("La habitación Rosa está en la planta 2 y tiene 2 camas.")
    case 5:
        print("La habitación Gris está en la planta 3 y tiene 1 cama.")
    case _:
        print("Esa habitación no existe.")