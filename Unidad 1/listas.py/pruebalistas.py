print(("Empiezo"))
diasemana= ["Lunes" , "Martes", "Jueves"]
diasfindesemana= ["Sábado", "Domimgo"]
diasemana.append("Viernes") #Añado al final de la lista
diasemana.insert(2, "Miércoles") #Añado a una posición de la lista
diasemana= diasemana + diasfindesemana #Junto dos listas 
diasemana.pop(6) #Borrar elemento de la lista 
diasemana.remove("Martes") #Borra valor
print(len(diasemana)) #Tamaño de la lista
print(diasemana)
print(diasemana.index("Lunes")) #Devuelve en que posición está ese valor
print (diasemana[1:3]) #Devuelve lista de una posición a otra
print (diasemana[:]) #Devuelve lista completa
print (diasemana[1:]) #devuelve elementos desde el 1 hasta el final
print (diasemana[:4]) #devuelve elementos desde el principio hasta la posicion
if "Martes2" in diasemana: #Comprueba si un valor está en la lista
    print("Está")
else:
    print("No está")

for valorlista in diasemana: #Pinta los elementos uno debajo del otro
    print(valorlista)

