'''
Para insertar caracteres que son ilegales
en una cadena usamos un caracter de escape

'''
texto = "Somos los asi llamados \"Vikingos\" del norte"
print(texto)

texto = 'It\'s alright'
print(texto)

texto = "This will insert one \\ (backslash)."
print(texto)

#Salto de linea o Salto de Fe (Assasins Creed) o Spiderman: Into the Spider-Verse
texto = "Hola \n Mundo"
print(texto)

texto = "Hola \rMundo"
print(texto)

texto = "Hola \tMundo"
print(texto + "\n")

#Este ejmplo borra un caracter (bakcspace)
#texto = "Hola \bMundo"
#print(texto)

#Una barra invertida (backslash) seguida de 3 enteros dara como resultado un valor octal 
print("octal")
texto = "\110\145\154\154\157"
print(texto +  "\n")

#Una barra invertida (backslash) seguida de una 'x' y un numero hexadecimal representa 
#un valor hexadecial:
print("hexadecimal")
texto = "\x48\x65\x6c\x6c\x6f"
print(texto)


