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

