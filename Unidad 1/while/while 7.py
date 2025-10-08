import random
num= random.randint(1,10)
humano= int(input("Dame un numero: "))

while num != humano:
    print("sigue intentandolo")
    humano= int(input("Dame otro numero: "))

if num == humano:
    print("Lo has adivinado")
