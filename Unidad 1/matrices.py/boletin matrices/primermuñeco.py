def generaLista():
    listanotas= []
    jilgueros = int(input("Dime una secuencia de notas: "))
    while jilgueros > 0:
        listanotas.append(jilgueros)
        jilgueros = int(input("Dime una secuencia de notas: "))
    return listanotas

def esValida(listanotas, notamaxima, notaminimo):
    listasinduplicados = []
    i = 0
    while i < len(listanotas):
        if listanotas[i] not in listasinduplicados:
            listasinduplicados.append(listanotas[i])
        i = i + 1

    if notamaxima == (listasinduplicados[0]) or (listasinduplicados[-1]) and notaminimo == (listasinduplicados[0]) or notaminimo == (listasinduplicados[-1]):
        esVerda = True     
    else:
        esVerda = False
    return listasinduplicados, esVerda

def calcularMinMax(listasinduplicados):
    notamaxima = max(listasinduplicados)
    notaminima = min(listasinduplicados)
    return notamaxima,notaminima

def calculapuntos(listasinduplicados, esVerda):
    puntos= len(listasinduplicados)
    return puntos

listanotas = generaLista()
if esValida(listanotas,notamaxima, notaminimo):
    puntos = calculapuntos(listanotas)
    print("Seuencia válida, Nº de puntos: ", puntos)
else:
    print("Secuencia de notas NO válida")





