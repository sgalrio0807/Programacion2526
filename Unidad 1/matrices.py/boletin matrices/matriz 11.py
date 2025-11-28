matriz = [[8,1,6],[3,5,7],[4,9,2]]

def devuelveDiagonal1(matriz):
    diagonalprincipal = []
    for i in range(len(matriz)):
        diagonalprincipal.append(matriz[i][i])
    return diagonalprincipal

def devuelveDiagonal2(matriz):
    diagonalsecundaria = []
    for i in range(len(matriz)):
        diagonalsecundaria.append(matriz[i][-1 - i])
    return diagonalsecundaria

def devuelvesumaelementos(matriz, esprincipal):
    if esprincipal == True:
        diagonal = devuelveDiagonal1(matriz) 
    else:
        diagonal = devuelveDiagonal2(matriz)

    suma = 0
    for numero in diagonal:
        suma += numero
    return suma

sumaelementos = devuelvesumaelementos(matriz, True)
print (sumaelementos)

sumaelementos = devuelvesumaelementos(matriz, False)
print (sumaelementos)