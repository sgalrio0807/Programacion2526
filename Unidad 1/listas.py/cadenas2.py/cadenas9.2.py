frase = input("Dime una frase: ")
caracter1 = input("Dime un caracter ")
caracter2 = input("Dime otro caracter ")

salida = ''
if caracter1 in frase:
    salida = frase.replace(caracter1, caracter2)

print(salida)