# Solicitar los números al usuario
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

# Estructura de control para comparar los valores
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

---

# Definir variables
edad = 16
tiene_licencia = False

# Estructura de control para verificar si puede conducir
if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")

---

# Definir variables
habla_ingles = True
sabe_python = False

# Estructura de control para evaluar al candidato
if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif not habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")
