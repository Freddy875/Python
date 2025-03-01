# Definir la palabra
palabra = "ordenador"

# Obtener el carácter en la quinta posición (índice 4, porque los índices comienzan en 0)
caracter = palabra[4]

# Mostrar el resultado
print(f"El carácter en la quinta posición es: '{caracter}'")

----

# Definir la frase
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

# Encontrar el índice de la primera aparición de "práctica"
indice = frase.find("práctica")

# Mostrar el resultado
print(f"El índice de la primera aparición de 'práctica' es: {indice}")

---

# Definir la frase
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

# Encontrar el índice de la primera aparición de "práctica"
indice = frase.find("práctica")

# Mostrar el resultado
print(f"El índice de la primera aparición de 'práctica' es: {indice}")

----

"""
Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
"""

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

print(frase.rindex("práctica"))  # Encuentra y muestra el índice de la última aparición de "práctica"

