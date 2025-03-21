import os
from pathlib import Path

# Ruta absoluta a la carpeta de recetas
BASE_DIR = Path("C:/Users/fer87/OneDrive/Documentos/Mis Proyectos/Curso Python/Proyectos/Día 6/Recetas")

def contar_recetas():
    contador = 0
    for carpeta, _, archivos in os.walk(BASE_DIR):
        for archivo in archivos:
            if archivo.endswith(".txt"):
                contador += 1
    return contador

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():
    print("📖 ADMINISTRADOR DE RECETAS 📖")
    print(f"📁 Ruta de recetas: {BASE_DIR}")
    print(f"📄 Total de recetas: {contar_recetas()}")
    print("\nOpciones:")
    print("1 - Leer receta")
    print("2 - Crear nueva receta")
    print("3 - Crear nueva categoría")
    print("4 - Eliminar receta")
    print("5 - Eliminar categoría")
    print("6 - Salir")

def listar_categorias():
    return [x for x in BASE_DIR.iterdir() if x.is_dir()]

def elegir_categoria():
    categorias = listar_categorias()
    if not categorias:
        print("No hay categorías.")
        return None
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat.name}")
    opcion = input("Selecciona una categoría: ")
    try:
        return categorias[int(opcion)-1]
    except:
        print("Selección inválida.")
        return None

def elegir_receta(categoria):
    recetas = [x for x in categoria.iterdir() if x.suffix == ".txt"]
    if not recetas:
        print("No hay recetas en esta categoría.")
        return None
    for i, receta in enumerate(recetas, 1):
        print(f"{i}. {receta.name}")
    opcion = input("Selecciona una receta: ")
    try:
        return recetas[int(opcion)-1]
    except:
        print("Selección inválida.")
        return None

def abrir_leer(archivo):
    with open(archivo, encoding="utf-8") as f:
        return f.read()

def leer_receta():
    categoria = elegir_categoria()
    if categoria:
        receta = elegir_receta(categoria)
        if receta:
            contenido = abrir_leer(receta)
            print(f"\n📄 Contenido de {receta.name}:\n")
            print(contenido)

def crear_receta():
    categoria = elegir_categoria()
    if categoria:
        nombre = input("Nombre de la receta (sin .txt): ") + ".txt"
        contenido = input("Contenido de la receta:\n")
        ruta = categoria / nombre
        if ruta.exists():
            print("Ya existe una receta con ese nombre.")
        else:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(contenido)
            print("Receta creada con éxito.")

def crear_categoria():
    nombre = input("Nombre de nueva categoría: ")
    nueva = BASE_DIR / nombre
    try:
        nueva.mkdir()
        print("Categoría creada con éxito.")
    except FileExistsError:
        print("La categoría ya existe.")

def eliminar_receta():
    categoria = elegir_categoria()
    if categoria:
        receta = elegir_receta(categoria)
        if receta:
            receta.unlink()
            print("Receta eliminada.")

def eliminar_categoria():
    categoria = elegir_categoria()
    if categoria:
        for archivo in categoria.iterdir():
            archivo.unlink()
        categoria.rmdir()
        print("Categoría eliminada.")

def iniciar_programa():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("\nElige una opción (1-6): ")

        if opcion == "1":
            leer_receta()
        elif opcion == "2":
            crear_receta()
        elif opcion == "3":
            crear_categoria()
        elif opcion == "4":
            eliminar_receta()
        elif opcion == "5":
            eliminar_categoria()
        elif opcion == "6":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción inválida.")
        
        input("\nPresiona Enter para continuar...")

# Punto de entrada
if __name__ == "__main__":
    if not BASE_DIR.exists():
        print(f"No se encontró la carpeta de recetas en:\n{BASE_DIR}")
    else:
        iniciar_programa()
