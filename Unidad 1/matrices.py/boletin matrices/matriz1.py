matriz = [[8,1,6],[3,5,7],[4,9,2]]
numfila = int(input("Dime el numero de fila: "))
numcolumna = int(input("Dime el numero de la columna: "))

def dameelemento(matriz):
    posicion= matriz[numfila][numcolumna]
    return posicion

def damefila(matriz):
    fila = matriz[numfila]
    return fila

def damecolumna(matriz):
    columna = [matriz[0][numcolumna], matriz[1][numcolumna], matriz[2][numcolumna]]
    return columna

elemento = dameelemento(matriz)
print(elemento)

filacompleta = damefila(matriz)
print(filacompleta)

columnacompleta = damecolumna(matriz)
print(columnacompleta)
