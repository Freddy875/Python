'''
Existen 3 tipos numeircos en Python
int
float
complex
'''

x =1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#Enteros

print("Enteros")

'''
Los entrsos son todo numero positivo
o negativo sin decimales 
de longitud indefinida
'''

x = 1
y = 123456789
z = -987654321

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#Flotantes o reales
'''
Numeros con punto flotante 
es un numero positivo o negativo 
contien uno o mas decimales
'''
print("Flotantes o reales")

x = 1.10
y = 1.0
z = -35.59
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

'''
Los flotantes tambien puede ser expresado
en notación cientifica con la letra "e"
para indicar la potencia de 10
'''

x = 35e3
y = 12e4
z = -87.7e100
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#Complejos

print("Complejos")
'''
Los complejos son escritos con 
la letra "j" para indicar 
la parte imaginaria
'''

x = 3+5j
y = 5j
z = -5j
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#Conversiones

print("Conversiones")
'''
Convertir un tipo de dato a otro
'''

#Convertir de entero a flotante:
x = float(1)

#Convertir de flotante a entero:
y = int(2.8)

#Convertir de entero a complejo
z = complex(x)

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#Numero random o aleatorio

print("Numero aleatorio del 1 al 10")

import random

print(random.randrange(1,10))

print("Numero aleatorio del 1 al 100")

print(random.randrange(1,100))