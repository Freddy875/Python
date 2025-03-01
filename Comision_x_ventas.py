"""
Elabora un programa para calcular las comisiones del 13% por ventas, preguntando el nombre y cuanto han vendido, respondiendo con el nombre y el monto que corresponde por las comisiones 
"""

# Solicitar el nombre del vendedor
nombre = input("Ingrese su nombre: ")

# Solicitar el monto de ventas y convertirlo a número
ventas = float(input("Ingrese el monto total de sus ventas: "))

# Calcular la comisión (13% de las ventas)
comision = ventas * 0.13

# Mostrar el resultado
print(f"\nHola {nombre}, tu comisión es de ${comision:.2f} por tus ventas de ${ventas:.2f}.")
