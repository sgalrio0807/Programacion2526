numero = input("Dime un número: ")
inicio = int(input("Posición inicial: "))
fin = int(input("Posición final: "))

if inicio < 0 or fin > len(numero) or inicio >= fin:
    print("Rango no válido")
else:
    print(numero[inicio:fin])
