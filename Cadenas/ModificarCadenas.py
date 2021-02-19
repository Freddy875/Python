'''
Modificar Cadenas
'''
#Upper Case

a="Hola Mundo"
print(a.upper()) 

#Lower Case

b = "Hola Mundo"
print(b.lower())

#Remover espacioa en blanco
c = " ! Hola, Mundo "
print(c.strip())

#Remplazar cadenas
d = "Hola Mundo "
print(d.replace("H","J"))

'''
Cadena dividia
El metodo split devulve una lista donde el texto
entre separadores se convierte en los elementos 
de la lista
'''

e = "Hola, Mundo"
f = e.split(",")
print(f)
print(type(f))