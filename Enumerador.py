# Lista de nombres
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Loop con enumerate para obtener índice y nombre
for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

----

# String base
palabra = "Python"

# Crear la lista de tuplas con (índice, caracter)
lista_indices = list(enumerate(palabra))

# Imprimir la lista resultante
print(lista_indices)

---

# Lista de nombres
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Loop con enumerate para obtener índice y nombre
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):  # Verifica si el nombre empieza con "M"
        print(indice)

