numeros = input("Introduce numero: ")

def cargaelementos(numeros):
    listaelementos = []
    while True:
        esnumero = True
        for i in numeros:
            if i not in "0123456789":
                esnumero = False

        if not esnumero:   
            return listaelementos

        listaelementos.append(int(numeros))  
        numeros = input("Introduce numero: ")

def estaordenadaascendentemente(lista):
    orden = True
    i = 0
    while i < len(lista)-1 and orden:
        if lista[i] > lista[i+1]:
            orden = False
        i = i + 1
    return orden

def estaordenada(lista, ascendente):
    if ascendente:
        print("Está ordenada ascendentemente")
    else: 
        print("No está ordenada ascendentemente")

lista = cargaelementos(numeros)
print(lista)
ascendente = estaordenadaascendentemente(lista)
estaordenada(lista, ascendente)



