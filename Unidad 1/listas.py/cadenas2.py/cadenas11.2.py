numentero = input("Dime un numero: ")
if len(numentero)>3:
    for i in range(-3, -1, -3):
        print(numentero[i:len(numentero)]-i)
