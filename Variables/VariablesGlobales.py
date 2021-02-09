'''
Las variables que se crean fuera de la 
funcion se conocen como variables globales
'''

x = "asombros"

def miFuncion():
    print("Python es " + x)

miFuncion()

'''
Si crea una variable con el mismo nombre dentro de una funcion,
la variable sera local y solo se puede usar dentro de la 
funcion.
La variable global con el mismo nombre permanecera como estaba, 
globar y con el valor original 
'''

x = "asombroso"

def miFuncion():
    x = "fantastico"
    print("Python es " + x)

miFuncion()

print("Python es " + x)


'''
La palabra clave global
Cuando se crea una variable dentro de una funcion,
esa variable es local; es decir solo se puede usar 
dentro de esa funcion.
Para crear una variable global dentro de una funcion
se puede usar la palabra clave global
'''

def miFuncion():
    global x
    x = "fantastico"

miFuncion()

print("Python es " + x)


'''
Tambien se puede usar la palabra clave global 
si se desea cambiar una variable global dentro
de una funcion 
'''

x = "asombroso"

def miFuncion():
    global x
    x = "fantastico"

miFuncion()

print("Python es " + x)
