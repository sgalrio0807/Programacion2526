def muestramenu():
    print("R) Registrar puntuaciones de equipo")
    print("L) Listar equipos y su puntuación por fase")
    print("C) Clasificados por fase")
    print("S) Salir")

def eligeopcion():
    menu= muestramenu()
    opcion = input("Introduce una opcion del menu: ")
    while opcion != "s":
        print(menu)
        opcion = input("Opción incorrecta, introduce una opcion del menu: ")
    return opcion

print(eligeopcion())