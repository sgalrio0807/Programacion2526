print("Pulse T para generar un nuevo tablero")
print("Pulse J para jugar")
print("Pulse E para salir del juego")
opcion= input("Elige una opción: ").lower()
listatablero = []
import random
cuentaminas = 0
numelementos = 0

while opcion != "t" and opcion != "j" and opcion != "e":
    print("Incorrecto")
    print("Pulse T para generar un nuevo tablero")
    print("Pulse J para jugar")
    print("Pulse E para salir del juego")
    opcion= input("Elige una opción: ").lower()

if opcion == "t":
    while numelementos <= 8:
        elemento = (random.randint(0,1))
        if elemento == 0:
            listatablero.append(" ")
        elif elemento == 1:
            cuentaminas += 1
            listatablero.append("x")
        numelementos += 1

    print("Generando tablero...")
    print("Tablero generado, se han escondido", cuentaminas, "minas. Tablero:", listatablero)

elif opcion == "j":
    print("Jugando")
elif opcion == "e":
    print("saliendo")