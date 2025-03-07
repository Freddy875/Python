# Listas de capitales y países
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

# Loop con zip para emparejar cada país con su capital
for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}")

---

-- Tabla de países
CREATE TABLE Paises (
    id INTEGER PRIMARY KEY,
    nombre TEXT
);

-- Tabla de capitales con una relación con la tabla de países
CREATE TABLE Capitales (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    pais_id INTEGER,
    FOREIGN KEY (pais_id) REFERENCES Paises(id)
);

---

# Listas de marcas y productos
marcas = ["Nike", "Apple", "Samsung", "Adidas", "Sony"]
productos = ["Zapatillas", "iPhone", "Televisor", "Camiseta", "PlayStation"]

# Crear el objeto zip
mi_zip = zip(marcas, productos)

# Convertir a lista y mostrar los pares
print(list(mi_zip))


---

# Listas con las traducciones de los números
espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

# Crear el objeto zip y convertirlo en una lista
numeros = list(zip(espanol, portugues, ingles))

# Imprimir la lista de traducciones
print(numeros)
