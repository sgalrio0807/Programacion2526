print("Dame el primer numero")
num1 = int (input())  

print("Dame el segundo numero")
num2 = int (input()) 
if num1 and num2 >0:
    print("Los dos numeros son positivos")
elif num1 <0 and num2 >0 or num1 >0 and num2 <0:
    print("Alguno de los dos numeros es negativo")
elif num1 and num2 <0:
    print("Los dos numeros son negativos")
