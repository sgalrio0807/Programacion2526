#leeyvalidadatos
# compruebasiespar
# ejecutalodelpar
# compruebamultiplo3
# ejecutamultiplo3
# compruebamultiplo7
# ejecutamultiplo7

# definicion funcion compruebasiespar recibe un numero y devuelve booleano(true/false)
def compruebasiespar(numero):
    return numero %2 == 0

numero= int(input("Dame un número:"))
esPar = compruebasiespar(numero)
print(numero, esPar)
esPar = compruebasiespar(32)

print("32", esPar)


#def calculacadena(posic1,posic2,num):
    #salida=num[posic1]+num[posic2]
    #print(salida)