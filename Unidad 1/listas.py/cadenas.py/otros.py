#========================================================================
#las cadenas son inmutables
#========================================================================
nombre = "Lucía"
nombre.replace("a" , "o") #no cambia la variable nombre
print(nombre)
nombre = nombre.replace("a" , "o") #si cambia nombre
#========================================================================
#paso de string a lista: lista(nombrecadena) y de lista a string: for y concateno caracter a caracter
#========================================================================
nombrelista = list(nombre) #paso de string a lista de caracteres
nombrelista.insert (0, "A")
print(nombrelista)
cadenasalida = ""
for valor in nombrelista: #paso de lista de caracteres a string
    cadenasalida = cadenasalida + valor
print(cadenasalida)