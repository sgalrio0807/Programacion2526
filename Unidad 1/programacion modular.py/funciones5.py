numerosadecir= int(input("Cuantos números quieres introducir: "))
lista=[]
for i in range(numerosadecir):
    num= int(input("Introduce número: "))
    lista.append(num)

def estaOrdenada(lista, ascendente):
    if ascendente:
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                return False
        return True
    
    else:
        for i in range(len(lista) - 1):
            if lista[i] < lista[i + 1]:
                return False
        return True

respuesta = input("¿Quieres comprobar si está ordenada ascendentemente? (s/n): ")

if respuesta.lower() == "s":
    print(estaOrdenada(lista, True))
else:
    print(estaOrdenada(lista, False))