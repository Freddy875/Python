archivo = open("texto.txt", "r")
print(archivo.read())
archivo.close()  # Cerrar el archivo después de leerlo

with open("texto.txt", "r") as archivo:
    print(archivo.read())  # Se cierra automáticamente después de salir del bloque `with`


# Abrir el archivo en modo lectura
archivo = open("texto2.txt", "r", encoding="utf-8")

# Leer e imprimir la primera línea
print(archivo.readline().strip())  # strip() elimina saltos de línea extra

# Cerrar el archivo
archivo.close()


mi_archivo = open("texto2.txt", "r", encoding="utf-8")

# Leer y descartar la primera línea
mi_archivo.readline()

# Leer e imprimir la segunda línea
print(mi_archivo.readline())

# Cerrar el archivo
mi_archivo.close()


# Abrir el archivo en modo escritura ("w") y reemplazar su contenido
mi_archivo = open("mi_archivo.txt", "w")
mi_archivo.write("Nuevo texto")  # Escribimos el nuevo contenido
mi_archivo.close()  # Cerramos el archivo

# Volver a abrir el archivo en modo lectura ("r") y mostrar su contenido
mi_archivo = open("mi_archivo.txt", "r")
print(mi_archivo.read())  # Leer e imprimir el contenido actualizado
mi_archivo.close()  # Cerrar el archivo

# Abrir el archivo en modo "a" (append) para añadir una línea al final
mi_archivo = open("mi_archivo2.txt", "a")
mi_archivo.write("\nNuevo inicio de sesión")  # Agregamos la nueva línea
mi_archivo.close()  # Cerramos el archivo

# Volver a abrir el archivo en modo lectura ("r") y mostrar su contenido
mi_archivo = open("mi_archivo2.txt", "r")
print(mi_archivo.read())  # Leer e imprimir el contenido actualizado
mi_archivo.close()  # Cerrar el archivo

# Lista con los valores a escribir
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# Abrir el archivo en modo "a" (append) para añadir la nueva información
with open("registro.txt", "a", encoding="utf-8") as archivo:
    archivo.write("\n")  # Añade un salto de línea antes de escribir los datos
    archivo.writelines("\t".join(registro_ultima_sesion) + "\n")  # Escribir con tabuladores y salto de línea

# Volver a abrir el archivo en modo lectura ("r") y mostrar su contenido
with open("registro.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())  # Leer e imprimir el contenido actualizado


from pathlib import Path

# Obtener el directorio base del usuario
ruta_base = Path.home()

# Imprimir la ruta base
print(ruta_base)

from pathlib import Path

# Crear la ruta relativa al archivo "practicas_path.py"
ruta = Path("Curso Python","Día 6","practicas_path.py")

# Imprimir la ruta relativa
print(ruta)


from pathlib import Path

# Obtener el directorio base del usuario (home)
ruta_base = Path.home()

# Crear la ruta absoluta al archivo "practicas_path.py"
ruta = ruta_base / "Curso Python" / "Día 6" / "practicas_path.py"

# Imprimir la ruta absoluta
print(ruta)

def abrir_leer(nombre_archivo):
        with open(nombre_archivo, "r") as archivo: 
            return archivo.read()  # Leer y devolver el contenido del archivo

# Ejemplo de uso:
contenido = abrir_leer("ejemplo.txt")
print(contenido)  # Imprime el contenido del archivo

def abrir_leer(nombre_archivo):
    #Abre un archivo y devuelve su contenido.
    with open(nombre_archivo, "r") as archivo:
        return archivo.read()  # Leer y devolver el contenido del archivo

# Ejemplo de uso:
contenido = abrir_leer("ejemplo.txt")
print(contenido)  # Imprime el contenido del archivo


def sobrescribir(archivo):
        archivo_sobrescribir = open(archivo, "w")  # Abrir en modo escritura
        archivo_sobrescribir.write("contenido eliminado")  # Sobrescribir el contenido
        archivo_sobrescribir.close()  # Cerrar el archivo
    
# Ejemplo de uso:
sobrescribir("mi_archivo.txt")  # Llamar la función para sobrescribir el archivo
    
# Verificar el contenido después de sobrescribir
archivo_verificar = open("mi_archivo.txt", "r")
print(archivo_verificar.read())  # Debería imprimir "contenido eliminado"
archivo_verificar.close()  # Cerrar el archivo después de leerlo

def registro_error(archivo):
    mi_archivo = open(archivo, "a")  # Abrir en modo append
    mi_archivo.write("\nse ha registrado un error de ejecución")  # Añadir mensaje en nueva línea
    mi_archivo.close()  # Cerrar el archivo

# Ejemplo de uso:
registro_error("log_errores.txt")  # Añade el mensaje al archivo

# Verificar el contenido después de añadir el error
mi_archivo_verificar = open("log_errores.txt", "r")
print(mi_archivo_verificar.read())  # Imprimir contenido actualizado
mi_archivo_verificar.close()  # Cerrar el archivo después de leerlo


def registro_error(archivo):
    with open(archivo, "a") as mi_archivo:
            mi_archivo.write("se ha registrado un error de ejecución")
