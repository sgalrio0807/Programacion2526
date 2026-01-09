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

def esProductoDestacado(ventas, nombreProducto):
    esDestacado = True
    producto = getProducto(ventas, nombreProducto)
    if producto[3] >= 4.2:
        esDestacado = True
    else:
        esDestacado = False
    return esDestacado

def getProductosDestacados(ventas):
    lista = []
    for i in ventas:
        esDestacado = esProductoDestacado(ventas, i[0])
        producto = getProducto(ventas, i[0])
        if esDestacado == True:
            lista.append(i)
    return lista

def tieneMayorIngreso(nombreProducto1, nombreProducto2):
    ventas = menu()
    ingreso1 = calcular_ingresos(ventas, nombreProducto1)
    ingreso2 = calcular_ingresos(ventas, nombreProducto2)
    if ingreso1 > ingreso2:
        mayoringreso = True
    else:
        mayoringreso = False
    return mayoringreso

def calcularIngresosTotales():
    ventas = menu()
    total = 0
    for i in ventas:
        unidades = i[1]
        precio = i[2]
        total += unidades * precio
    return total
      
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

destacado = esProductoDestacado(muestramenu, "Portátil")
destacado1 = esProductoDestacado(muestramenu, "Tablet")
print(destacado)
print(destacado1)

listadestacados = getProductosDestacados(muestramenu)
print(listadestacados)

mayoresingresos1 = tieneMayorIngreso("Teclado mecánico", "Ratón gaming")
mayoresingresos2 = tieneMayorIngreso("Auriculares", "Cámara digital")
print(mayoresingresos1)
print(mayoresingresos2)

total = calcularIngresosTotales()
print(total)

assert tieneMayorIngreso("Smartphone", "Auriculares")
assert tieneMayorIngreso("Portátil", "Tablet") == True
assert calcularIngresosTotales() == 612977.4

