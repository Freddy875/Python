'''
Una tienda ofrece un dexcuento del 15% sobre el total de compra y un 
cliente desea saber cuánto deberá pagar finalmente por su compra 
'''

fPrecio = float(input("Ingrese el precio: "))

fDescuento = fPrecio * 0.15

fPrecioFinal = fPrecio - fDescuento

print(f"El precio final a pagar es de ${fPrecioFinal:.2f}")