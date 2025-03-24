"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""

###

def suma(num1, num2):
    try:
        resultado = num1 + num2
    except:
        print("Error inesperado")
    else:
        print(resultado)

###

"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""

###

def cociente(num1,num2):
        
    print(num1/num2)
    
#MENSAJE EN PANTALLA
def cociente(num1, num2):
    try:
        resultado = num1 / num2
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
    else:
        print(resultado)

###

"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.

"""


def abrir_archivo(nombre_archivo):
    archivo = open(nombre_archivo)


def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

###

###
def generador_infinito():
    n = 1
    while True:
        yield n
        n += 1

generador = generador_infinito()
###

###
def generador_multiplos_de_7():
    n = 7
    while True:
        yield n
        n += 7

generador = generador_multiplos_de_7()
###

def generador_vidas():
    vidas = 3
    while vidas > 0:
        yield f"Te quedan {vidas} vidas" if vidas > 1 else "Te queda 1 vida"
        vidas -= 1
    yield "Game Over"

perder_vida = generador_vidas()
