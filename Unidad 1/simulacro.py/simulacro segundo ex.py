print ("==========================================================")
print ("(A)Añadir cliente")
print ("(V) Validar emails almacenados")
print ("(C) Contar clientes de un dominio")
print ("(M) Mostrar los % de clientes premium y normales.")
print ("(G)Salir")
print ("===========================================================")

eleccion = input("Seleccione una opción: ").lower().upper()

while eleccion != "G":
    if eleccion == "A":
        premium = input("¿Eres premium?(S o N): ").lower().upper()
        correo = input("Dime tu correo: ")
        while premium != "S" or premium != "N":
            premium = input("¿Eres premium?(S o N): ").lower().upper()
    eleccion = input("Seleccione una opción: ").lower().upper()


print ("Salida del programa.")

