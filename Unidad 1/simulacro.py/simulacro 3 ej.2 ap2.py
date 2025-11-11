jug1 = input("Jugador 1: Pares o nones?: ")
jug2 = input("Jugador 2: Pares o nones?: ")
dedos1 = int(input("Jugador 1: Cuántos dedos sacas?: "))
import random
dedos2 = random.randint(0,10)

victoriasjug1 = 0
victoriasjug2 = 0

while dedos1 != 0 and dedos2 != 0:
    while jug1 == jug2:
        jug1 = input("Jugador 1: Pares o nones?: ")
        jug2 = input("Jugador 2: Pares o nones?: ")

    total = dedos1 + dedos2
    if total % 2 == 0 and jug1 == "pares":
        victoriasjug1 += 1
        print("Jugador 2 ha sacado",dedos2)
        print("Jugador 1 gana")
    elif total % 2 != 0 and jug1 == "nones":
        victoriasjug1 += 1
        print("Jugador 2 ha sacado",dedos2)
        print("Jugador 1 gana")
    else:
        victoriasjug2 += 1
        print("Jugador 2 ha sacado",dedos2)
        print("Jugador 2 gana")
    
    jug1 = input("Jugador 1: Pares o nones?: ")
    jug2 = input("Jugador 2: Pares o nones?: ")
    dedos1 = int(input("Jugador 1: Cuántos dedos sacas?: "))
    dedos2 = random.randint(0,10)

print("El jugador 1 ha ganado",victoriasjug1,"partidas y el jugador 2 ha ganado",victoriasjug2,"partidas.")