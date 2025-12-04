def tirar_dado():
    from random import randint
    return randint(1,6)

def menu():
    print("Selecciona 1 para jugar")
    print("Selecciona 2 para mostrar historial")
    print("Selecciona 3 para finalizar y mostrar resumen")
    opcion = input("Selecciona opción: ")
    return opcion

from random import randint

def tirar_dado():
    return randint(1,6)

def menu():
    print("1. Apostar")
    print("2. Mostrar historial")
    print("3. Retirarse")
    opcion = input("Selecciona opción: ")
    return opcion

def jugar():
    historial = []
    saldo = 0
    jugada = 0
    opcion = ""

    while opcion != "3":
        opcion = menu()
        if opcion == "1":
            jugada += 1
            numero = int(input("Número apostado (2-12): "))
            cantidad = int(input("Cantidad apostada: "))
            dado1 = tirar_dado()
            dado2 = tirar_dado()
            suma = dado1 + dado2
            if suma == numero:
                ganancia = cantidad * 2
                saldo += ganancia
                historial.append(("En la", jugada, "º jugada apostó al valor", numero, "y sumó", suma, "ganando", ganancia, "€"))
            else:
                saldo -= cantidad
                historial.append(("En la", jugada, "º jugada apostó al valor", numero, "y sumó", suma, "perdiendo", cantidad, "€"))
        elif opcion == "2":
            for h in historial:
                print(h)

    print("Resumen final:")
    for h in historial:
        print(h)
    print("Saldo total neto:", saldo, "€")

juego = jugar()
print(juego)




