nummax = float(input("Introduce el dinero maximo que se quiere gastar en la compra: "))
productos = input("Introduce un producto: ").lower()
precio = float(input("Introduce el precio del producto: "))
def cargacesta(nummax):
    listaproductos = []
    listaprecios = []
    listaimporte = []
    sumaprecios = 0

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

#pedir_productosyprecios
#almacenar_listas
#carga_cesta
#calcular_coste_total
#mostar_resumen

