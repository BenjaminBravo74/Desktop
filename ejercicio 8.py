nombreproducto=input("ingrese el nombre del producto: ")
preciounitario=float(input("ingrese el valor: "))
cantidadcomprada=float(input("ingrese la cantidad comprada: "))
preciototal=preciounitario*cantidadcomprada
descuento= 5*preciototal/100
preciofinal= preciototal-descuento
print("elprecio total es ",preciototal,"\n", "el descuento es ",descuento,"\n","el precio final es de ",preciofinal)