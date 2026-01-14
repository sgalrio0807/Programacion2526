matriz = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'Ñ', 'O'],
    ['P', 'Q', 'R', 'S'],
    ['T', 'U', 'V', 'W'],
    ['X', 'Y', 'Z', '_']
]

def descifrar(cadena):
    resultado = ""
    pares = cadena.split(",")

    for par in pares:
        fila = int(par[0]) - 1
        columna = int(par[1]) - 1
        letra = matriz[fila][columna]
        resultado += letra

    return resultado

def cifrar(texto):
    texto = texto.upper()
    resultado = []

    for letra in texto:
        if letra == " ":
            letra = "_"

        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == letra:
                    par = str(i + 1) + str(j + 1)
                    resultado.append(par)

    return ",".join(resultado)


mensaje_cifrado = "21,34,74,21,71,31,61,44,74,34,34,21,23,11,74,13,44,42,74,61,53,11,12,11,32,44,74,72,74,51,21,53,54,31,54,61,21,42,13,31,11"
print(descifrar(mensaje_cifrado))

mensaje = "NO SOLO HAY QUE CONFIAR EN EL PROCESO, HAY QUE SEGUIRLO"
print(cifrar(mensaje))
