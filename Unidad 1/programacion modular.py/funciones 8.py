def calcular_tiempo(segundos):
    horas = segundos // 3600              # 1 hora = 3600 segundos
    minutos = (segundos % 3600) // 60     # resto dividido entre 60 da los minutos
    segundos_finales = segundos % 60      # lo que queda son los segundos
    return horas, minutos, segundos_finales   # devuelve 

def mostrar_tiempo():
    segundos = int(input("Escribe el tiempo en segundos: "))  # pide al usuario el número
    h, m, s = calcular_tiempo(segundos)                       # llama a la otra función
    print(segundos, "segundos equivalen a", h, "horas,", m, "minutos y", s, "segundos.")

mostrar_tiempo()  # llamar a la función principal