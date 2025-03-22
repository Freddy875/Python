# Clase base
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Clase derivada
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (f"Cliente: {self.nombre} {self.apellido}\n"
                f"Número de cuenta: {self.numero_cuenta}\n"
                f"Balance actual: ${self.balance:.2f}")

    def depositar(self, monto):
        self.balance += monto
        print(f"Depósito exitoso. Nuevo balance: ${self.balance:.2f}")

    def retirar(self, monto):
        if monto > self.balance:
            print("Fondos insuficientes.")
        else:
            self.balance -= monto
            print(f"Retiro exitoso. Nuevo balance: ${self.balance:.2f}")

# Función para crear un cliente
def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su número de cuenta: ")
    balance_inicial = float(input("Ingrese su balance inicial: "))
    return Cliente(nombre, apellido, numero_cuenta, balance_inicial)

# Función principal
def inicio():
    cliente = crear_cliente()
    print("\n¡Bienvenido!")
    print(cliente)

    while True:
        print("\n¿Qué desea hacer?")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar balance")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            cliente.depositar(monto)
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            cliente.retirar(monto)
        elif opcion == "3":
            print(cliente)
        elif opcion == "4":
            print("Gracias por usar el sistema bancario. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el programa
inicio()
