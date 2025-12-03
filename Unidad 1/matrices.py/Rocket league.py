def pintaMenu():
    print ("R) Registrar puntuaciones de equipo")
    print ("L) Listar equipos y su puntuación por fase")
    print ("C) Clasificados por fase")
    print ("S) Salir")
    opcion = input("Selecciona una opción del menú: ").lower()
    while opcion not in ("r", "l", "c", "s"):
        print("Opcion incorrecta")
        opcion = input("Selecciona otra opción del menú: ").lower()
    return opcion

def registroPuntuaciones(opcion):
    eleccion = opcion
    listaequipos = []
    listapuntos = []
    if eleccion == "r":
        fase = input("Que fase quieres registrar(inicial, semifinal o final): ")
        while fase not in ("inicial", "semifinal", "final"):
            fase = input("Incorrecto, di de nuevo la fase que quieres registrar(inicial, semifinal o final): ")
        if fase == "inicial":
            for i in range(8):
                equipos = input("Dime el nombre del equipo: ")
                listaequipos.append(equipos)
                puntos = int(input("Y su puntuación: "))
                listapuntos.append(puntos)
        elif fase == "semifinal":
            for i in range(4):
                equipos = input("Dime el nombre del equipo: ")
                listaequipos.append(equipos)
                puntos = int(input("Y su puntuación: "))
                listapuntos.append(puntos)
        else:
            for i in range(2):
                equipos = input("Dime el nombre del equipo: ")
                listaequipos.append(equipos)
                puntos = int(input("Y su puntuación: "))
                listapuntos.append(puntos)
        print("===========================================")
        print("Datos registrados correctamente")
        print("===========================================")
    return fase, listaequipos, listapuntos

def listarEquipos(opcion, fase_guardada, listaequipos, listapuntos):
    eleccion = opcion
    if eleccion == "l":
        fase = input("Que fase quieres listar(inicial, semifinal o final): ")
        while fase not in ("inicial", "semifinal", "final"):
            print("===========================================")
            print("La Fase", fase, "no ha sido registrada en el sistema")
            print("===========================================")
            fase = input("Di de nuevo la fase que quieres listar(inicial, semifinal o final): ")
        
        if fase != fase_guardada:
            print("===========================================")
            print("La Fase", fase, "no ha sido registrada en el sistema")
            print("===========================================")
        else:
            print("===========================================")
            print("Fase", fase)
            print("===========================================")
            for i in range(len(listaequipos)):
                print("El equipo", listaequipos[i], "ha obtenido", listapuntos[i], "puntos")
    return listaequipos, listapuntos

opcion = pintaMenu()
print(opcion)

registro = registroPuntuaciones(opcion)
print(registro)

listar = listarEquipos(opcion, registro[0], registro[1], registro[2])
print(listar)