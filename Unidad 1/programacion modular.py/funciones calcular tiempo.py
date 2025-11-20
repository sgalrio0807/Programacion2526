def calcular_tiempo(segundos):
    horas = segundos // 3600             
    minutos = (segundos % 3600) // 60    
    segundos_finales = segundos % 60      
    return horas, minutos, segundos_finales   

def mostrar_tiempo():
    segundos = int(input("Escribe el tiempo en segundos: ")) 
    h, m, s = calcular_tiempo(segundos)                      
    print(segundos, "segundos equivalen a", h, "horas,", m, "minutos y", s, "segundos.")

tiempo = mostrar_tiempo()  