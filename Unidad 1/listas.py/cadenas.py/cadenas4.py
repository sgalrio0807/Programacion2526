num= input("Dame un número: ")
posicion= input("¿Que dígito quieres ver?: ")

if posicion in num:
    print("La posición de la primera ocurrencia es:", num.index(posicion))
else:
    print(-1)

