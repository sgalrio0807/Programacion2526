humano=  float(input("¿Piedra(0), Papel(1) o Tijeras(2)?: "))
import random
maquina= random.randint(0, 2)
print ("La maquina ha elegido", maquina)
match humano:
    case 0:
        if maquina ==0:
            print ("Empate")
        elif maquina ==1:
            print ("Has perdido")
        elif maquina ==2:
            print ("Has ganado")
    
    case 1:
        if maquina ==0:
            print ("Has ganado")
        elif maquina ==1:
            print ("Empate")
        elif maquina ==2:
            print ("Has perdido")

    case 2:
        if maquina ==0:
            print ("Has perdido")
        elif maquina ==1:
            print ("Has ganado")
        elif maquina ==2:
            print ("Empate")