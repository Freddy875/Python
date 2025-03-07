# Programa para generar un nombre creativo para una cerveza

# Solicitar datos al usuario
animal = input("¿Cuál es tu animal favorito? ")
color = input("¿Cuál es tu color favorito? ")

# Generación del nombre de la cerveza
nombre_cerveza = f"\"{animal.capitalize()} {color.capitalize()}\""

# Impresión del resultado en dos líneas
print("\n¡Felicidades! El nombre de tu cerveza es:")
print(nombre_cerveza)
