# Definir los sets
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}

# Unir los sets en uno solo
mi_set_3 = mi_set_1.union(mi_set_2)

# Mostrar el resultado
print(mi_set_3)

---

# Definir el set
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

# Eliminar un elemento al azar y almacenarlo en una variable
eliminado = sorteo.pop()

# Mostrar el elemento eliminado y el set actualizado
print(f"Elemento eliminado: {eliminado}")
print(f"Set actualizado: {sorteo}")
