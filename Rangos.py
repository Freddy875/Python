# Crear una lista con los números del 2500 al 2585
mi_lista = list(range(2500, 2586))  # El segundo valor en range es 2586 porque el límite superior no se incluye

# Imprimir la lista para verificar
print(mi_lista)

---

# Crear una lista con los múltiplos de 3 desde 3 hasta 300
mi_lista = list(range(3, 301, 3))

# Imprimir la lista para verificar
print(mi_lista)

---

# Inicializar la variable para la suma
suma_cuadrados = 0

# Loop a través del rango de 1 a 15
for num in range(1, 16):  # El segundo valor en range es 16 porque el límite superior no se incluye
    suma_cuadrados += num ** 2  # Elevar al cuadrado y sumar al acumulador

# Imprimir el resultado
print(suma_cuadrados)
