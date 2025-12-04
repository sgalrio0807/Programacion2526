def redondear(num):
    resultado = 0.0
    if num == int(num):
        resultado = int(num) + 0.00
    else:
        n = int(num * 1000)
        parte_entera = n // 1000
        primero = (n // 100) % 10
        segundo = (n // 10) % 10
        tercero = n % 10
        if tercero >= 5:
            segundo = segundo + 1
        resultado = parte_entera + primero/10 + segundo/100
    return resultado

resultado1 = redondear(1.449)
resultado2 = redondear(1.444)
resultado3 = redondear(0.375)
resultado4 = redondear(0.374)
resultado5 = redondear(1)

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)