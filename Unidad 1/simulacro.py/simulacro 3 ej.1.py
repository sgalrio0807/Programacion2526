print("A.Introduzca el número de árboles que va a introducir.")
print("B.Tipo, diámetro y altura; si es tipo B además, la edad.")
print("C.Mostrar el resumen de los datos guardados.")
print("D.Mostar un resumen de la información introducida.")
print("E.Salir del programa ")
menu = input("Dime una opción del menú(E para salir del programa): ").lower()

listanumArboles = []
listaedadArbol = []
listaalturaArbol = []
listadiametro = []
listatipoarbol = []

contador = 0


while menu == "a": 
    numArboles = int(input("Introduzca el número de árboles: "))
    listanumArboles.append(numArboles)
    while numArboles > contador:
        contador += 1
        tipoArbol = input("Dime el tipo de árbol: ").lower()
        listatipoarbol.append(tipoArbol)
        diametroArbol = int(input("Dime el diámetro del árbol: "))
        listadiametro.append(diametroArbol)
        alturaArbol = int(input("Dime la altura del árbol: "))
        listaalturaArbol.append(alturaArbol)
        if tipoArbol == "b":
            edadArbol= int(input("Dime la edad del árbol: "))
            listaedadArbol.append(edadArbol)

    menu = input("Dime una opción del menú(E para salir del programa): ").lower()

if menu == "d":
    alturamax = max(listaalturaArbol)
    alturamin = min(listaalturaArbol)
    mediaEdad = sum(listaedadArbol) / len(listaedadArbol)
    print("La altura máxima es",alturamax)
    print("La altura mínima es",alturamin)
    print("La media de edad para los de tipo B es",mediaEdad)
    print("Hay en total",numArboles,"árboles.")

elif menu == "f":
    arbolmasalto = [max(listaalturaArbol), tipoArbol, diametroArbol]
    print (arbolmasalto)

elif menu == "e":
    print("Saliendo del programa.")