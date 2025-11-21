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
    lista = []
    for i in range(0,len(matriz)):
        columnacompleta = matriz[i][numcolumna]
        lista.append(columnacompleta)
    return lista
        
elemento = dameelemento(matriz)
print(elemento)

filacompleta = damefila(matriz)
print(filacompleta)

columnacompleta = damecolumna(matriz)
print(columnacompleta)
