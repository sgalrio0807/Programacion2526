num= int(input("Dime un numero: "))

if num <= 0:
  num=int(input("El numero debe ser mayor que 0"))

for i in range (1, num +1):
     print(i)
print("Final")