def esMultiplo():
    numero1= int(input("Dame un número entero: "))
    numero2= int(input("Dame otro número entero: "))
    
    if numero1 % numero2 == 0:
        print(numero1, "es mútiplo de", numero2)
    else: 
        print(numero1, "no es mútiplo de", numero2)

esMultiplo()