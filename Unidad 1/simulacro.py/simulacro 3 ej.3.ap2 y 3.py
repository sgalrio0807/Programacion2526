letra = input("Intoduce una letra: ").lower()
palabras = input("Dime palabras (stop para terminar): ").lower()
listaPalabras = []
contador = 0
while palabras != "stop":
    listaPalabras.append(palabras)
    contador += 1
    palabras = input("Dime palabras (stop para terminar): ").lower()

print("Introduzca E si desea devolver la lista de palabras que comienzan por la letra.")
print("Introduzca C si desea devolver la lista de palabras que contienen  la letra.")
print("Introduzca S para terminar el programa.")
seleccion = input("Selecciona una opción: ")

while seleccion != "s":
    if seleccion == "e":
        primeraletra = []
        palabrasinrepetir = []
        for palabra in listaPalabras:
            if palabra not in palabrasinrepetir:
                palabrasinrepetir.append(palabra)
        for palabra in palabrasinrepetir:
            if palabra[0] == letra:
                primeraletra.append(palabra)
        print (primeraletra)

    seleccion = input("Selecciona una opción: ").lower()

    if seleccion == "c":
        contieneletra = []
        palabrasinrepetir = []
        for palabra in listaPalabras:
            if palabra not in palabrasinrepetir:
                palabrasinrepetir.append(palabra)
        for palabra in palabrasinrepetir:
            if letra in palabra:
                contieneletra.append(palabra)
        print (contieneletra)

        seleccion = input("Selecciona una opción: ").lower()

print("Fin del programa")