matriz = [[8,1,6],[3,5,7],[4,9,2]]

def devuelveDiagonalPrincipal(matriz):
    diagonalprincipal = []
    for i in range(len(matriz)):
        diagonalprincipal.append(matriz[i][i])
    return diagonalprincipal

def devuelveDiagonalSecundaria(matriz):
    diagonalsecundaria = []
    for i in range(len(matriz)):
        diagonalsecundaria.append(matriz[i][-1 - i])
    return diagonalsecundaria

def compruebasiescuadrada(matriz):
    numfilas = len(matriz)
    numcolumnas = len(matriz[0])
    return numfilas == numcolumnas

diagprincipal = devuelveDiagonalPrincipal(matriz)
diagsecundaria = devuelveDiagonalSecundaria(matriz)
cuadrada = compruebasiescuadrada(matriz)

print (diagprincipal)
print(diagsecundaria)
print(cuadrada)