print("A.Introduzca el número de árboles que va a introducir.")
print("B.Tipo, diámetro y altura; si es tipo B además, la edad.")
print("C.Mostrar el resumen de los datos guardados.")
print("D.Mostar un resumen de la información introducida.")
print("E.Salir del programa ")
menu = input("Dime una opción del menú(E para salir del programa): ").lower()
listaalturaArbol = []

while menu == "a":
    contador = 0 
    numArboles = int(input("Introduzca el número de árboles: "))
    while numArboles > contador:
        contador += 1
        tipoArbol = input("Dime el tipo de árbol: ").lower()
        diametroArbol = int(input("Dime el diámetro del árbol: "))
        alturaArbol = int(input("Dime la altura del árbol: "))
        listaalturaArbol.append(alturaArbol)
        if tipoArbol == "b":
            edadArbol= int(input("Dime la edad del árbol: "))

    menu = input("Dime una opción del menú(E para salir del programa): ").lower()

if menu == "d":
    alturamax = max(listaalturaArbol)
    alturamin = min(listaalturaArbol)
    mediaEdad = sum(edadArbol) / len(edadArbol)
    print("La altura máxima es",alturamax)
    print("La altura mínima es",alturamin)
    print("La media de edad para los de tipo B es",mediaEdad)
    print("Hay en total",numArboles,"árboles.")

elif menu == "e":
    print("Saliendo del programa.")