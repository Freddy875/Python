class Personaje:
    def __init__(self, nombre, casa, edad, habilidad):
        self.nombre = nombre
        self.casa = casa
        self.edad = edad
        self.habilidad = habilidad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años, pertenezco a {self.casa} y mi habilidad es {self.habilidad}.")

# Crear un objeto a partir de la clase
harry_potter = Personaje("Harry Potter", "Gryffindor", 17, "magia defensiva")

# Usar el método del objeto
harry_potter.presentarse()

###

class Dinosaurio:
    def __init__(self, nombre, dieta, periodo, tamaño):
        self.nombre = nombre
        self.dieta = dieta  # carnívoro o herbívoro
        self.periodo = periodo  # período en el que vivió
        self.tamaño = tamaño  # en metros o una descripción

    def describir(self):
        print(f"{self.nombre.capitalize()} era un dinosaurio {self.dieta} del período {self.periodo}, y medía aproximadamente {self.tamaño}.")

# Crear las instancias
velociraptor = Dinosaurio("velociraptor", "carnívoro", "Cretácico", "2 metros")
tiranosaurio_rex = Dinosaurio("tiranosaurio rex", "carnívoro", "Cretácico", "12 metros")
braquiosaurio = Dinosaurio("braquiosaurio", "herbívoro", "Jurásico", "25 metros")

# Usar el método describir
velociraptor.describir()
tiranosaurio_rex.describir()
braquiosaurio.describir()
###
class PlataformaStreaming:
    def __init__(self, nombre, precio_mensual, catalogo, calidad_maxima):
        self.nombre = nombre
        self.precio_mensual = precio_mensual  # en dólares
        self.catalogo = catalogo  # número aproximado de títulos
        self.calidad_maxima = calidad_maxima  # como "HD", "Full HD", "4K"

    def mostrar_info(self):
        print(f"{self.nombre} ofrece alrededor de {self.catalogo} títulos, "
              f"cuesta ${self.precio_mensual} al mes y su calidad máxima es {self.calidad_maxima}.")

# Crear las instancias
netflix = PlataformaStreaming("Netflix", 15.99, 5000, "4K")
hbo_max = PlataformaStreaming("HBO Max", 14.99, 3000, "Full HD")
amazon_prime_video = PlataformaStreaming("Amazon Prime Video", 12.99, 4000, "4K")

# Mostrar información
netflix.mostrar_info()
hbo_max.mostrar_info()
amazon_prime_video.mostrar_info()

###
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

    def describir(self):
        print(f"La casa es de color {self.color} y tiene {self.cantidad_pisos} pisos.")

# Crear la instancia
casa_blanca = Casa("blanco", 4)

# Usar el método para describir la casa
casa_blanca.describir()
###

class Cubo:
    # Atributo de clase
    caras = 6

    def __init__(self, color):
        # Atributo de instancia
        self.color = color

    def describir(self):
        print(f"Este cubo es de color {self.color} y tiene {Cubo.caras} caras.")

# Crear la instancia
cubo_rojo = Cubo("rojo")

# Usar el método para describir el cubo
cubo_rojo.describir()
###
class Personaje:
    # Atributo de clase
    real = False

    def __init__(self, especie, magico, edad):
        # Atributos de instancia
        self.especie = especie
        self.magico = magico
        self.edad = edad

    def describir(self):
        tipo = "mágico" if self.magico else "no mágico"
        print(f"Este personaje es un {self.especie}, {tipo}, tiene {self.edad} años y es real: {Personaje.real}.")

# Crear la instancia
harry_potter = Personaje("Humano", True, 17)

# Usar el método para describir al personaje
harry_potter.describir()
###

class Perro:
    def ladrar(self):
        print("Guau!")

# Crear una instancia de Perro
mi_perro = Perro()

# Hacer que el perro ladre
mi_perro.ladrar()

###

class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

# Crear una instancia de Mago
merlin = Mago()

# Hacer que lance un hechizo
merlin.lanzar_hechizo()
###

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

