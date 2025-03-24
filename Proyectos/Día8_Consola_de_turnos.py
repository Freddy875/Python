from numeros import turno_perfumeria, turno_farmacia, turno_cosmetica, mensaje_turno

# Generadores inicializados
gen_perfumeria = turno_perfumeria()
gen_farmacia = turno_farmacia()
gen_cosmetica = turno_cosmetica()

# Funciones decoradas
@mensaje_turno
def pedir_turno_perfumeria():
    return next(gen_perfumeria)

@mensaje_turno
def pedir_turno_farmacia():
    return next(gen_farmacia)

@mensaje_turno
def pedir_turno_cosmetica():
    return next(gen_cosmetica)

# Programa principal
def main():
    while True:
        print("\n¿A qué área desea dirigirse?")
        print("1. Perfumería")
        print("2. Farmacia")
        print("3. Cosmética")
        opcion = input("Ingrese el número de su elección: ")

        if opcion == "1":
            pedir_turno_perfumeria()
        elif opcion == "2":
            pedir_turno_farmacia()
        elif opcion == "3":
            pedir_turno_cosmetica()
        else:
            print("Opción no válida.")

        continuar = input("¿Desea sacar otro turno? (s/n): ").lower()
        if continuar != "s":
            print("Gracias por utilizar el sistema de turnos. ¡Hasta pronto!")
            break

if __name__ == "__main__":
    main()
