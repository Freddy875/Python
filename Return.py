# Definir la función potencia
def potencia(base, exponente):
    return base ** exponente  # Calcula la potencia y la devuelve
---

# Definir la función para convertir USD a EUR
def usd_a_eur(dolares):
    return dolares * 0.90  # Conversión a euros

# Crear la variable con un monto en dólares
dolares = 100  # Puedes cambiar este valor

# Calcular el monto en euros
euros = usd_a_eur(dolares)

# Imprimir el resultado
print(f"{dolares} USD equivalen a {euros} EUR")

---

# Definir la función para invertir una palabra y convertirla a mayúsculas
def invertir_palabra(palabra):
    return palabra[::-1].upper()  # Invierte la palabra y la convierte en mayúsculas

# Crear una variable con una palabra
palabra = "anita lava la tina"  # Puedes cambiarla por cualquier otra

# Llamar a la función y obtener el resultado
resultado = invertir_palabra(palabra)

# Imprimir el resultado
print(resultado)
