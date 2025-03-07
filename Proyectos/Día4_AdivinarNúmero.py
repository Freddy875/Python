import random

# Pedir el nombre del usuario
nombre = input("¡Hola! ¿Cuál es tu nombre? ")

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

print(f"Bueno, {nombre}, he pensado un número entre 1 y 100. Tienes solo ocho intentos para adivinar cuál es.")

# Inicializar intentos
intentos = 0
max_intentos = 8

# Bucle para los intentos
while intentos < max_intentos:
    try:
        # Pedir al usuario que ingrese un número
        numero_usuario = int(input("Introduce un número: "))
        
        # Verificar si está en el rango permitido
        if numero_usuario < 1 or numero_usuario > 100:
            print("Número fuera de rango. Debes elegir un número entre 1 y 100.")
            continue  # No cuenta como intento válido
        
        intentos += 1  # Contar intento válido
        
        # Comparar el número ingresado con el número secreto
        if numero_usuario < numero_secreto:
            print("Incorrecto. El número es mayor.")
        elif numero_usuario > numero_secreto:
            print("Incorrecto. El número es menor.")
        else:
            print(f"¡Felicidades, {nombre}! Has adivinado el número en {intentos} intentos.")
            break  # Salir del bucle si acierta
        
    except ValueError:
        print("Por favor, ingresa un número válido.")  # Manejo de error si el usuario ingresa texto

# Si el usuario no adivinó en 8 intentos
if intentos == max_intentos and numero_usuario != numero_secreto:
    print(f"Lo siento, {nombre}. Se te han agotado los intentos. El número era {numero_secreto}. ¡Inténtalo de nuevo!")
