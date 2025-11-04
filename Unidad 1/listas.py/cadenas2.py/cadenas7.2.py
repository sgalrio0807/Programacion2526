nombre = "sergio galan rios"
nombreseparado = nombre.split()
palabrasalida = ""
for palabra in nombreseparado:
    palabrasalida = palabrasalida + palabra[0].upper() + palabra[1:] + " "
print(palabrasalida)