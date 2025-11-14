numnumeros = int(input("Dame el numero de numeros que quieres introducir: "))

def obtengolista(numnumeros):
    lista = []
    for i in range(0, numnumeros):
        num = int(input("introduce numero: "))
        lista.append(num)
    return lista

def estaordenadaascendentemente(lista):
    orden = True
    i = 0
    while i < len(lista)-1 and orden:
        if lista[i] > lista[i+1]:
            orden = False
        i = i + 1
    return orden

def estaordenada(lista, ascendente):
    if ascendente == True:
        print("Esta ordenada ascendentemente")
    else: 
        print("No esta ordenada ascendentemente")


listainicial = obtengolista(numnumeros)

lista = [1,2,3,4]
orden = estaordenadaascendentemente(lista)
print(orden)

lista = [1,7,4,2]
ordendesc = estaordenadaascendentemente(lista)
print(ordendesc)

listaordenada = estaordenada(lista, ascendente)
print(listaordenada)