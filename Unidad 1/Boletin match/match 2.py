dia= (input("Dame un dia de la semana"" "))
dia = dia.upper()
match dia:
    case "Martes"| "MARTES" | "martes":
        print ("----------" 
               "----------"
               "Martes"
               "----------"
               "----------"\
        "8:00 a 10:00 Prog" \
        "10:00 a 11:00 Leng" \
        "11:00 a 11:30 Recreo" \
        "11:30 a 13:30 Leng" \
        "13:30 a 14:30 IP")
    case "Sabado" | "domingo":
        print ("Dia de estudio y reflexion")
    case _:
        print ("El valor es incorrecto")