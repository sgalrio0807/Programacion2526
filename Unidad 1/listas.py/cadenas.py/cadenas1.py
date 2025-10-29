listanum= []
num = int(input("Dame un número para comprobar si es capicúa: "))
listanum.append(num)
listareves = ""

for i in str(listanum[0]):
    listareves= i + listareves

if str(listanum[0]) == listareves:
    print("Capicúa")
else:
    print("No es capicúa")