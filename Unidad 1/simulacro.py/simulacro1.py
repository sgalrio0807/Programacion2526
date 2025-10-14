nombre= input("Dime tu nombre: ").lower()

while nombre != "exit":
    nota= float(input("Dime la nota que has obtenido: "))
    
    while nota <0 or nota >100:
        nota= float(input("Nota no valida, introduzca de nuevo: "))

    if nota >= 90 and nota <= 100:
        print("Sobresaliente")
    elif nota >= 70 and nota <= 89:
        print("Notable")
    elif nota >= 60 and nota <= 69:
        print("Bien")
    elif nota >= 50 and nota <= 59:
        print("Suficiente")
    elif nota >= 0 and nota <= 49:
        print("Suspenso")
    nombre= input("Dime tu nombre: ").lower()


