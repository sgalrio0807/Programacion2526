diasemana= input("Dame un dia de la semana:")

match diasemana:
    case "L" | "M" | "X" | "J" | "V":
        print("IES")
    case "S" | "D":
        print("Casa")
    case _:
        print("No valido")