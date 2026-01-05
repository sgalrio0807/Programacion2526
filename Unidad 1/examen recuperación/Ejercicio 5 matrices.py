matriz = [[8,1,6],[3,5,7],[4,9,2]]

def sumafilapar(matriz):
    suma = 0
    for i in range(len(matriz)):
        if i % 2 == 0:      
            for elemento in matriz[i]:
                suma += elemento
    return suma

sumanumeros = sumafilapar(matriz)
print(sumanumeros)