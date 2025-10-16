num1= int(input("Dime el primer numero de un grupo de tres numeros: "))
num2= int(input("Dime el segundo numero de un grupo de tres numeros: "))
num3= int(input("Dime el tercer numero de un grupo de tres numeros: "))
while num1 == "0" and num2 == "0" and num3 == "0":
    print("Fin del programa")

if num1<num2 and num3:
    print(num1, num2, num3, "es un numero creciente.")
elif (num1>num2 and num2<num3) and (num1<num2 and num2>num3):
    print(num1, num2, num3, "es un numero desordenado.")
elif num1>num2 and num3:
    print(num1, num2, num3, "es un numero decreciente.")