#Conjuntos 
#Son otro tipo de colleccion 
#Donde los elementos se agregan de forma desordenada
#No puede haber elementos duplicados 

conjunto = set()
#Esto es un conjunto vacio
# Para especificar que un conjunto usamos la palabra clave set
#Los conjuntos y los diccionariso tiene el mismo simbolo 
#Las llaves {} si no le indicamos las llaves entonces seria un diccionario 

#conjunto = {1,2,3,"Hola",4.56,[1,2,3]}
#Esto genera un error de ejecución 
#ya que en un conjunto no puede haber otro tipo de colecciones

conjunto = {1,2,3,"Hola",4.56,1,2,3,"Hola",4.56}

print(conjunto)

#No puede haber elementos duplicados en los conjuntos 
#Esto no genera un error de ejecución
#Sino que no mostrarla los ultimos elementos agregados 
#Ya que estos mismos son ya existen dentro del conjunto
#Solamente guarda una sola vez cada valor dentro del conjunto

#Agregar más elementos a un conjunto    

conjunto.add(5)

print(conjunto)

#Lo logico seria pensar que se agrega al final de los elementos
#Pero en los conjuntos no hay orden asi que el conjunto
#Lo agrega donde el quiera

conjunto.add("Adios")
conjunto.add('a')

print(conjunto)

#Eliminar un elemento de un conjunto 

conjunto.discard(3)

print(conjunto)

conjunto.discard("Hola")

print(conjunto)

#Eliminar todos los elementos del conjunto 
#quedaa un conjunto vacio 

conjunto.clear()

print(conjunto)

#Buscar un determinado elementos del conjunto 

print(3 in conjunto)

#Devuleve un valor de tipo boolean (True/False)
#Como limpiamos todo el conjunto entonces devuleve False

conjunto = {1,2,3,"Hola",4.56}

#Aqui volvemos a llenar el conjunto 
#En este caso si devulve un true 

print(4.56 in conjunto)

#Tambien se puede usar el not in para saber si un valor valor no se encuntre dentro del conjunto

print(3  not in conjunto)

#En este caso devuelve false porque 3 si forma parte del conjunto

print(11 not in conjunto)

#En este caso devuelve true porque el 11 NO forma parte del conjunto

# Anteriormente mencionamos que un connunto vacio se declara con la palabra set
# Ya que de no hacerlo asi seria un diccionario
# En caso de no declarar un conjunto vacio y declarar el conjunto con elementos 
# en su interior entonces ya no es necasrio declarar el conjunto vacio

conjuntoA = {1,2,3}

conjuntoB = {3,4,5}

#Igualdad de dos conjuntos 

print(conjuntoA == conjuntoB)

#Devuelve un valor de tipo boolean en este caso un false 

conjuntoB = {3,2,1}
#Volvemos a declarar el conjunto b pero con los mismos elementos 
#del conjuntoA solo que en otro orden 

print(conjuntoA == conjuntoB)
#En este caso devolvera un true 
#porque sin importar el orden 

#Saber cuantos elementos tiene un conjunto 

print(len(conjuntoA))

#Union de dos conjuntos 

#A diferencia de la listas y las tuplas no se puede sumar dos conjuntos 
#para mostrar su union
# Esto causar un error de ejecucion  

#conjuntoC = conjuntoA + conjuntoB

#print(conjuntoC)

conjuntoA = {1,2,3}

conjuntoB = {3,4,5}

conjuntoC = conjuntoA | conjuntoB

print(conjuntoC)

#Como en los conjuntos no puede haber valores duplicados solo se muestra el 3 una vez 

#Interseccion de dos conjuntos

conjuntoC = conjuntoA & conjuntoB

print(conjuntoC)

#El resultado sera 3 
# Ya que en una interseccion solo se muestra 
# los elementos que existen en ambos conjuntos

#Diferencia de conjuntos 
#Muestra los elementos en A que no estan en B

conjuntoC = conjuntoA - conjuntoB

print(conjuntoC)

conjuntoC = conjuntoB - conjuntoA

print(conjuntoC)

#Diferencia simetrica de conjuntos 

#elementos que estan en A y en B pero no estan en ambos 

conjuntoC = conjuntoA ^ conjuntoB

print(conjuntoC)

#Determinar si un conjunto es un subconjunto de otro
#es decir que un conjunto esta dentro de otro

conjuntoC = {1,2,3,4,5}

print(conjuntoA.issubset(conjuntoC))
#Devuelve un valor de tipo Boolean

print(conjuntoB.issubset(conjuntoC))

#Determinar si un conjunto es un superconjunto de otro

print(conjuntoC.issuperset(conjuntoA))

print(conjuntoC.issuperset(conjuntoB))

#Saber si dos conjuntos son disconexos
#Es decir que no comparten ningun elemento en comun 

print(conjuntoA.isdisjoint(conjuntoB))
#Es este caso devulve un false ya que si comparten un elemento 
#que es el 3

#Conjunto inmutable

conjuntoD = frozenset({1,2,7})

#conjuntoD.add(5)

#print(conjuntoD)

#Esto genera un error de ejecucion ya que al ser un conjunto 
#inmutable entonces no se pueden agregar ni modificar 
#los elementos del conjunto 




