# Programa para generar un nombre creativo para una cerveza

# Preguntas al usuario
sabor = input("¿Cuál es tu sabor favorito en una cerveza? (Ejemplo: amargo, dulce, tostado) ")
animal = input("Menciona un animal que te parezca interesante o divertido: ")

# Generación del nombre de la cerveza
nombre_cerveza = f"\"{sabor.capitalize()} {animal.capitalize()}\""

# Impresión del resultado en dos líneas
print("\n¡Felicidades! El nombre de tu cerveza es:")
print(nombre_cerveza)
