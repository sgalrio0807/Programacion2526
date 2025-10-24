print("Selecciona una de las siguientes opciones (R, E, S)") 
print("R. Registrar juegos")
print("E. Mostrar estadísticas")	
print("S. Salir del programa")
menu= input("Seleccione una opción de el programa: ").lower()

listanombres= []
listapuntuaciones= []
listageneros= []

while menu not in ["r", "e", "s"]:
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

    menu= input("Seleccione de nuevo una opción de el programa(e para ver tus estadísticas/s para salir del programa): ").lower()


if menu == "e":
    print("Tu colección de juegos PSP:")
    for numveces in range (numveces):
        print(listanombres[numveces],"|",listapuntuaciones[numveces],"|", listageneros[numveces])
       
elif menu == "s":
    print("Salir del programa")  