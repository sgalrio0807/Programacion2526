matriz = [[22, 20, 19, 21],[18, 25, 23, 22],[19, 21, 20, 24],[17, 23, 22, 19],[24, 23, 27, 26]]

def calcularmedia(listaNumeros):
    media = 0
    for i in listaNumeros:
        media = media + i
    media = media / len(listaNumeros)
    return media

def calculamediafila(matriz):
    listaMedias = []
    for fila in matriz:
        media_fila = calcularmedia(fila)
        listaMedias.append(media_fila)
    return listaMedias

def calculaMediaColumna0(matriz):
    columna0 = []
    media = 0
    for i in range(0,len(matriz)):
        media = media + i
        media = media / len(matriz)
    return media

lista_numeros = matriz[0]
mediamatriz = calcularmedia(lista_numeros)
print(mediamatriz)

listaMedias = calculamediafila(matriz)
print(listaMedias)

mediacolumna0 = calculaMediaColumna0(matriz)
print(mediacolumna0)
