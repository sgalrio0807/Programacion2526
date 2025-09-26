print("Dame el primer numero")
num1 = int (input())  

print("Dame el segundo numero")
num2 = int (input()) 

print("Dame el tercer numero")
num3 = int (input())

if num1 > num2 and num1 > num3:
    print("El numero mayor es:", num1)

elif num2 > num1 and num2 > num3:
    print("El numero mayor es:", num2)

elif num3 > num1 and num3 > num2:
    print("El numero mayor es:", num3)