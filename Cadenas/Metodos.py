#Convierte el primer caracter a mayuscula
texto = "hola, y  bienvenido a mi mundo."
x = texto.capitalize()
print(x)

texto = "24 anios es mi edad"
x = texto.capitalize()
print(x)

#Convierte la cadena a minusculas
texto = "Hola, Y Bienvenido A Mi Mundo."
x = texto.casefold()
print(x)

#Centra la cadena
texto = "bananas"
x = texto.center(20)
print(x)

texto = "bananas"
x = texto.center(20,"O")
print(x)

#Devuelve el numero de veces que un valor especifico aparece en la cadena
texto = "Me encentan las manzanas, las manzanas son mi fruta favorita"
x = texto.count("manzanas")
print(x)

texto = "Me encentan las manzanas, las manzanas son mi fruta favorita"
x = texto.count("manzanas",10,24)
print(x)

#Devuevle una version codificada de la cadena
texto = "Mi nombre es Fernando Sánchez Mejía"
x = texto.encode()
print(x)

print(texto.encode(encoding="ascii",errors="backslashreplace"))
print(texto.encode(encoding="ascii",errors="ignore"))
print(texto.encode(encoding="ascii",errors="namereplace"))
print(texto.encode(encoding="ascii",errors="replace"))
print(texto.encode(encoding="ascii",errors="xmlcharrefreplace"))

texto = "Fernando S\xc3\xa1nchez Mej\xc3\xada"
print(texto)

#Devuelve verdadero si una cadena termina con un especifico valor 

texto = "Hola, Bienvenido a mi mundo."
print(texto)
x = texto.endswith(".")
print(x)

texto = "Hola, Bienvenido a mi mundo."
x = texto.endswith("mi mundo.")
print(x)

texto = "Hola, Bienvenido a mi mundo."
x = texto.endswith("mi mundo.",5,11)
print(x)

#Establece el tamaño de pestaña de la cadena 
texto = "H\te\tl\tl\to"
print(texto)
print(texto.expandtabs())
print(texto.expandtabs(2))
print(texto.expandtabs(4))
print(texto.expandtabs(10))

#Buscar la cadena de un valor especifico y devuelve la pocision donde lo encontro
#Encontrar la palabra bienvenido

texto = "Hola, Bienvenido a mi mundo"
x = texto.find("Bienvenido")
print(x)

#Encontrar la primera letra e
texto = "Hola, Bienvenido a mi mundo"
x = texto.find("e")
print(x)

#Encontrar encontrar una letra entre un rango de valores
texto = "Hola, Bienvenido a mi mundo"
x = texto.find("e",9,12)
print(x)

#Cuando el valor no es contrado devulve un -1
texto = "Hola, Bienvenido a mi mundo"
x = texto.find("q")
print(x)

#Formate un valor especifico en una cadena

texto = "Por solo {precio:.2f} pesos"
print(texto.format(precio = 49.50))

#Indice con nombre:
texto = "Mi nombre es {fname}, Tengo {edad} anios".format(fname = "Freddy", edad=24)
print(texto)
#Indice numerado:
texto = "Mi nombre es {0}, Tengo {1} anios".format("Freddy",24)
print(texto)
#Marcadores de posicion vacios:
texto = "Mi nombre es {}, Tengo {} anios".format("Freddy",24)
print(texto)













