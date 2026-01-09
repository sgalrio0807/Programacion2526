import random
lista1 = []
lista2 = [] 
lista3 = [] 
lista4 = [] 
lista5 = [] 
carton = []
def getListaSinRepetidos(lista1, lista2, lista3, lista4, lista5): 

    for columna1 in range(5):
        columna1 = (random.randint(1,15))
        while columna1 not in lista1:
            lista1.append(columna1)
    for columna2 in range(5):
        columna2 = (random.randint(16,30))
        while columna2 not in lista2:
            lista2.append(columna2)
    for columna3 in range(5):
        columna3 = (random.randint(31,45))
        while columna3 not in lista3:
            lista3.append(columna3)
    for columna4 in range(5):
        columna4 = (random.randint(46,60))
        while columna4 not in lista4:
            lista4.append(columna4)
    for columna5 in range(5):
        columna5 = (random.randint(61,75))
        while columna5 not in lista5:
            lista5.append(columna5)

    lista3.pop(2)
    lista3.insert(2, "--")
    return lista1, lista2, lista3, lista4, lista5

def generaCarton(lista1, lista2, lista3, lista4, lista5):
    carton = getListaSinRepetidos(lista1, lista2, lista3, lista4, lista5) 
    print(lista1)
    print(lista2)
    print(lista3)
    print(lista4)
    print(lista5)
    for i in carton:
        i[0] == (1,15)
        i[1] == (16,30)
        i[2] == (31,45)
        i[3] == (46,60)
        i[4] == (61,75)
    return carton

imprimocarton = generaCarton(lista1, lista2, lista3, lista4, lista5)
print(imprimocarton)

carton = [lista1,lista2,lista3,lista4,lista5]
assert generaCarton(len(carton) == 5 and len(carton) == 5) == True
assert generaCarton(carton[2][2] == "--") == True


