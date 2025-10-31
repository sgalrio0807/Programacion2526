num= input("Dame un número: ")
salida = ""
posicion= int(input("¿Que posición quieres ver?: "))

if posicion < len(num):
    print(num[posicion])
else:
    print("Posición incorrecta")
    

