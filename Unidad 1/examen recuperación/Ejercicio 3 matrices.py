matriz = [[8,1,6],[3,5,7],[4,9,2]]

def numerospares(matriz):
    listanumeros = []
    for fila in matriz:
        for elemento in fila:
            if elemento %2 == 0:
                listanumeros.append(elemento)
    return listanumeros

listadenumerospares = numerospares(matriz)
print (listadenumerospares)