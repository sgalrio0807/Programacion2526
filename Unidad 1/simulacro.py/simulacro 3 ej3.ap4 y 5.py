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
print("Introduzca L si desea ver la palabra más corta y más larga.")
print("Introduzca S para terminar el programa.")
seleccion = input("Selecciona una opción: ")

while seleccion != "s":
    if seleccion == "e":
        secuencia = input("Dime una secuencia de caracteres: ").lower()
        primerasecuencia = []
        palabrasinrepetir = []
        for palabra in listaPalabras:
            if palabra not in palabrasinrepetir:
                palabrasinrepetir.append(palabra)
        for palabra in palabrasinrepetir:
            if palabra[:len(secuencia)] == secuencia:
                primerasecuencia.append(palabra)
        print (primerasecuencia)

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
    
    if seleccion == "l":
        palabracorta = listaPalabras[0]
        palabralarga = listaPalabras[0]
        for palabra in listaPalabras:
            if len(palabra) < len(palabracorta):
                palabracorta = palabra
            if len(palabra) > len(palabralarga):
                palabralarga = palabra

        print("La palabra más corta es:", palabracorta)
        print("La palabra más larga es:", palabralarga)

    seleccion = input("Selecciona una opción: ").lower()


print("Fin del programa")