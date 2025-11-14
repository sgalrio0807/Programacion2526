nummax = float(input("Introduce el dinero maximo que se quiere gastar en la compra: "))
productos = input("Introduce un producto: ").lower()
precio = float(input("Introduce el precio del producto: "))

listaproductos = []
listaprecios = []
listaimporte = []
sumaprecios = 0

def cargacesta(nummax):

    while sumaprecios <= nummax:
        listaprecios.append(precio)
        listaproductos.append(productos)
        productos = input("Introduce un producto: ").lower()
        precio = float(input("Introduce el precio del producto: "))
        sumaprecios += precio

    print("Importe máximo a gastar:", nummax )
    print("Productos:", listaproductos)
    print("Precios:", listaprecios)
    print("Coste total de la cesta", sumaprecios)
    return productos, precios, costetotal

resultados = cargacesta(nummax)
productos = resultados[0]
precios = resultados[1]
costetotal = resultados[2]

def pintamenu():
    print("S para dinero sobrante")
    print("R para eliminar producto")
    print("c para lista de producto ccuyo precio es mas alto del importe")
    opcion = input("Introduce una opción: ").lower()

    if opcion == "s":
        print("Sobrante")
    elif opcion == "r":
        print("Remove")
    elif opcion == "c":
        print("Productos caros")
    return pintamenu

resultado = pintamenu()

def sobrante():
    resta = (nummax - sumaprecios)
    print("La resta entre numero maximo a gastar y suma de los precios es", resta)
    return resta

def eliminarproducto():
    productos = input("Introduce un producto: ").lower()
    print(listaproductos,",",listaprecios)
    seguro= input("Estas seguro/a(S/N):").lower()
    if seguro == "s":
            listaproductos.remove(productos)
    return listaproductos

def productoscaros():
    importe = float(input("Introduce importe: "))
    if listaprecios > importe:
        listaimporte.append(productos)
    return listaimporte

#pedir_productosyprecios
#almacenar_listas
#carga_cesta
#calcular_coste_total
#mostar_resumen

