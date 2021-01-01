"""
Python no tienen ningun comando para declarar una varibale 
Una variable se crea en el momemento en que le asignan un valor
por primera vez
"""

x = 5
y = "Freddy"

print(x)
print(y)

"""
Las variables no necesitan ninguna declaracion de tipo en particular 
e incluso pueden cambiar de tipo una vez que se ha establecido 
"""
x = 4
print(x)
x = "Sally"
print(x)

#Fundiciones

print("Fundicion")
"""
Si desea especificar el tipo de datos de una variable, 
puede hacerlo con una conversion 
"""
x = str(3) # x sera '3'
y = int(3) # y sera 3
z = float(3) # z sera 3.0

print(x)
print(y)
print(z)

print("Obtener el tipo")
"""
Puede obtener el tipo de datos de una variable 
con la funcion type()
"""

x = 5
y = "John"
print(type(x))
print(type(y))

print("Cotizaciones simples o dobles")
"""
Las variables de cadena se puede declarar
utilizando comillas simples 
o comillas dobles
"""
print("Las variables de cadena se puede declarar"
    " utilizando comillas simples" 
    " o comillas dobles")

x = "Freddy"
print(x)
# Las comillas dobles son lo mismo que las comillas simples
print("Las comillas dobles son lo mismo que las comillas simples")
x = 'Freddy'
print(x)

print("Distingue entre mayusculas y minusculas")
"""
Los nombres de las variables distinguen
entre mayusculas y minusculas
"""
print("Los nombres de las variables distinguen"
        "entre mayusculas y minusculas")
a = 4
A = "Gaby"
#A no sobreescribe a
print(a)
print(A)


