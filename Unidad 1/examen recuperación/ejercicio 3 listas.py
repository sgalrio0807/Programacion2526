diasemana = ["Lunes" , "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print(diasemana[6])

lista = []
import random
while len(lista) <= 4:
    aleatorio = random.randint(0,8)
    lista.append(aleatorio)
print(lista)

listamultiplos = []
for i in range(0,61,3):
    listamultiplos.append(i)
listamultiplos.pop(0)
print(listamultiplos)

listamultiplos.append("martes")
listamultiplos.append("miercoles")
listamultiplos.append("jueves")
print(listamultiplos)

for i in range(0,31,3):
    listamultiplos.append(i)
print(listamultiplos[0:10])

listamultiplos.pop(8)
listamultiplos.insert(8, "programo")
print(listamultiplos[0:10])