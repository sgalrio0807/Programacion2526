listanormal=[]
listamultiplos=[]
for i in range(10):
    num= int(input("Introduce un numero: "))
    listanormal.append(num)

def multiplosdetres(listanormal):
    for terminaen3 in listanormal:
        if terminaen3 % 10 == 3:
            listamultiplos.append(terminaen3)
    return listamultiplos

multiplos = multiplosdetres(listanormal)
print(multiplos)