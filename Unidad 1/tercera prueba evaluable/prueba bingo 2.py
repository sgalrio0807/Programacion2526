carton_bingo = [

    [5,  21, 38,   50, 63],

    [12, 17, 44,   47, 74],

    [1,  29, "--", 55, 69],

    [9,  25, 32,   59, 61],

    [14, 19, 41,   52, 66]
]

import random
listaaleatorios = [] 
def generaAleatorio(listaaleatorios):
    aletorio = random.randint(0, 75)
    while aletorio not in listaaleatorios:
        listaaleatorios.append(aletorio)
    return listaaleatorios

def buscaNumeroEnLista(fila, numero):
    i = 0
    encontrado = False
    posicion = -1
    while i < len(fila) and not encontrado:
        if fila[i] == numero:
            encontrado = True
            posicion = i
        else:
            i += 1
    return posicion

def compruebaSiHayLineaEnFila(listaaleatorios, fila ):
    estaEnLista = True
    while fila not in listaaleatorios:
        estaEnLista = False
    return estaEnLista

def jugarALaLinea(carton_bingo, estaEnLista):
    if estaEnLista == True:
        for i in carton_bingo:
            estaEnLista == True
        estaEnLista == False

def imprimeResultados():
    print("Se ha conseguido LÍNEA en el cartón")
    print("Numeros que han salido antes de completar la fila", posicion ,)
    print("Fila acertante: la numero", fila ,)
    print("Lista de numeros que han salido:", listaaleatorios)

