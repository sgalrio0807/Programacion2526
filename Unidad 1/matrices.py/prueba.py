lista1 = [0,2,4]
lista2 = [1,3,5]
lista3 = [6,8,10]
matriz = [lista1,lista2,lista3] 
#print(matriz)          #imprime todas las listas
#print(matriz[1])       #imprime lista1
#print(matriz[1][1])    #imprime elemto fila 1 columna 1
lista = []
def sumafilas(matriz):
    sumalista = matriz[0] + matriz [2]
    sumaelementos = (matriz [1][1]) + (matriz [2][2])
    lista.append(sumaelementos)
    return sumalista,sumaelementos,lista

def sumamatriz(lista):
    suma = 0
    for i in range (0,len(lista)):
        suma = suma+sumafilas(matriz, i)
    return suma

#def sumamatriz(matriz):
    listamatriz = []
    suma1 = matriz[0][0] + matriz[0][1] + matriz[0][2]
    suma2 = matriz[1][0] + matriz[1][1] + matriz[1][2]
    suma3 = matriz[2][0] + matriz[2][1] + matriz[2][2]
    listamatriz = suma1 + suma2 +suma3
        
    return listamatriz

suma= sumafilas(matriz)
sumamatrices = sumamatriz(lista)
print(suma)
print(sumamatriz)







