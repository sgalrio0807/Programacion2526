contra = "1234"
contraescrita= str(input("Introduzca contraseña: "))

while contraescrita != contra:
    print("Intento fallido")
    contraescrita= str(input("Introduzca contraseña de nuevo: "))
print("Bienvenido")