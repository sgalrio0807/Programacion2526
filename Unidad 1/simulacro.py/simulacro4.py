año= int(input("Dime un año: "))

while año >= 0:
    
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        print("El año" , año, "fue, es o será bisiesto.")
    else:
        print("El año" , año, "no ha sido, no es, ni será bisiesto.")
    
    año= int(input("Dime otro año(número negativo para finalizar): "))

print("Valor incorrecto, fin del programa.")