matriz = [[8,1,6],[3,5,7],[4,9,2]]

def sumacolumna(matriz):
    columna = int(input("Dime que columna quieres sumar: "))
    suma = 0
    for fila in matriz:
        suma += fila[columna]
    return suma

resultado = sumacolumna(matriz)
print(resultado) 

