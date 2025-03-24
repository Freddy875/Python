# Generadores para cada área
def turno_perfumeria():
    n = 1
    while True:
        yield f"P-{n}"
        n += 1

def turno_farmacia():
    n = 1
    while True:
        yield f"F-{n}"
        n += 1

def turno_cosmetica():
    n = 1
    while True:
        yield f"C-{n}"
        n += 1

# Decorador para mensaje estándar
def mensaje_turno(func):
    def wrapper():
        turno = func()
        print("Su turno es:")
        print(turno)
        print("Aguarde y será atendido.")
        return turno
    return wrapper
