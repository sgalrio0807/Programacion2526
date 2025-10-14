num= int(input("Dame un numero: "))

for linea in range(num):
    if linea %2 == 0:
        print("*" + "#" * (num-2)+ "*")
    
    else:
        cadena = ""
        for j in range (num):
            if j % 2 == 0:
                cadena += "*"
            else:
                cadena += "@"
        print(cadena)