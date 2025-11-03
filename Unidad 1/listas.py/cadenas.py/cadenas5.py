num= input("Dame un número entero: ")
posicion= int(input("¿De que número quieres ver su posición?: "))

if posicion < len(num):
    print(num[posicion])
else:
    print("Posición incorrecta")
