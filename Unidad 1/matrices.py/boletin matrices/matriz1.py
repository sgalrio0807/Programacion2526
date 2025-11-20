matriz = [[8,1,6],[3,5,7],[4,9,2]]
numfila = input("Dime el numero de fila: ")
numcolumna = input("Dime el numero de la possición de elementos: ")

def dameelemento(matriz):
    posicion= matriz[numfila[numcolumna]]
    return posicion

def damefila(matriz):
    fila = matriz[numfila]
    return fila

def damecolumna(matriz):
    columna = matriz[numfila[numcolumna]]
    if columna == "0":
        
