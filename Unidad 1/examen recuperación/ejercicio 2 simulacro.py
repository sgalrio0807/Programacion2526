num1 = int(input("Introduce un número: "))
lista = []
contador = 0
suma = 0
esdecreciente = True
escreciente = True

while num1 != 0:
    contador +=1
    lista.append(num1)
    num1 = int(input("Introduce un número: "))

print("fin")
for i in range(len(lista)-1):
    if lista[i] >= lista[i+1]:
        escreciente = False
    elif lista[i] <= lista[i+1]:
        esdecreciente = False

contador += 1
print("Se han intraducido", contador, "numeros")

for i in lista:
    suma += i
media = suma / contador
print("La media es", media)

if escreciente == True:
    print("lista creciente")
elif esdecreciente == True:
    print("lista decreciente")
else:
    print("lista desordenada")