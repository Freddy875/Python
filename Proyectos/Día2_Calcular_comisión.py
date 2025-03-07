# Programa para calcular la comisión de un vendedor

# Solicitar datos al usuario
nombre = input("Por favor, ingresa tu nombre: ")
ventas = float(input("Ingresa el monto total de tus ventas este mes: "))

# Calcular la comisión (13% de las ventas)
comision = (ventas * 13) / 100

# Imprimir el resultado con dos decimales
print(f"\nHola, {nombre}. Tu comisión de este mes es: ${comision:.2f}")

