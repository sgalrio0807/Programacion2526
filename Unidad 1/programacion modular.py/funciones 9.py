def calcular_tiempo(segundos):
    horas = segundos // 3600              
    minutos = (segundos % 3600) // 60    
    segundos_finales = segundos % 60      
    return horas, minutos, segundos_finales   

def mostrar_tiempo():
    segundos = int(input("Escribe el tiempo en segundos: ")) 
    h, m, s = calcular_tiempo(segundos)                      
    print(segundos, "segundos equivalen a", h, "horas,", m, "minutos y", s, "segundos.")

def a_horas(segundos):           # pasar a horas
    return segundos / 3600

def a_minutos(segundos):         # pasar a minutos
    return segundos / 60

def a_segundos(horas, minutos, segundos):           # pasar a segundos
    return horas * 3600 + minutos * 60 + segundos

def menu():
    opcion = ""   

    while opcion != "-1":
        print("\n======== MENÚ ========")
        print("S - Convertir a segundos")
        print("M - Convertir a minutos")
        print("H - Convertir a horas")
        print("-1 - Salir")

        opcion = input("Elige una opción: ").upper() 

        if opcion == "S":
            horas = int(input("Introduce las horas: "))
            minutos = int(input("Introduce los minutos: "))
            segundos = int(input("Introduce los segundos: "))
            total = a_segundos(horas, minutos, segundos)
            print("El tiempo total equivale a", total, "segundos.")

        elif opcion == "M":
            segundos = int(input("Introduce los segundos: "))
            print(segundos, "segundos equivalen a", a_minutos(segundos), "minutos.")

        elif opcion == "H":
            segundos = int(input("Introduce los segundos: "))
            print(segundos, "segundos equivalen a", a_horas(segundos), "horas.")

        elif opcion == "-1":
            print("Salir del programa.")

        else:
            print("Opción no válida, intenta de nuevo.")

menu()