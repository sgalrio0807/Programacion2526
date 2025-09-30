opcion= input("Dame una opcion")

match opcion:
    case "A":
        print ("Alta")
    case "B":
      print ("Baja")
    case "C":
        print ("Cambio")
    case _:
        print("No valido")