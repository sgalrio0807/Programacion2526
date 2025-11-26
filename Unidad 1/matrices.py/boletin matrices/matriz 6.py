matriz = [[8,1,6],[3,5,7],[4,9,2]]

def calculacolumna(matriz, numcolumna):
    suma = 0
    calculaMediaColumna(numcolumna,matriz)
    for i in numcolumna:
        suma += i
    return suma

def calculaMediaColumna(numColumna,matriz):
    columna0 = []
    for i in range(len(matriz)):
        columna0.append(matriz[i][numColumna])
    return columna0

calculo = calculacolumna(matriz)
print(calculo)