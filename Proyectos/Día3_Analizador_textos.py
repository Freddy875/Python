# Programa analizador de texto

# Solicitar el texto al usuario
texto = input("Ingresa un texto: ").lower()  # Convertimos a minúsculas para análisis uniforme

# Solicitar tres letras al usuario
letras = []
for i in range(3):
    letra = input(f"Ingrese la letra {i+1}: ").lower()
    letras.append(letra)

# 1️⃣ Contar cuántas veces aparece cada letra en el texto
conteo_letras = {letra: texto.count(letra) for letra in letras}

# 2️⃣ Contar el número total de palabras en el texto
palabras = texto.split()
cantidad_palabras = len(palabras)

# 3️⃣ Obtener la primera y la última letra del texto
primera_letra = texto[0]
ultima_letra = texto[-1]

# 4️⃣ Invertir el texto
texto_invertido = " ".join(palabras[::-1])

# 5️⃣ Verificar si la palabra "Python" está en el texto
presencia_python = "sí" if "python" in texto else "no"

# Mostrar resultados
print("\n📊 Resultados del análisis:")
print("-" * 40)
print("1️⃣ Frecuencia de las letras ingresadas:")
for letra, cantidad in conteo_letras.items():
    print(f"   → La letra '{letra}' aparece {cantidad} veces.")
print(f"\n2️⃣ El texto tiene un total de {cantidad_palabras} palabras.")
print(f"3️⃣ La primera letra del texto es '{primera_letra}' y la última es '{ultima_letra}'.")
print(f"4️⃣ El texto invertido es:\n   {texto_invertido}")
print(f"5️⃣ ¿El texto menciona 'Python'? {presencia_python.capitalize()}.")
print("-" * 40)
