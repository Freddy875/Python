'''
Listas 
Son parecidad a los arreglos o vectores
Estructuras de datos mas flexibles
Podemos almacenamos 
valores numericos, cadenas, bolleanos 
e inclusive otroas listas
'''

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes"]

print(lista)

print(lista[0])

print(lista[2])

#En python podemos ingresar a las listas de adelante para atras
#o desde atras para adelante 

print(lista[-1])

print(lista[-4])

#print(list[7])
#ERROR el elemento anterior no es posible acceder porque excede los valores de la lista 

print(lista[0:3])

#Podemos acceder a sublistas
#Siempre accede a un valor antes porque las listas empiezan en cero 

print(lista[:4])
#Si no ingresamos el inicio de la lista empieza desde la pocicion 0 hasta la que le indicamos 

print(lista[1:4])
#Podemos acceder a una sublista desde donde nosotros querramos

print(lista[2:])
#en este caso imprime el valor desde donde le indicamos hasta el fin de la lista 

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",40,5.67,[1,2,3],True]

print(lista)

#una lista es una estructura de datos muy flexible 

print((f"La lista 1 tiene {len(lista)} elementos"))

#La sentencia len se usa para conocer la cantidad de elementos de un elemento

lista2 = [1,2,3,4,5]

print((f"La lista 2 tiene {len(lista2)} elementos"))

lista2.append(6)

#La sentencia anterior le agregamos un nuevo elemento con la funcion append
#La funcion append agrega un elemento al final de la lista 

print(lista2)

lista2.append("Freddy")

print(lista2)

#Como en python las listas son estructuras de datos tambien podemos agregar una cadena 

lista3 = [1,2,4,5]

print(lista3)

lista3.insert(2,3)

#Insrt es para agregar un elemento desde cualquier puento de la lista 
#El primer parametro de la funcion representa la posicion del indice donde
#queremos agregar y el segundo parametro es el numero que queremos agregar

print(lista3)

#Para agregar variaos elementos a la lista usamos el metodo extend

lista4 = [1,2,3,4,5]

lista4.extend([6,7,8])

print(lista4)

#Podemos sumar dos listas 

lista5 = [1,2,3,4,5]
lista6 = [6,7,8]

lista7 = lista5 + lista6

print(lista7)

#Buscar un determinado elemento en la lista 
#Si el elemento se encuentra en la lista 
# devuelve un True si no esta en la lista 
# entonces devueve un false  

lista8 = [1,2,3,4,5,"Freddy"]

print(3 in lista8)

print(10 in lista8)

#Conocer el indice en el que se encuentra cierto elemento 
#con el metodo index

print(lista8.index(5))

#print(lista8.index(10))
#Si devuleve un valor que no existe en la lista 
#genera un error de excepcion 


#Una lista puede tener elementos repetidos 

lista9 = [1,2,3,4,5,"Freddy",1,2,3,4,5,"Freddy"]

#Para saber cuantos elementos repedidos se puede tener en una 
#lista se usa el metodo count 

print(lista9.count(1))

#Si pasamos un valor que no se encuentra en la lista devuelve un cero

print(lista9.count(10))

#Eliminar elelementos de la lista 

lista10 = [1,2,3,4,5,"Freddy"]

print(lista10)

#Para eliminar un elemento se usa pop

lista10.pop()

#Si pasamos un pop sin nada en el parentesis 
#Entonces elimina el ultimo elemento 

print(lista10)


#Tambien se puede pasar un parametro en pop 
#le indicamos el indice del elelemento que queremos eliminar 

lista10.pop(3)

print(lista10)

#Para eliminar un elemento de la lista sin conocer su 
#indice su utiliza el metodo remove
# Con el remove solo pasamos el elemento que queremos eliminar  

lista10.remove(5)

print(lista10)

#Se pueden eliminar todos lo elementos de la lista 
#Para eso con el metodo clear

lista10.clear()

print(lista10)

#Se puede voltaer los lelementos de la lista
#Es decir que el primero esta en la ultima pocision 

lista11 = [1,2,3,4,5]

lista11.reverse()

print(lista11)

#Si queremos copiar los elementos de una lista 
#Al final ponemos el simbolo de multiplicar (*)
#Y la cantidad por la que querremos que se multipliquen 

lista12 = [1,2,3,4,5,"Freddy"]*2

print(lista12)

#En este caso copia los elementos de la lista en el mismo orden 

#Ordenar los elementos de la lista 

lista12 = [5,4,-7,9,0,1,3]

#Con el metodo sort podemos ordenar los elementos de manera ascendnete 

lista12.sort()

print(lista12)

#Aunque tambine se puede ordenar los elemen tos de manera descendente 
#Dentor del metodo sort colocamos reverse = True 

lista12.sort(reverse=True)

print(lista12)

