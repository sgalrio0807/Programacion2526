listanum= []
num = int(input("Dame un número para ponerlo al revés: "))
listanum.append(num)
listareves = ""

for i in str(listanum[0]):
        listareves= i + listareves

print("Número al revés:", listareves)
