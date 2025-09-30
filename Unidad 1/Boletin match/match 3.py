numMes= input("Dame el numero de mes" " ")

match numMes:
    case "1" | "2" | "3":
        print ("Invierno")
    case "4" | "5" | "6":
        print ("Primavera")
    case "7" | "8" | "9":
        print ("Verano")
    case "10" | "11" | "12":
        print ("Otoño")
    case _:
        print ("No corresponde a ninguna estacion")
