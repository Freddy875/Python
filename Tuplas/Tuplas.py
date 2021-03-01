'''
Tuplas son utilizadas para alamacenar multiples
elementos en una sola variable
Las tuplas son colecciones de datos los cuales estan 
ordenados y no son cambianles
'''

estaTupla = ("manzana","banana","cereza")
print(estaTupla)

'''
Los elementos de la tuplas estan ordenadas, 
no son cambianles y permiten duplicar valores
Los elementos en la tupla estan indexados
El primer indice tiene el elemento [0]
el segundo[1], etc.
'''

'''
Ordenada significa que los elementos tiene un definido orden 
y que el orden no cambiara
'''

'''
No cambiable significa que no podemos cambiar, agregar o remover 
elementos despues que la tupla ha sido creada
'''

print("Valores duplicados de una tupla")
estaTupla = ("manzana","banana","cereza","manzana","cereza")
print(estaTupla)

#Longitud de la tupla
print("Longitud de una tupla")
estaTupla = ("manzana","banana","cereza")
print(len(estaTupla))

#Crear una tupla con una solo elementos
estaTupla = ("manzana",)
print(type(estaTupla))

#NO es una tupla
estaTupla = ("manzana")
print(type(estaTupla))

#Elementos de la tupla - Tipos de datos

print("Elementos de la tupla - Tipos de datos")

tupla1 = ("manzana","banana","cereza")
tupla2 = (1,5,7,9,3)
tupla3 = (True,False,True,False)

print(tupla1)
print(tupla2)
print(tupla3)

#Una tupla puede contener diferentes tipos de datos

tupla1 = ("abc",34,True,40,"male")
print(tupla1)

miTupla = ("manzana","banana","cereza")
print(type(miTupla))

#Construir una tupla
estaTupla = ("manzana","banana","cereza")
print(estaTupla)



