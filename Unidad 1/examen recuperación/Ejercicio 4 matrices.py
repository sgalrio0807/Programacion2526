matriz = [[8,2,6],[3,5,7],[4,8,2]]
numfila = int(input("Dime el número de fila:"))

def sumafila(matriz, numfila):
    suma = 0
    for elemento in matriz[numfila]:
            suma += elemento
    return suma
   
sumanumeros = sumafila(matriz, numfila)
print (sumanumeros)