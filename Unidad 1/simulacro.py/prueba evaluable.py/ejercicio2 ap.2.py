num= int(input("Dime cuantas piedras quieres mostrar(0 - 5): "))
while num <0 or num >5:
    num= int(input("Número invalido, dime otro número: "))

par= num % 2 == 0
impar= num % 3 == 0

apostador= input("Dime si apuesta par o impar: ")
import random
maquina= random.randint(0, 5)

while num == maquina:
    print("Fin del programa.")

suma_total= num + maquina
if suma_total != apostador:
    print("La suma total es", suma_total, "así que ha ganado la máquina." )
elif suma_total == apostador:
    print("La suma total es", suma_total, "así que ha ganado el apostador.")

