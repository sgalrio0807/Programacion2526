letra = input("Intoduce una letra: ").lower()
palabras = input("Dime palabras (stop para terminar): ").lower()
listaPalabras = []
contador = 0
while palabras != "stop":
    listaPalabras.append(palabras)
    contador += 1
    palabras = input("Dime palabras (stop para terminar): ").lower()

print("La letra introducida es", letra)
print("La lista de palabras es", listaPalabras, "y el numero de palabras introducido es", contador)

