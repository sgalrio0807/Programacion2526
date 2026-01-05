matriz = [[8,1,6],[3,5,7],[4,9,2]]
fila = int(input("Dime un numero de fila: "))
columna = int(input("Dime un numero de columna: "))

def maximofila(matriz, fila):
    return max(matriz[fila])

def maximocolumna(matriz, columna):
    lista = []
    for fila in matriz:
        lista.append(fila[columna])
        nummaxcolumna = max(lista)
    return nummaxcolumna

def maximototal(matriz):
    lista = []
    for i in range(len(matriz)):
        lista.append(maximofila(matriz, i))
        nummaxtotal = max(lista)
    return nummaxtotal

numfila = maximofila(matriz, fila)
numcolumna = maximocolumna(matriz, columna)
nummax = maximototal(matriz)

print(numfila)
print(numcolumna)
print(nummax)


