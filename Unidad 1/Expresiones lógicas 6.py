cajeroautomático = float(input("Ingrese el dinero a retirar: "))
saldo = 1000
if cajeroautomático <= saldo:
    print("Retiro exitoso")
else:
    print("Saldo insuficiente")