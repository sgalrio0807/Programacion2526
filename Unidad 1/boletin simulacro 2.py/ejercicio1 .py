
num1 = int(input("Dame el primer número: "))
num2 = int(input("Dame el segundo número: "))

def validoNumero(num1, num2):
    lista = []
    lista.append(num1)
    for digitos in lista:
        while digitos <= num2:
            num1 = int(input("Dame el primer número: "))
            num2 = int(input("Dame el segundo número: "))
    return num1,num2

def sumadigitos(num1, num2):
    suma = 0
    contador = 0
    digitosnum2 = []
    digitosnum1 = []
    digitosnum2.append(num2)  
    digitosnum1.append(num1)
    for digitos in digitosnum2:
        suma += 1
    while contador <= suma:
        contador += 1
        for i in digitosnum1:
            sumatotal = i + i
    return sumatotal

validados = validoNumero(num1, num2)
print(validados)
sumadedigitos = sumadigitos(num1, num2)
print(sumadedigitos)