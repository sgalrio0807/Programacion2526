dia= input("Dame un dia de la semana"" ")

match dia:
    case "Lunes"| "LUNES" | "lunes":
        print ("----------" 
               "----------"
               "Lunes"
               "----------"
               "----------"\
        "8:00 a 9:00 Fol" \
        "9:00 a 10:00 Ede" \
        "10:00 a 11:00 Prog" \
        "11:00 a 11:30 Recreo" \
        "11:30 a 12 Prog" \
        "12:00 a 14:00 BBDD")
    case "Sabado" | "domingo":
        print ("Dia de estudio y reflexion")
    case _:
        print ("El valor es incorrecto")

        

   

        