# Crear una instancia de Alarma
mi_alarma = Alarma()

# Postergar la alarma
mi_alarma.postergar(10)
###

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

# Llamar al método estático sin necesidad de crear una instancia
Mascota.respirar()
###
class Jugador:
    # Atributo de clase
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print("¡El jugador ha sido revivido!")

# Comprobamos el estado inicial
print("¿Está vivo el jugador?", Jugador.vivo)

# Revivimos al jugador
Jugador.revivir()

# Comprobamos el nuevo estado
print("¿Está vivo el jugador?", Jugador.vivo)
###

class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
            print(f"¡Flecha lanzada! Flechas restantes: {self.cantidad_flechas}")
        else:
            print("¡No quedan flechas!")

# Crear una instancia con 3 flechas
legolas = Personaje(3)

# Lanzar flechas
legolas.lanzar_flecha()
legolas.lanzar_flecha()
legolas.lanzar_flecha()
legolas.lanzar_flecha()  # Sin flechas
###

# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Clase derivada
class Alumno(Persona):
    pass

# Crear una instancia de Alumno
alumno1 = Alumno("Ana", 20)

# Mostrar los atributos heredados
print(f"Nombre: {alumno1.nombre}, Edad: {alumno1.edad}")
###


# Clase base
class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

# Clase derivada
class Perro(Mascota):
    pass

# Crear una instancia de Perro
mi_perro = Perro(5, "Fido", 4)

# Mostrar los atributos heredados
print(f"Nombre: {mi_perro.nombre}, Edad: {mi_perro.edad}, Patas: {mi_perro.cantidad_patas}")

###

# Clase base
class Vehiculo:
    def acelerar(self):
        pass

    def frenar(self):
        pass

# Clase derivada
class Automovil(Vehiculo):
    pass

# Crear una instancia de Automovil
mi_auto = Automovil()

# Llamar a los métodos heredados (aunque no hacen nada aún)
mi_auto.acelerar()
mi_auto.frenar()
###


class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")

# Herencia múltiple: primero Padre, luego Madre
class Hija(Madre, Padre):
    pass

# Crear una instancia
hija = Hija()

# Probar los métodos heredados
hija.reir()       # De Padre
hija.trabajar()   # De Madre (porque aparece después en la herencia)

###

class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Pone huevos como un ave...")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nada como un pez...")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Camina como un mamífero...")
    def amamantar(self):
        print("Amamanta a sus crías como un mamífero...")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    def quien_soy(self):
        print("¿Quién soy?")
        self.poner_huevos()
        self.nadar()
        self.caminar()
        self.amamantar()
        print(f"Tengo pico: {self.tiene_pico}")
        print(f"¿Soy vertebrado? {self.vertebrado}")
        print(f"¿Soy venenoso? {self.venenoso}")
        print("¡Soy un ornitorrinco!")

# Jugar a adivinar
animal_misterioso = Ornitorrinco()
animal_misterioso.quien_soy()

###

class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"

class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"

# Prueba
hijo = Hijo()
print(hijo.color_ojos)          # Heredado del padre
print(hijo.reir())              # Heredado del padre
print(hijo.hobby())             # Método sobrescrito

###
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

# Iteramos y mostramos su longitud
for obj in [palabra, lista, tupla]:
    print(len(obj))

###

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

# Crear instancias de cada personaje
arquero = Arquero()
mago = Mago()
samurai = Samurai()

# Crear lista en el orden deseado
personajes = [arquero, mago, samurai]

# Iterar y ejecutar ataque de cada personaje
for personaje in personajes:
    personaje.atacar()

###

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

# Función polimórfica
def personaje_defender(personaje):
    personaje.defender()

# Crear instancias
mago = Mago()
arquero = Arquero()
samurai = Samurai()

# Probar la función con cada personaje
personaje_defender(mago)
personaje_defender(arquero)
personaje_defender(samurai)
###

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

###

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas

###


class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")
