'''
Python permite asignar multiples 
variables en un linea
'''
x,y,z = "Naranja", "Manzana" , "Cereza"
print(x)
print(y)
print(z)

'''
Puede asignar el mismo valor a multiples variables
en una linea
'''
x = y = z = "Naranja"

print(x)
print(y)
print(z)

print("Desempaquetar una coleccion")
'''
Si tiene una coleccion de valores en una lista, tupla,etc
Python le permite extraer los valores de las variables
A esto se le llama desembalaje 
'''

frutas = ["Manzana","Platano","Cereza"]
x,y,z = frutas
print(x)
print(y)
print(z)

