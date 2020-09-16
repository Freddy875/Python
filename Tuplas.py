#Tuplas 
#Las tuplas son colecciones de datos
#Parecidos a las listas 
#Solo que las tuplas son inmutables
#Es decir no podemos modificar las tuplas 
#No podemos agregar nuevos elelemntos 
#No podemos eliminar elementos 
#No podemos modificar lo elementos que ya tenemos 

tupla = ()

#Tupla vacia 

#Las tuplas van entre parentesis ()
#Minetras que las listas van entre corchetes []

print(tupla)

tupla = (4,"Hola",6.87,[1,2,3],4,True)

print(tupla)

#Las tuplas al igual que las listas son estructuras
#de datos flexibles que pueden tener diferentes tipos de datos 

#tupla.append(5)
#esto genera un error de compilacion
#ya que las tuplas no tienen el metodo append

#tupla[0] = 8
#esto genera un error de compilacion 
#ya que las tuplas no se pueden modificar
#los elementos que ya tenemos 

#tupla.pop()
#esto genera un erro de compilacion 
#ya que las tuplas no se pueden 
#eliminar lo elelemtos que tenemos 
#además de que las tuplas no tienene 
#el metodo pop 

print(tupla[1])
#Podemos mostrar un solo elemento 
#con el indice 

print(tupla[-3])
#Tambien se pueden mostrar los elementos 
#con un indice negativo 

print(tupla[1:])
#Muestra todos los elementos de la tupla desde la pocicion 1 hasta el final 

#Podemos buscar un elemento en la tupla 

print(4 in tupla)

#Tambien se puede buscar un elemento con el metodo index

print(tupla.index(4))

#Muestra el primer elelemento que encunetra 
#A pesar de que tupla anterior tiene 2 cuatros 

#Se puede hacer la busqueda con el metodo count
# El cual devuelve el total de coincidiencias que encuentra 

print(tupla.count(4))

print(tupla.count(7))
#Si pasamos un valor que no se encuentra en la lista devuelve un cero

#Además podemos usar el metodo len para idnciar cuantos elementos tiene una tupla 

print(len(tupla))

#Podemos conbertir listas a tuplas
#y tuplas a listas 

#Para convertir una tupla en una lista usamos la funcion list 
lista = list(tupla)

print(f"Aqui es una tupla {tupla}")

print(f"Aqui es una lista {lista}")



#Para convertir una lista en una tupla usamos la funcion tuple

lista2 = [4,"Hola",6.87,[1,2,3],4,True]

tupla2 = tuple(lista2)

print(f"Aqui es una lista {lista2}")

print(f"Aqui es una tupla {tupla2}")


