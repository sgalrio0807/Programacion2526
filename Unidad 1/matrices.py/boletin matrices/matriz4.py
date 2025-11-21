matriz = [[8,1,6],[3,5,7],[4,9,2]]
numfila = int(input("Indica el numero de fila que quieres sumar: "))

def sumaFila(matriz, numfila):
    suma = 0
    fila = matriz[numfila]
    for i in fila:
        suma = i + suma
    return suma

sumas = sumaFila(matriz,numfila)
print(sumas)
