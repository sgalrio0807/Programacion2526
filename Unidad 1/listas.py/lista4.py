lista= []
for i in range (0, 4):
    num=int (input("Introduce un número: "))
    lista.append(num)
print(lista)

listainversa= []
for elemento in range(len(lista), 0, -1):
    listainversa.append(elemento)
print(listainversa) 