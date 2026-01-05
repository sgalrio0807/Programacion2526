matriz = [[8,1,6],[3,5,7],[4,9,2]]

def sumacolumna(matriz):
    columna = int(input("Dime que columna quieres sumar: "))
    suma = 0
    lista = []
    for fila in matriz:
        suma += fila[columna]
        if columna %2 == 0:
            lista.append(suma)
    return lista[2]

resultado = sumacolumna(matriz)
print(resultado) 
