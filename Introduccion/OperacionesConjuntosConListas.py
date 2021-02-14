'''
Crear dos listas 
En las que no debe de haber repeticiones 
y mostrar 

-Lista de elementos que aparecen en dos listas 
-Lista de elementos que aparecen en la primera, pero no en la segunda
-Lista de elementos que aparecen en la segunda, pero no en la primera 
-Lista de elementos que aparecen en ambas listas 
'''

lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

#Eliminar los elementos repetidos de ambas listas 
#Primero creamos dos variables para que guarden
#los valores de las listas pero estas varaibles
#seran conjuntos para evitar los elementos repetidos

conjuntoA = set(lista1)
conjuntoB = set(lista2)

#Usamos la propiedad de union de los conjuntos 
#Para eso creamos una variable llamada union
#Y volvamos a convertir ambos conjuntos a valores

union = list(conjuntoA | conjuntoB)

#Para conocer los elementos que estan solo en A 
#pero no en B usamos la propiedad de diferencia 
#de los conjuntos y los guardamos en una variable
#llamada soloA

solaA = list(conjuntoA - conjuntoB)

#Hacemos lo mismo para conocer los elementos que estan
#solo en B pero no en A
#Para eso tenemos otra variable 
#llamada soloB

soloB = list(conjuntoB - conjuntoA)

#Y para conocer lo elementos que aparecen en ambas listas
#Usamos la pripiedad de interseccion de los conjuntos 
#en una variable del mismo nombre 

interseccion = list(conjuntoA & conjuntoB)

print(f"Los elementos de la lista 1 son: {lista1}")
print(f"Los elementos de la lista 2 son: {lista2}")
print(f"Los elementos que aparecene en ambas listas son: {union}")
print(f"Los elementos que aparecen en la primera lista",
f"pero no en la segunda son: {solaA}")
print(f"Los elementos que aparecen en la segunda lista",
f"pero no en la primera son: {soloB}")
print(f"Los elementos que aparecen en ambas listas son: {interseccion}")


