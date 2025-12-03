matriz = [[8,1,6],[3,5,7],[4,9,2]]
num = 6
encontrado = False
posicion = 0
while (posicion < len(matriz)) and not encontrado:
    if matriz[posicion] == num:
        encontrado = True
    else: 
        posicion = posicion + 1
print(posicion)