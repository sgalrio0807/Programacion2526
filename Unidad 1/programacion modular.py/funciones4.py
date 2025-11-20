numerosadecir= int(input("Cuantos números quieres introducir: "))
lista=[]
for i in range(numerosadecir):
    num= int(input("Introduce número: "))
    lista.append(num)

def estaOrdenadaAscendentemente(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

orden= estaOrdenadaAscendentemente(lista)
print(orden)
