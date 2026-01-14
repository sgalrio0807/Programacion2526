def tirar_dado():
    from random import randint
    return randint(1,6)

def apostar():
    maquina = tirar_dado()
    jugador = int(input("Introduce tu numero: "))
    apuesta = int(input("Introduce la cantidad que apuestas: "))
    jugadas = 0
    ganancias = 0
    perdidas = 0 
    while jugador != -1:
        jugadas += 1
        if maquina == jugador:
            ganancias += apuesta
            print("En la",jugadas,"º jugada apostó al valor",jugador, "y sumó",maquina, ", ganando",apuesta, "€")
        else:
            perdidas += apuesta
            print("En la",jugadas,"º jugada apostó al valor",jugador, "y sumó",maquina, ", perdiendo",apuesta, "€")
        maquina = tirar_dado()
        jugador = int(input("Introduce tu numero: "))
        if jugador != -1:
            apuesta = int(input("Introduce la cantidad que apuestas: "))   
    return ganancias, perdidas

def retirarse(ganancias, perdidas):
    saldo = ganancias - perdidas
    return saldo

jugar = apostar()          
ganancias = jugar[0]      
perdidas = jugar[1]        

contar = retirarse(ganancias, perdidas)  

print("\nRESUMEN FINAL")
print("Ganancias:", ganancias, "€")
print("Pérdidas:", perdidas, "€")
print("Saldo final:", contar, "€")
