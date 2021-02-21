#Los booleans representa dos valores: True o False 
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

#Con un if

a = 300
b = 220

if b > a:
    print( f"{b} es mayor que {a}")
else:
    print(f"{a} es mayor que {b}")

print(bool("Hola"))
print(bool(15))

x = "Hola"
y = 15

print(bool(x))
print(bool(y))

'''
Mayoria de los valores son True
Si tienen algun tipo de valor 
Cualquier cadena es True, excepto cadenas vacias
Cualquier numero es True, excepto 0
Cualquier lista,tupla,conjunto y diccionario son True, excepto los vacios
'''
print(bool("abc"))
print(bool(123))
print(bool(["manzana, cereza, platano"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

'''
Un objeto se evalua como false si tiene un objeto 
que esta hecho de una clase con _len_
funcion que devuelve 0 o false
'''

class miClase():
    def __len__(self):
        return 0

miObjeto = miClase()
print(bool(miObjeto))

#Las funciones pueden vevolver un valor booleano

def miFuncion():
    return True

print(miFuncion())

def miFuncion():
    return True

if miFuncion():
    print("SI")
else:
    print("NO")

'''
Pytho tiene muchas funciones integradas que devuelve un valor booleano
como la isinstance() funcion que se puede user para determinar si un 
objeto es del determinado tipos de datos 
'''

x = 200

print(isinstance(x,int))
