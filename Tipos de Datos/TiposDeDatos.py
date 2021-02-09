'''
En la programaión los tipos 
de datos son un concepto importante
Las variables pueden almacenar diferentes
tipos de datos, y los diferentes tipos 
pueden hacer diferentes cosas
Python tiene los siguientes tipos
de datos por default en las
siguientes categorias 
Tipos Texto: str
Tipos numericos: int, float, complex
Tipos Secuencia: list, tuple, range
Tipos de mapeo: dict
Tipos set o conjuntos: set, frozenset
Tipos booleanos: Bool
Tipos binarios: Bytes, bytearray, memoryview
'''

'''
Se puede obtener el tipo de dato 
de cualquier objeto con la función type
'''

cadena = "Hola Mundo"
print(cadena)
print(type(cadena))
entero = 5
print(entero)
print(type(entero))
real = 20.5
print(real)
print(type(real))
complejo = 1j
print(complejo)
print(type(complejo))
lista = ["Manzana","Platano","Cereza"]
print(lista)
print(type(lista))
tupla = ("Manzana","Platano","Cereza")
print(tupla)
print(type(tupla))
rango = range(6)
print(rango)
print(type(rango))
dictado = {"Nombre":"Freddy","Edad":24}
print(dictado)
print(type(dictado))
conjunto = {"Manzana","Platano","Cereza"}
print(conjunto)
print(type(conjunto))
FrutaFria = frozenset({"Manzana","Platano","Cereza"})
#Esta variable se llama FrutaFria proque es de tipo frozenset y todas son frutas
print(FrutaFria)
print(type(FrutaFria))
Booleano = True
print(Booleano)
print(type(Booleano))
bit=b"Hello"
print(bit)
print(type(bit))
arreglo = bytearray(5)
print(arreglo)
print(type(arreglo))
memoria = memoryview(bytes(5))
print(memoria)
print(type(memoria))

'''
Configuracion de tipo de dato exacto
'''
print("Configuracion de tipo de dato exacto")
cadena = str("Hola Mundo")
print(cadena)
print(type(cadena))
entero = int(5)
print(entero)
print(type(entero))
real = float(20.5)
print(real)
print(type(real))
complejo = complex(1j)
print(complejo)
print(type(complejo))
lista = list(("Manzana","Platano","Cereza"))
print(lista)
print(type(lista))
tupla = tuple(("Manzana","Platano","Cereza"))
print(tupla)
print(type(tupla))
rango = range(6)
print(rango)
print(type(rango))
dictado =  dict(Nombre="Freddy",Edad=24)
print(dictado)
print(type(dictado))
conjunto = set(("Manzana","Platano","Cereza"))
print(conjunto)
print(type(conjunto))
FrutaFria = frozenset(("Manzana","Platano","Cereza"))
#Esta variable se llama FrutaFria proque es de tipo frozenset y todas son frutas
print(FrutaFria)
print(type(FrutaFria))
Booleano = bool(5)
print(Booleano)
print(type(Booleano))
bit=bytes(5)
print(bit)
print(type(bit))
arreglo = bytearray(5)
print(arreglo)
print(type(arreglo))
memoria = memoryview(bytes(5))
print(memoria)
print(type(memoria))







