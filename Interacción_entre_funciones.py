import random  # Importar la librería para generar números aleatorios

# Función para lanzar dos dados
def lanzar_dados():
    dado1 = random.randint(1, 6)  # Generar un número entre 1 y 6
    dado2 = random.randint(1, 6)  # Generar otro número entre 1 y 6
    return dado1, dado2  # Retorna los dos valores de los dados

# Función para evaluar la jugada según la suma de los dados
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2  # Calcular la suma de los dos dados
    
    # Evaluar el resultado según las condiciones dadas
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# No invocamos las funciones, solo las definimos según la consigna

----

# Función para reducir la lista eliminando duplicados y el valor más alto
def reducir_lista(lista):
    lista_unica = list(set(lista))  # Convertir a set para eliminar duplicados y luego volver a lista
    lista_unica.remove(max(lista_unica))  # Eliminar el número más alto
    return lista_unica  # Retornar la lista reducida

# Función para calcular el promedio de los valores de la lista reducida
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0  # Evitar división por cero si la lista está vacía

# Crear la lista de números
lista_numeros = [1, 2, 15, 7, 2]

# No invocamos las funciones, solo las definimos según la consigna

---

import random  # Importamos la librería para generar resultados aleatorios

# Función para lanzar la moneda y devolver "Cara" o "Cruz"
def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])  # Elige aleatoriamente entre "Cara" o "Cruz"

# Función para probar suerte con la lista de números
def probar_suerte(resultado_moneda, lista):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []  # Devuelve una lista vacía
    else:
        print("La lista fue salvada")
        return lista  # Devuelve la lista intacta

# Crear la lista de números
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# No se invocan las funciones, solo se definen según la consigna
