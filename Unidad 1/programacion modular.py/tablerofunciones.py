#pintamenu

import random
listatablero = []
#generatablero
def generatablero():
    numelementos = 0
    cuentaminas = 0
    while numelementos <= 7:
        elemento = (random.randint(0,1))
        if elemento == 0:
            listatablero.append(" ")
        elif elemento == 1:
            cuentaminas += 1
            listatablero.append("x")
        numelementos += 1

    print("Generando tablero...")
    print("Tablero generado, se han escondido", cuentaminas, "minas. Tablero:", listatablero)
    return listatablero, cuentaminas

#juegajuego
def juegajuego(listatablero, cuentaminas):
    print("jugando")
    puntuacionpositiva = 0
    puntuacionnegativa = 0
    intentos = int(input("Introduce numero de intentos: "))
    print("Tienes que encontar las x en", intentos,"intentos.")
    posicionlista = int(input("Dime una posicion del tablero(1-8): "))
    while posicionlista < 9:
        for posicionlista in listatablero:
            if posicionlista == " ":
                puntuacionnegativa -= 1
                print("-1 punto")
            elif posicionlista == "x":
                puntuacionpositiva += 1
                print("+1 punto")
    while "x" not in listatablero:
        print("Juego terminado")
    return juegajuego

#saliendojuego
def saliendojuego():
    print("saliendo")


resultado = generatablero()
juegajuego(resultado[0], resultado[1])