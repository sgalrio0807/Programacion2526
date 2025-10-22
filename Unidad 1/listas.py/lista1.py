animales= ["perro", "gato", "elefante", "oveja", "ratón", "pájaro"]
usuario= input("Dime un animal: ").lower()

if usuario in animales:
    print ("El/La", usuario, "si está en la lista.")
else:
    print ("El/La", usuario, "no está en la lista.")