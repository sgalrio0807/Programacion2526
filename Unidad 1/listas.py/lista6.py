num1= int(input("Dime el pimer número: "))
num2= int(input("Dime el segindo número: "))
num3= int(input("Dime el tercer número: "))
num4= int(input("Dime el cuarto número: "))
num5= int(input("Dime el quinto número: "))
num6= int(input("Dime el sexto número: "))
num7= int(input("Dime el séptimo número: "))
num8= int(input("Dime el octavo número: "))
num9= int(input("Dime el noveno número: "))
num10= int(input("Dime el décimo número: "))

numeros= [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
maximo= numeros [0]
minimo= numeros [0]
numeros.sort()  # Para ordenar de menor a mayor

for i in numeros:
    if i > maximo:
        print(i, "maximo")
    elif i < minimo:
        print(i, "minimo")
    else:
        print(i)
       


