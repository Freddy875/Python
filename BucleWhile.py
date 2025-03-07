# Definir la variable inicial
numero = 10

# Loop While para contar de 10 a 0
while numero >= 0:
    print(numero)
    numero -= 1  # Restar 1 en cada iteración

---

# Definir la variable inicial
numero = 50

# Loop While para restar hasta 0
while numero >= 0:
    if numero % 5 == 0:  # Verificar si el número es divisible por 5
        print(numero)
    numero -= 1  # Restar 1 en cada iteración

---

# Lista de números
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

# Loop For para recorrer la lista
for numero in lista_numeros:
    if numero < 0:  # Verificar si el número es negativo
        break  # Interrumpir el loop
    print(numero)
