print("Selecciona una de las siguientes opciones (R, E, S)") 
print("R. Registrar juegos")
print("E. Mostrar estadísticas")	
print("S. Salir del programa")
menu= input("Seleccione una opción de el programa: ").lower()

listanombres= []
listapuntuaciones= []
listageneros= []

while menu not in ["r", "e", "s", "p", "d", "g"]:
    menu= input("Seleccione una opción de el programa: ").lower()

while menu == "r": 
    numveces= int(input("Cuántos juegos quiere registrar: "))
    for i in range(numveces):
        nombres= input("Dime el nombre del juego: ")
        listanombres.append(nombres)
        puntuaciones= int(input("Dime la puntuación que le das al juego(1-10): "))
        listapuntuaciones.append(puntuaciones)
        generos= input("Dime el genero del juego seleccionado: ")
        listageneros.append(generos)

    menu= input("Seleccione de nuevo una opción de el programa(e para ver tus estadísticas/s para salir del programa/ p para ver la mayor puntuación/d para ver si está en lista tu juego/g para seleccionar un genero): ").lower()


if menu == "e":
    print("Tu colección de juegos PSP:")
    for numveces in range (numveces):
        print(listanombres[numveces],"| Puntuaciones: ",listapuntuaciones[numveces],"| Género:", listageneros[numveces])

      
elif menu == "p":
    max = 0
    for puntuaciones in listapuntuaciones:
        if puntuaciones> max:
            max = puntuaciones
    pmax= puntuaciones.index(max)        
    print("Mejor puntuación: ")
    print(nombres[pmax])

elif menu == "d":
    comprobante= input("¿Que juego quieres comprobar?: ")
    if comprobante in listanombres:
        print(comprobante, "| Puntuación", puntuaciones, "| Género", generos)
    else:
        print("Este juego no está en la lista del sistema.")

elif menu == "g":
    comprobantegenero= input("¿De que genero quieres los juegos?: ")
    encontrado= False
    for i in range(comprobantegenero):
        comprobantegenero==encontrado
        if listanombres in comprobantegenero:
            encontrado= True    
            print(listanombres(comprobantegenero))
    else:
        print("No hay juegos para ese género en la lista del sistema")

elif menu == "s":
    print("Salir del programa") 