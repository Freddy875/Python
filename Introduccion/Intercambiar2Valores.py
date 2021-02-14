#Intercambiar 2 valores de una variable 

#iNumeroX = int(input("Ingresa el valor de x (entero): "))

#iNumeroY = int(input("Ingresa el valor de y (entero): "))

#iAux = iNumeroX

#iNumeroX = iNumeroY

#iNumeroY = iAux

#print(f"Ahore x vale : {iNumeroX}")

#print(f"Y el valor de y es: {iNumeroY}")

#Otra forma de hacerlo es

iNumeroX = int(input("Ingresa el valor de x (entero): "))

iNumeroY = int(input("Ingresa el valor de y (entero): "))

iNumeroX , iNumeroY = iNumeroY , iNumeroX

print(f"Ahore x vale : {iNumeroX}")

print(f"Y el valor de y es: {iNumeroY}")

#Tambien se puede intercambiar una cadena 

cValorA = input("Ingresa el valor de a (cadena): ")

cValorB = input("Ingresa el valor de b (cadena): ")

cValorA , cValorB = cValorB ,cValorA

print(f"El nuevo valor de a es : {cValorA}")

print(f"El nuevo valor de b es : {cValorB}")
