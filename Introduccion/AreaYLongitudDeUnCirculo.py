#Ingresar el radio de un circulo 
#y reportar su area y la longitud 
#de la circuenferencia 

#print("Este programa te dice la longitud y area de un ciruclo")

#fRadio = float(input("Ingresa el radio del circulo: "))

#PI = 3.1416

#Declaramos el valor de PI co

#fArea = PI * (fRadio**2)

#fLongitud = 2 * PI * fRadio

#print(f"El area del circulo es: {fArea} \nY la longitud del criculo es: {fLongitud}")

#Otra forma de hacer es

import math

print("Este programa te dice la longitud y area de un ciruclo")

fRadio = float(input("Ingresa el radio del circulo: "))

fArea = math.pi * (fRadio**2)

fLongitud = 2 * math.pi * fRadio

print(f"El area del circulo es: {fArea:.2f}",
f"\nY la longitud del criculo es: {fLongitud:.2f}")


