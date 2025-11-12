print("Pulse T para generar un nuevo tablero")
print("Pulse J para jugar")
print("Pulse E para salir del juego")
opcion= input("Elige una opción: ").lower()
listatablero = []
import random
cuentaminas = 0
numelementos = 0
puntuacionpositiva = 0
puntuacionnegativa = 0

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
    tablerogenerado = input("El tablero ha sido generado?(S/N): ").lower()
    if tablerogenerado == "s":
        posicionlista = int(input("Dime una posicion del tablero(1-8): "))
        while posicionlista < 9:
            for posicionlista in listatablero[:len]:
                if posicionlista == " ":
                    puntuacionnegativa -= 1
                    print("-1 punto")
                elif posicionlista == "x":
                    puntuacionpositiva += 1
                    print("+1 punto")
        total = puntuacionpositiva - puntuacionnegativa
        print("Tu puntuacion total es", total)

elif opcion == "e":
    print("saliendo")