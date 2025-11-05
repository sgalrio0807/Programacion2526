cadena= input("Dame un número de mínimo 4 caracteres: ")
num= int(cadena)

while len(cadena)<4:
    cadena= input("Dame un número de mínimo 4 caracteres: ")

if num % 2 == 0:
    salida = cadena[2] + cadena [4]
    print (salida)

elif num % 3 == 0:
    salida = cadena[1] + cadena [2]
    print (salida)

elif num % 7 == 0:
    salida = cadena[0] + cadena [3]
    print (salida)

else:
    print("Este número no es válido")