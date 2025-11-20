numcadenas = int(input("¿Cuántas cadenas quieres introducir?: "))
def cargarcadenas(numcadenas):
    lista = []
    i = 0
    while i < numcadenas:
        cadena = input("Introduce una cadena: ")
        lista.append(cadena)
        i = i + 1
    return lista

def eliminarduplicados(lista):
    listasinduplicados = []
    i = 0
    while i < len(lista):
        if lista[i] not in listasinduplicados:
            listasinduplicados.append(lista[i])
        i = i + 1
    return listasinduplicados

lista = cargarcadenas(numcadenas)
print("Lista original:", lista)

listaeliminada = eliminarduplicados(lista)
print("Lista sin duplicados:", listaeliminada)