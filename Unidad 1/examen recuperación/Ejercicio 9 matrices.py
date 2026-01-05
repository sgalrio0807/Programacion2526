matriz = [[8,1,6],[3,5,7],[4,9,2]]

def diagonalprincipal(matriz):
    listadiagonalprincipal = []
    for i  in range(len(matriz)):
        listadiagonalprincipal.append(matriz[i][i])
    return listadiagonalprincipal

def diagonalsecundaria(matriz):
    listadiagonalsecundaria = []
    for i in range(len(matriz)):
        listadiagonalsecundaria.append(matriz[i][-1 - i])
    return listadiagonalsecundaria

principal = diagonalprincipal(matriz)
secundaria = diagonalsecundaria(matriz)

print(principal)
print(secundaria)