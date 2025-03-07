# Definir la función que suma los cuadrados de los números recibidos
def suma_cuadrados(*numeros):
    return sum(num ** 2 for num in numeros)  # Calcula la suma de los cuadrados

# No invocamos la función, solo la definimos según la consigna

---
# Definir la función que suma los valores absolutos de los números recibidos
def suma_absolutos(*numeros):
    return sum(abs(num) for num in numeros)  # Calcula la suma de los valores absolutos

# No invocamos la función, solo la definimos según la consigna

---

# Definir la función que recibe un nombre y varios números
def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)  # Sumar los números recibidos
    return f"{nombre}, la suma de tus números es {suma_numeros}"

# No invocamos la función, solo la definimos según la consigna
