matriz = [[8,1,6],[3,5,7],[4,9,2]]

def sumavalores(matriz):
    suma = 0
    for fila in matriz:
        for elemento in fila:
            suma += elemento
    return suma

sumacompleta = sumavalores(matriz)
print (sumacompleta) 