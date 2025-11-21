matriz = [[8,1,6],[3,5,7],[4,9,2]]
def numerosPares(matriz):
    listapares = []
    for i in range(len(matriz)):
        fila = matriz[i]
        for a in fila:
            if a %2 == 0:
                listapares.append(a)
    return listapares

numerospares = numerosPares(matriz)
print(numerospares)
