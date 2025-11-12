nummax = float(input("Introduce el dinero maximo que se quiere gastar en la compra: "))
productos = input("Introduce un producto: ").lower()
precio = float(input("Introduce el precio del producto: "))
listaproductos = []
listaprecios = []
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





