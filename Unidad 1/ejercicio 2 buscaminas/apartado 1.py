print("Pulse T para generar un nuevo tablero")
print("Pulse J para jugar")
print("Pulse E para salir del juego")
opcion= input("Elige una opción: ").lower()

while opcion != "t" and opcion != "j" and opcion != "e":
    print("Incorrecto")
    print("Pulse T para generar un nuevo tablero")
    print("Pulse J para jugar")
    print("Pulse E para salir del juego")
    opcion= input("Elige una opción: ").lower()

if opcion == "t":
    print("Generando tablero")
elif opcion == "j":
    print("Jugando")
elif opcion == "e":
    print("saliendo")