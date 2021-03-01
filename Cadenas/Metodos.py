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

#Index
'''
Busca una cadena de un especifico valor y devuelve 
la posición de donde encontrarlo
'''

texto = "Hola, Bienvenido a mi mundo"

x = texto.index("Bienvenido")

print(x)

#Encontrar la primera e

texto = "Hola, Bienvenido a mi mundo"

x = texto.index("e")

print(x)

#Entre un rango

texto = "Hola, Bienvenido a mi mundo"

x = texto.index("e",5,10)

print(x)

'''
Si el valor no es encontrado, el metodo find()
devuelve un -1 pero con un metodo index()
devuelve una excepcion
'''
texto = "Hola, Bienvenido a mi mundo"

print(texto.find("q"))
#print(texto.index("q"))

#isalnum() Devuelve True si todos los caracteres en la cadena son alfanumericos

#Primer ejemplo es True

texto = "CompanyX"

x = texto.isalnum()

print(x)

#Segundo ejemplo es False

texto = "Company10"

x = texto.isalnum()

print(x)

#sialpha

'''
Devuelve true si todos los caracteres en la cadena son alfabeticos
'''

#Primer ejemplo es True

texto = "CompanyX"

x = texto.isalpha()

print(x)

#Segundo ejemplo es False

texto = "Company10"

x = texto.isalpha()

print(x)

#isdecilam 

'''
Devuelve True si todos los caracteres en la cadena son decimales
'''

texto = "\u0033" #Unicode for 3

x = texto.isdecimal()

print(x)

a = "\u0030" #unicode para 0
b = "\u0047" #unicdoe para G

print(a.isdecimal())
print(b.isdecimal())

#isdigit()

'''
Devuelve True si todos los caracteres en la cadena son decimales
'''
texto = "50800" #Unicode for 3

x = texto.isdigit()

print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())

#isdentifier

'''
Devuelve True si la cadena es un identificador
Una cadena es conciderada un identificador valido
si solo contiene letras alfanumericas (a-z) y (0-9),
o guiones bajo (_).
Un identificador valido no puede comenzar con un numero
ni conteenr espacios 
'''

texto = "Demo"

x = texto.isidentifier()

print(x)

a = "MiCarpeta"
b = "Demo002"
c = "2Traer"
d = "mi demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

#islower
'''
Devuelve True si todos los caracteres
en la cadena esta en minusculas
'''

texto = "hola mundo"

x = texto.islower()

print("Es minuscula")

print(x)

a = "Hola mundo"
b = "hola 123"
c = "minombre_esFreddy"

print(a.islower())
print(b.islower())
print(c.islower())

#isnumeric

'''
Devuelve True si todos los caracteres en la cadena son numericos
'''

print("Es numerico")

texto = "565543"

x = texto.isnumeric()

print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())

#isprintable

'''
Devuelve True si todos los caracteres en la cadena son imprimibles
'''

texto = "!Hola¡ ¿Tu eres el #1?"

x = texto.isprintable()

print("Es imprimible")

print(x)

texto = "!Hola¡\n ¿Tu eres el #1?"

x = texto.isprintable()

print(x)

#isspace

'''
Devuelve True si todos los caracteres en la cadena son espacios en blanco
'''

texto = "   "

x = texto.isspace()

print("Es un espacio en blanco")

print(x)

texto = "  s  "

x = texto.isspace()

print(x)

#istitle

'''
Devuelve true si la cadena sigue las reglas de un titulo
es decir si las primera letra de la cadena inicia con
mayuscula y todas las demas con minusculas
'''

print("Es un titulo")

texto = "Hola, A Bienvenido A Mi Mundo"

x = texto.istitle()

print(x)

a = "HOLA, Y BIENVENIDO A MI MUNDO"
b = "Hola"
c = "22 Nombres"
d = "Esto es %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

#isupper

'''
Devuelve True si todos los caracteres en la cadena son mayusculas
'''

print("Es mayuscula")

texto = "ESTO ES AHORA"

x = texto.isupper()

print(x)

a = "Hola Mundo"
b = "hola 123"
c = "MI NOMBRE ES FREDDY"

print(a.isupper())
print(b.isupper())
print(c.isupper())

#Join 

'''
Unir elementos de un iterable al fin de una cadena
'''

print("Join")

miTupla = ("John","Peter","Vicky")

x = "#".join(miTupla)

print(x)

myDict = {"name":"John","country":"Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

#ljust

'''
Devuelve la cadena justificada a la derecha
'''

print("ljust")

texto = "El mango"

x = texto.ljust(20)

print(x,"es mi fruta favorita")

texto = "El mango"

x = texto.ljust(20,"O")

print(x,"es mi fruta favorita")

#lower

print("minusculas")

#Convierte una cadena en minusculas

texto = "Hola mis AMIGOS"

x = texto.lower()

print(x)

#lstrip

#Devuelve una versión recortada a la izquierda de la cadena.

texto = "   mango   "

x = texto.lstrip()

print("De todas las furta el " , x, "es mi fruta favorita")

texto = ",,,,,ssaaww.....banana"

x = texto.lstrip(",.saw")

print(x)

#maketrnas()

#Devuelve una tabla de traducción que se utilizará en las traducciones.

print("maketrans")

texto = "Hola, Sam"

miTabla = texto.maketrans("S","P")

print(texto.translate(miTabla))

texto = "Hola, Sam"

x = "mSa"
y = "eJo"

miTabla = texto.maketrans(x,y)

print(texto.translate(miTabla))

texto = "Buenas noches, Sam"

x = "mSa"
y = "eJo"
z = "noches"

print(texto.maketrans(x,y,z))

#Particion 

#Devuelve una tupla donde la cadena se divide en tres partes

texto = "Yo podria comer mango todo el dia"

x = texto.partition("mango")

print(x)

texto = "Yo podria comer mango todo el dia"

x = texto.partition("manzana")

print(x)



















