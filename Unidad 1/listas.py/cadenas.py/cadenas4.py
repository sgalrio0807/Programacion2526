num= int(input("Dame un número: "))
posicion= int(input("¿Que posición quieres ver?: "))
lista= []
lista.append(num)

while num != 0:
    lista.append(1)
    num = num // 10

if lista == []:
    lista.append(1)
lista.pop(0)
print(lista)