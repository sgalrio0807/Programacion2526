matriz = [[8,1,6],[3,5,7],[4,9,2]]
numfila = int(input("Dime el número de fila: "))
numcolumna = int(input("Dime el número de columna: "))

def damefilaycolumna(matriz, numfila, numcolumna):
    numeroexacto = matriz[numfila][numcolumna]
    return numeroexacto

def devuelvefila(matriz, numfila):
    numerofila = matriz[numfila]
    return numerofila

def devuelvecolumna(matriz, numcolumna):
    columna = []
    for fila in matriz:
        columna.append(fila[numcolumna])
    return columna

numeroconcreto = damefilaycolumna(matriz, numfila, numcolumna)
numerodefila = devuelvefila(matriz, numfila)
numerodecolumna = devuelvecolumna(matriz, numcolumna)

print (numeroconcreto)
print (numerodefila)
print (numerodecolumna)