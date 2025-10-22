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
if "Martes2" in diasemana: #Comprueba si un valor está en la lista
    print("Está")
else:
    print("No está")

for valorlista in diasemana: #Pinta los elementos uno debajo del otro
    print(valorlista)

