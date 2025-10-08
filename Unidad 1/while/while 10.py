import random
num1= random.randint(0, 10)
num2= random.randint(0, 10)
suma_correcta= num1 + num2
humano= int(input("Dime la suma de los dos numeros: "))
while humano != suma_correcta:
    print("Respuesta fallida, intentalo otra vez, dime la suma: ")
print("Correcto")

