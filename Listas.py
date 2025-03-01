# Definir una lista con distintos tipos de datos
mi_lista = ["Python", 42, True, 3.14, "Lista mixta"]

# Mostrar la lista
print(mi_lista)

---

# Lista original
medios_transporte = ["avión", "auto", "barco", "bicicleta"]

# Agregar "motocicleta" a la lista
medios_transporte.append("motocicleta")

# Mostrar la lista actualizada
print(medios_transporte)

---

# Definir el diccionario
mi_dict = {
    "valores_1": {"v1": 3, "v2": 6},
    "puntos": {"points1": 9, "points2": [10, 300, 15]}
}

# Obtener el segundo elemento de la lista 'points2'
segundo_item = mi_dict["puntos"]["points2"][1]

# Imprimir el resultado
print(segundo_item)

---

# Diccionario original
mi_dic = {"nombre": "Karen", "apellido": "Jurgens", "edad": 35, "ocupacion": "Periodista"}

# Actualizar valores existentes
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"

# Agregar una nueva clave "pais"
mi_dic["pais"] = "Colombia"

# Mostrar el diccionario actualizado
print(mi_dic)
