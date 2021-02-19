edad = 24
texto = "Mi nombre es Freddy, y tengo {} anios"
print(texto.format(edad))

cantidad = 3
NumArticulo = 567 #NumArticulo es Numero del articulo como su ID
precio = 49.95
miOrden = "Quiero {} piezas de articulo {} por {} pesos."
print(miOrden.format(cantidad,NumArticulo,precio))

#Tambien se puede indexar
cantidad = 3
NumArticulo = 567 #NumArticulo es Numero del articulo como su ID
precio = 49.95
miOrden = "Quiero pagar {2} pesos for {0} piezas del articulo {1}"
print(miOrden.format(cantidad,NumArticulo,precio))

