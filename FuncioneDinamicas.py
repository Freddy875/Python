# Definir la función que verifica si todos los números son positivos
def todos_positivos(lista):
    return all(num > 0 for num in lista)  # all() devuelve True si todos los valores cumplen la condición

# Crear una lista con valores positivos y negativos
lista_numeros = [10, 5, 8, -3, 7, 12]  # Contiene un número negativo

---

# Definir la función que suma los números dentro del rango permitido
def suma_menores(lista):
    return sum(num for num in lista if 0 < num < 1000)  # Suma solo los valores dentro del rango

# Crear la lista de números
lista_numeros = [10, 500, 1200, -5, 750, 999, 1500, 0]

# No se invoca la función, solo se define según la consigna
