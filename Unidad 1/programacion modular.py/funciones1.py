def obtieneyvalidadatosdeentrada():
    numero= int(input("Dame un número positivo: "))
    while numero < 0:
        numero= int(input("Dame un número positivo: "))
    return numero

obtieneyvalidadatosdeentrada()
    