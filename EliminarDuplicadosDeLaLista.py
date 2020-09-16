#Eliminar los elementos repetidos de una lista 

lista=[1,2,3,"Freddy",2,2,1,"Freddy",3]


print(f"La lista original {lista}")

#Primero convertimos la lista a un conjunto 

conjunto = set(lista)

#Luego volvemos a convertir nuevamente el conjunto a una lista 

lista = list(conjunto)

print(f"La lista sin elementos repetidos {lista}")

#Otra forma de hacerlo en una sola linea es 

lista=[1,2,3,"Freddy",2,2,1,"Freddy",3]

print(f"La lista original {lista}")

lista = list(set(lista))

print(f"La lista sin elementos repetidos {lista}")
