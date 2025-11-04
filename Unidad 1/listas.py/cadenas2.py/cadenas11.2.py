numero = input("Dime un número entero: ")
contador = 0
resultado = ""

for i in numero[::-1]:
    if contador == 3:
        resultado = "." + resultado
        contador = 0
    resultado = i + resultado
    contador += 1

print(resultado)
