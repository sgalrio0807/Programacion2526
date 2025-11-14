numnumeros = int(input("Dame el numero de numeros que quieres introducir: "))

def obtengolista(numnumeros):
    lista = []
    for i in range(0, numnumeros):
        num = int(input("introduce numero: "))
        lista.append(num)
    return lista

def calculalistaordeninverso(lista):
    invertida = []
    for elemento in range(len(lista),0,-1):
        invertida.append(elemento)
    return invertida

listainicial = obtengolista(numnumeros)
listainversa = calculalistaordeninverso(listainicial)
print(listainicial)
print(listainversa)