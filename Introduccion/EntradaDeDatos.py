#Entrada de datos 

nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}")

numero = input("\nIngresa un numero: ")

#El input guarda datos de tipo cadena 

print(f"El numero es: {numero}")

#numero = input("\nIngresa un numero: ")
#print(f"El numero es: {numero+1}")
#La sentencia anterior marcara un error porque no se puede sumar 
#Un string con un int 

numero = int(input("\nIngresa otro un numero: "))
print(f"A tu numero se le sumo uno y ahore el numero es: {numero+1}")

numero = float(input("\Ingreso otro numero (flotante): "))
print(f"Tu numero es: {numero}")