filas = 4
columnas = 5
matriz = []

for i in range(filas):  
    fila = []
    for columna in range(columnas): 
        fila.append(i + columna)
    matriz.append(fila)

print(matriz)


