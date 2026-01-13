usuarioLeido = input("Introduce tu nombre de usuario: ")
claveLeida = input("Introduce la contraseña: ")
mensajeSucio = input("Introduce texto de conjuro: ")

def validarAcceso(claveLeida):
    esValida = True
    while len(claveLeida) <8:
        claveLeida = input("Contraseña inválida, introduce de nuevo: ")
    if "#" not in claveLeida and "*" not in claveLeida:
        esValida = False
    else:
        esValida = True
    return esValida

def limpiarConjuro(mensaje):
    mensaje = mensaje.upper()
    mensaje = mensaje.replace("MALDICIÓN", "BENDICIÓN")
    return mensaje

if validarAcceso(usuarioLeido, claveLeida):
    mensajeSucio = input("Introduce texto de conjuro: ")
    print(limpiarConjuro(mensajeSucio))
else:
    print("Acceso denegado")

