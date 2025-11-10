jug1 = input("Jugador 1: Pares o nones?: ")
jug2 = input("Jugador 2: Pares o nones?: ")
dedos1 = int(input("Jugador 1: Cuántos dedos sacas?: "))
dedos2 = int(input("Jugador 2: Cuántos dedos sacas?: "))

while jug1 == jug2:
    jug1 = input("Jugador 1: Pares o nones?: ")
    jug2 = input("Jugador 2: Pares o nones?: ")

total = dedos1 + dedos2
if total % 2 == 0 and jug1 == "pares":
    print("Jugador 1 gana")
elif total % 2 != 0 and jug1 == "nones":
    print("Jugador 1 gana")
else:
    print("Jugador 2 gana")

