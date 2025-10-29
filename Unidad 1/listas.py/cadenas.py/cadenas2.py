num= int(input("Dame un número entero: "))
listanum= []

while num != 0:
    listanum.append(1)
    num = num // 10

if listanum == []:
    listanum.append(1)

contador = 0
for i in listanum:
    contador += 1

print("Tiene", contador, "dígitos")
