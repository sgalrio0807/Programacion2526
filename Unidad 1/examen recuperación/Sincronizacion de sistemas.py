def pidedatos():
    numdatos = int(input("Introduce la cantidad de datos que quieres registrar: "))
    listarecursos = []
    listacantidad = []
    listanivelcritico = []
    while numdatos != 0:
        numdatos -= 1
        recurso = input("Introduce recurso: ")
        listarecursos.append(recurso)
        cantidad = int(input("Introduce cantidad: "))
        listacantidad.append(cantidad)
        nivelcritico = int(input("Introduce nivel crítico: "))
        listanivelcritico.append(nivelcritico)
        matriz = [(listarecursos),(listacantidad),(listanivelcritico)]
    return matriz
    
def leeRecursoBaseDatos(nombreRecurso, matriz):
    encontrado = False
    i = 0
    while (i < len(matriz)) and not encontrado:
        if nombreRecurso == matriz[0][i]:
            encontrado = True
        else: 
            i += 1
    return encontrado

matriz = pidedatos()
nombreRecurso = input("Introduce el nombre del recurso que quieras buscar: ")
cadenadefallo = "-1"
lectura = leeRecursoBaseDatos(nombreRecurso, matriz)
print(lectura)
