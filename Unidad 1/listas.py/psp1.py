print("Selecciona una de las siguientes opciones (R, E, S)") 
print("R. Registrar juegos")
print("E. Mostrar estadísticas")	
print("S. Salir del programa")
menu= input("Seleccione una opción de el programa: ").lower()

while menu != "r" and menu == "e" and menu == "s":
    menu= input("Seleccione una opción de el programa: ").lower()

if menu == "r":
    print("Registrando")
elif menu == "e":
    print("Estadísticas")
elif menu == "s":
    print("Salir del programa")  