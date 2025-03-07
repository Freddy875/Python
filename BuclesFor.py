# Lista de alumnos
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

# Loop para saludar a cada alumno
for alumno in alumnos_clase:
    print(f"Hola {alumno}")
--- 

# Lista de números
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

# Variable para almacenar la suma
suma_numeros = 0

# Loop para recorrer la lista y sumar los números
for numero in lista_numeros:
    suma_numeros += numero  # Sumar cada número al total

# Imprimir el resultado
print(suma_numeros)

---

# Lista de números
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

# Variables para almacenar las sumas
suma_pares = 0
suma_impares = 0

# Loop para recorrer la lista y clasificar los números
for num in lista_numeros:
    if num % 2 == 0:  # Verifica si el número es par
        suma_pares += num
    else:  # Si no es par, es impar
        suma_impares += num

# Imprimir los resultados
print(f"Suma de números pares: {suma_pares}")
print(f"Suma de números impares: {suma_impares}")
