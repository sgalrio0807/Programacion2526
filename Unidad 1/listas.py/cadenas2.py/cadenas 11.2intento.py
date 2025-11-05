numero = input("Dime un número entero: ")

contador = 0
salida = ""
for i in range(len(numero)-3, -1, -3):
    contador =+ 3
    salida = "." + numero[i: i +3] + salida
    principio = numero[0 : len(numero)-contador]
    salida = principio + salida
    
print(salida)