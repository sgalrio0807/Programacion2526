numMes= int(input("Dame el numero de mes:"))
numDia= int(input("Dame el numero de dia:"))

match numMes:
    case "1" | "2" | "3":
        print ("Invierno")
    case "4" | "5" | "6":
        print ("Primavera")
    case "7" | "8" | "9":
        print ("Verano")
    case "10" | "11" | "12":
        print ("Otoño")

if numMes ==3 and numDia <=20:
    print ("Es invierno")
elif numMes ==3 and numDia >=20:
    print ("Es primavera")
elif numMes ==6 and numDia <=20:
    print ("Es primavera")
elif numMes ==6 and numDia >=20:
    print ("Es verano")
elif numMes ==9 and numDia <=20:
    print ("Es verano")
elif numMes ==9 and numDia >=20:
    print ("Es otoño")
elif numMes ==12 and numDia <=20:
    print ("Es otoño")
elif numMes ==12 and numDia >=20:
    print ("Es invierno")


