matriz = [[8,1,6],[3,5,7],[4,9,2]]

def maximofila(matriz, fila):
    return max(matriz[fila])

def maximocolumna(matriz, columna):
    valores = []
    for fila in matriz:
        valores.append(fila[columna])
    return max(valores)

def maximototal(matriz):
    maximos_filas = []
    for i in range(len(matriz)):
        maximos_filas.append(maximofila(matriz, i))
    return max(maximos_filas)

maxfila0 = maximofila(matriz, 0)
maxfila1 = maximofila(matriz, 1)
maxfila2 = maximofila(matriz, 2)

maxcolumna0 = maximocolumna(matriz, 0)
maxcolumna1 = maximocolumna(matriz, 1)
maxcolumna2 = maximocolumna(matriz, 2)

maxtotal = maximototal(matriz)

print(maxfila0,maxfila1,maxfila2)
print(maxcolumna0,maxcolumna1,maxcolumna2)
print(maxtotal)