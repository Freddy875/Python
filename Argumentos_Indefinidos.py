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

----

# Definir la función para contar los atributos pasados como argumentos nombrados
def cantidad_atributos(**kwargs):
    return len(kwargs)  # Devuelve la cantidad de claves en el diccionario kwargs

# Ejemplo de uso
print(cantidad_atributos(nombre="Juan", edad=30, ciudad="Madrid"))  # Salida: 3
print(cantidad_atributos(a=1, b=2))  # Salida: 2
print(cantidad_atributos())  # Salida: 0

----

# Definir la función que devuelve una lista con los valores de los atributos
def lista_atributos(**kwargs):
    return list(kwargs.values())  # Extrae los valores y los convierte en lista

# Ejemplo de uso
print(lista_atributos(nombre="Carlos", edad=25, ciudad="Madrid"))  
# Salida: ['Carlos', 25, 'Madrid']

print(lista_atributos(a=10, b=20, c=30))  
# Salida: [10, 20, 30]

print(lista_atributos())  
# Salida: []

---

# Definir la función para describir a una persona
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")  # Encabezado con el nombre
    for clave, valor in kwargs.items():  # Recorrer los argumentos nombrados
        print(f"{clave}: {valor}")  # Imprimir cada característica

# Ejemplo de uso
describir_persona("María", color_ojos="azules", color_pelo="rubio")







