#Diccionarios 

#Son otro tipo de coleccion 
# donde los elementos tambien se guardan desordenados
# Tienen dos elementos por posicion 
# La clave y el valor 
# La clave no puede estar duplicada 

diccionario = {}

#Esto es un diccionario vacio  

print(diccionario)

#Agregar valores a un diccionario 

diccionario = {"azul":"blue","rojo":"red","verde":"green"}

#En este caso azul es la clave y blue es el valor
# Separao  por dos puntos

print(diccionario)


#Solo mostrar cierto elemento del diccionario con la clave

print(diccionario["azul"])

print(diccionario["rojo"])

#Agregar nuevos elementos al diccinoario

diccionario["amarillo"] = "yellow"

print(diccionario)

#Modificar elementos del diccionario

diccionario["azul"] = "BLUE"

#en este caso cambia todas las letras por mayusculas 

print(diccionario)

#Eliminar un elemento del diccionario 

del(diccionario["verde"])

print(diccionario)

#Al eliminar una clave automaticamente se elimina el valor que este tiene 

#Los diccionario pueden aceptar diferentes tipos de datos
#Como enteros, reales, y otras colecciones 
#como listas, tuplas e inclusive otros diccionarios 

agenda = {"Freddy":[23,1.68],"Jose":[21,1.75],"Maria":[22,1.67]}

print(agenda)

#diccionario dentro de otro diccionario

agenda = {"Freddy":{"eada":23,"estatura":1.68},"Jose":[21,1.75],"Maria":[22,1.67]}

print(agenda)

print(agenda["Freddy"])

print(agenda["Maria"])

heroe = {1:"Deadpool",2: "Iron Man",3:"Capitan America"}
#La clave y el valor pueden ser de diferentes tipos de datos 

print(heroe)

print(heroe[1])

#print(equipo[7])
#Si se pasa una clave que no existe 
#entonces generara un error de ejecución 

#Para evitar este error se puede evitar con el metodo get

print(heroe.get(7,"No existe un heroe con ese valor"))

#Buscar un elemento dentro de un diccionario 

print(10 in heroe)

# Mostrar todas las claves del diccionario 

print(heroe.keys())

# Mostrar solo los valores del diccionario 

print(heroe.values())

#Mostrar ambos elelementos 

print(heroe.items())

#Mostrar cuantos elementos tiene el diccionario

print(len(heroe))

#Limpiar todos los elementos del diccionario 

heroe.clear()

print(heroe)