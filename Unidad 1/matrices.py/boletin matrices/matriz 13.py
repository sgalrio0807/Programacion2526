matriz = [[8,1,6],[3,5,7],[4,9,2]]

def sumaFila(matriz, numfila):
    suma = 0
    for i in matriz[numfila]:
        suma += i
    return suma

def sumaColumna(matriz, numcolumna):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][numcolumna]
    return suma

