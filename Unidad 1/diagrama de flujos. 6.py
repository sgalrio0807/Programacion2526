print("Dame el primer numero")
num1 = int (input())  #int son nunmeros emteros y float decimales

print("Dame el segundo numero")
num2 = int (input()) 

if num2 != 0:  #!= significa "distinto de"
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
else:
    print("Error: No se puede dividir entre cero")