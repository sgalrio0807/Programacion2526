num1 = int(input("Dame un número: "))
num2 = int(input("Dame otro número: "))

while num1 != 0 and num2 != 0:
    while num1 >= num2:
        num1 = int(input("No válido, dame un número: "))
        num2 = int(input("Dame otro número: "))

    print("================================================")
    print("Impares que existen entre [", num1, "-", num2, "]: ", end="")

    contador = 0
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            print(i, end=", ")
            contador = contador + 1

    print("\nEn total existen", contador, "números impares en el rango.")
    print("================================================")

    num1 = int(input("Introduce otro primer número: "))
    num2 = int(input("Introduce otro segundo número: "))

print("Programa terminado.")