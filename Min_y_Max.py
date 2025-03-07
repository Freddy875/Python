# Lista de números con diversas operaciones matemáticas
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

# Obtener el valor máximo de la lista
valor_maximo = max(lista_numeros)

# Imprimir el valor máximo
print(valor_maximo)

---

# Lista de números
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

# Calcular el rango (diferencia entre el máximo y el mínimo)
rango = max(lista_numeros) - min(lista_numeros)

# Imprimir el resultado
print(rango)

---

# Diccionario de edades
diccionario_edades = {
    "Carlos": 55, "María": 42, "Mabel": 78, "José": 44,
    "Lucas": 24, "Rocío": 35, "Sebastián": 19, "Catalina": 2, "Darío": 49
}

# Obtener la edad mínima
edad_minima = min(diccionario_edades.values())

# Obtener el último nombre en orden alfabético
ultimo_nombre = max(diccionario_edades.keys())

# Imprimir los resultados
print(f"Edad mínima: {edad_minima}")
print(f"Último nombre en orden alfabético: {ultimo_nombre}")
