num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
num3 = int(input("Introduce otro número: "))

while num1 != 0 and num2 !=0 and num3 !=0:

    if num1 < num2 and num2 < num3:
        print("creciente")
    elif num1 > num2 and num2 > num3:
        print("decreciente")
    else:
        print("desordenados")
    
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
    num3 = int(input("Introduce otro número: "))

print("fin")