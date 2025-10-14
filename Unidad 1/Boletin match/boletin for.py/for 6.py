num= int(input("Dame un numero: "))

for linea in range(1, num+1):
    if linea ==1 or linea == num:
        print("*" + "#" * (num-2)+ "*")
    
    else:
        cadena = ""
        for j in range (num):
            if j % 2 == 0:
                cadena += "*"
            else:
                cadena += "@"
        print(cadena)