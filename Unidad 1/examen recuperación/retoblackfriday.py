def menu():
    ventas = [
    ["Portátil", 150, 799.99, 4.5],
    ["Smartphone", 250, 599.99, 4.3],
    ["Auriculares", 400, 49.99, 4.0],
    ["Tablet", 120, 299.99, 3.9],
    ["Monitor", 180, 199.99, 4.2],
    ["Smartwatch", 220, 149.99, 4.1],
    ["Teclado mecánico", 300, 89.99, 4.4],
    ["Ratón gaming", 350, 59.99, 4.0],
    ["Cámara digital", 90, 999.99, 4.6],
    ["Consola", 200, 399.99, 4.7]
]
    return ventas

def getProducto(ventas, nombreProducto):
    listavacia = []
    for i in ventas:
        if i[0] == nombreProducto:
            listavacia = i
    return listavacia

def calcular_ingresos(ventas, nombreProducto):
    producto = getProducto(ventas, nombreProducto)
    ingresos = 0
    if producto == []:
        ingresos = 0
    else:
        ingresos = producto[1] * producto[2]
    return ingresos
    
muestramenu = menu()
print(muestramenu)

listadeproducto = getProducto(muestramenu, "Smartwatch")
listadeproducto1 = getProducto(muestramenu, "Monitor")
listadeproducto2 = getProducto(muestramenu, "betis")
print(listadeproducto)
print(listadeproducto1)
print(listadeproducto2)

ingreosproducto = calcular_ingresos(muestramenu, "Monitor")
print(ingreosproducto)
