def muestramenu():
    print("R) Registrar puntuaciones de equipo")
    print("L) Listar equipos y su puntuación por fase")
    print("C) Clasificados por fase")
    print("S) Salir")

def eligeopcion():
    menu= muestramenu()
    opcion = input("Introduce una opcion del menu: ")
    while opcion != "s" and opcion != "r" and opcion != "l":
        print(menu)
        opcion = input("Opción incorrecta, introduce una opcion del menu: ")
    return opcion

def opcionR():
    fase= input("Introduce la fase que quieres registrar: ")
    while fase != "inicial" and fase != "semifinal" and fase != "final":
        fase= input("Opción incorrecta, introduce la fase que quieres registrar: ")
    return fase

def registroPuntuaciones(fase):
    puntuacionesinicial = []
    cochesinicial = []
    puntuacionessemi = []
    cochessemi = []
    puntuacionesfinal = []
    cochesfinal = []
    match fase:
        case "inicial":
            for i in range(0,8):
                coches = input("Introduce nombre de equipo: ")
                cochesinicial.append(coches)
                puntuacion = input("Introduce puntuación de su equipo: ")
                puntuacionesinicial.append(puntuacion)
                print("===========================================")
                print("Fase inicial")
                print("===========================================") 
                for i in range(len(cochesinicial)):
                    print("El equipo",cochesinicial[i], "ha obtenido", puntuacionesinicial[i], "puntos")
        case "semifinal":
            for i in range(0,4):
                coches = input("Introduce nombre de equipo: ")
                cochessemi.append(coches)
                puntuacion = input("Introduce puntuación de su equipo: ")
                puntuacionessemi.append(puntuacion)
                print("===========================================")
                print("Fase semifinal")
                print("===========================================") 
                for i in range(len(cochessemi)):
                    print("El equipo",cochessemi[i], "ha obtenido", puntuacionessemi[i], "puntos")
        case "final":
            for i in range(0,2):
                coches = input("Introduce nombre de equipo: ")
                cochesfinal.append(coches)
                puntuacion = input("Introduce puntuación de su equipo: ")
                puntuacionesfinal.append(puntuacion)
                print("===========================================")
                print("Fase final")
                print("===========================================") 
                for i in range(len(cochesfinal)):
                    print("El equipo",cochesfinal[i], "ha obtenido", puntuacionesfinal[i], "puntos")
    return puntuacionesinicial, cochesinicial, puntuacionessemi, cochessemi, puntuacionesfinal, cochesfinal


elegiropcion = eligeopcion()
if elegiropcion == "r":
    print(opcionR())

registrar = registroPuntuaciones(opcionR())
print("===========================================")
print("Datos registrados correctamente")
print("===========================================")      


