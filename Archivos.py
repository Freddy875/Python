archivo = open("texto.txt")
print(archivo.read())

with open("texto.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())  # Se cierra automáticamente después de salir del bloque `with`
