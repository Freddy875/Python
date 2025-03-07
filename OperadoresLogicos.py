# Definir las variables
num1 = 36
num2 = 72 / 2  # Esto da 36
num3 = 48

# Verificar si num1 es mayor que num2 y menor que num3
mi_bool = num1 > num2 and num1 < num3

# Imprimir el resultado
print(mi_bool)  # Esto imprimirá False

----

# Definir las variables
num1 = 36
num2 = 72 / 2  # Esto da 36
num3 = 48

# Verificar si num1 es mayor que num2 o menor que num3
mi_bool = num1 > num2 or num1 < num3

# Imprimir el resultado
print(mi_bool)  # Esto imprimirá True

---

# Definir la frase y las palabras
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

# Verificar si ambas palabras NO están en la frase
mi_bool = palabra1 not in frase and palabra2 not in frase

# Imprimir el resultado
print(mi_bool)  # Esto imprimirá True si ambas palabras no están en la frase
