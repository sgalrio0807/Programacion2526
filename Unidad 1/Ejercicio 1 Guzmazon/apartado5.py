nummax = float(input("Introduce el dinero maximo que se quiere gastar en la compra: "))
productos = input("Introduce un producto: ").lower()
precio = float(input("Introduce el precio del producto: "))
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

print("S para dinero sobrante")
print("R para eliminar producto")
print("c para lista de producto ccuyo precio es mas alto del importe")
opcion = input("Introduce una opción: ").lower()

if opcion == "s":
    resta = (nummax - sumaprecios)
    print("La resta entre numero maximo a gastar y suma de los precios es", resta)
    
elif opcion == "r":
    productos = input("Introduce un producto: ").lower()
    print(listaproductos,",",listaprecios)
    seguro= input("Estas seguro/a(S/N):").lower()
    if seguro == "s":
            listaproductos.remove(productos)
            print(listaproductos)
            
elif opcion == "c":
     importe = float(input("Introduce importe: "))
     if listaprecios > importe:
        listaimporte.append(productos)
        print(listaimporte)
   