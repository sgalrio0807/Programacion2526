matriz = [[8,1,6],[3,5,7],[4,9,2]]

def calculanumpares(matriz):
    listapares = []
    for i in range(0,len(matriz)):
        fila = matriz[i]
        for e in fila:
            if e %2 == 0:
                listapares.append(e)
    return listapares

def sumafila(listapares):
    suma = 0
    for i in listapares:
        suma = i + suma
    return suma

pares = calculanumpares(matriz)
print(pares)
sumapares = sumafila(pares)
print (sumapares)