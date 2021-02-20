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

