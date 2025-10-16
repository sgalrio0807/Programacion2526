mes= int(input("Dime el mes: "))
dia= int(input("Dime el día: "))
while (dia >31 and dia <1) and (mes >12 and mes <1):
    mes= int(input("Dime el mes de nuevo: "))
    dia= int(input("Dime el día de nuevo: "))

hemis= str(input("Dime el hemisferio: ")).lower()
while hemis != "norte" and hemis != "sur":
    hemis= input("Incorrecto, vuelve a introducir hemisferio: ").lower()

    match hemis:
        case "norte":
            if (mes == 3 and dia >= 21) or mes == 4 or mes== 5 or (mes == 6 and dia <21):
                        print("Primavera")
            elif (mes == 6 and dia >= 21) or mes == 7 or mes== 8 or (mes == 9 and dia <23):
                        print("Verano")
            elif (mes == 9 and dia >= 23) or mes == 10 or mes== 11 or (mes == 12 and dia <21):
                        print("Otoño")
            elif (mes == 12 and dia >= 21) or mes == 1 or mes== 2 or (mes == 3 and dia <21):
                        print("Invierno")

        case "sur":
            if (mes == 3 and dia >= 21) or mes == 4 or mes== 5 or (mes == 6 and dia <21):
                        print("Otoño")
            elif (mes == 6 and dia >= 21) or mes == 7 or mes== 8 or (mes == 9 and dia <23):
                        print("Invierno")
            elif (mes == 9 and dia >= 23) or mes == 10 or mes== 11 or (mes == 12 and dia <21):
                        print("Primavera")
            elif (mes == 12 and dia >= 21) or mes == 1 or mes== 2 or (mes == 3 and dia <21):
                        print("Verano")