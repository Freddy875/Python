import random

def elegir_palabra():
    palabras = ["python", "programacion", "desarrollo", "computadora", "software"]
    return random.choice(palabras)

def mostrar_palabra_oculta(palabra, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

def jugar_ahorcado():
    palabra_secreta = elegir_palabra()
    letras_adivinadas = set()
    vidas = 6
    
    print("\nBienvenido al juego del Ahorcado!")
    print(mostrar_palabra_oculta(palabra_secreta, letras_adivinadas))
    
    while vidas > 0:
        letra = input("\nIngresa una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una sola letra válida.")
            continue
        
        if letra in letras_adivinadas:
            print("Ya intentaste con esa letra.")
            continue
        
        letras_adivinadas.add(letra)
        
        if letra in palabra_secreta:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            vidas -= 1
            print(f"Incorrecto. Te quedan {vidas} vidas.")
        
        estado_actual = mostrar_palabra_oculta(palabra_secreta, letras_adivinadas)
        print(estado_actual)
        
        if "_" not in estado_actual:
            print("\n¡Felicidades! Has adivinado la palabra.")
            break
    else:
        print(f"\nHas perdido. La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    jugar_ahorcado()
