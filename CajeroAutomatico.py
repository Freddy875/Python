'''
Simular un cajero automático con un saldo inicial de $1000.00
Y tendra el siguiente menú de opciones:

1. Ingresar dinero a la cuenta
2. Retirar dinero de la cuenta 
3. Mostrar dinero disponible 
4. Salir

'''
fSaldo = 1000.00

print("Bienvenido al cajero automatico",
"\nMENU: ",
"\n1. Ingresar dinero a la cuenta"
"\n2. Retirar dinero de la cuenta"
"\n3. Mostrar dinero disponible"
"\n4. Salir"
)

iOpcion = int(input("Ingresa una opcion del menu: "))

if iOpcion == 1:

    print("1. Ingresar dinero a la cuenta")

    fDeposito = float(input("\n¿Cuanto dinero deseas ingresar?"))

    fSaldo += fDeposito

    print(f"Operacion exitosas: ",
    f"\nAhora cuentas con ${fSaldo:.2f} en tu cuenta")
elif iOpcion == 2:

    print("2. Retirar dinero de la cuenta")

    fRetiro = float(input("\n¿Cuanto dinero deseas retirar?"))

    if fRetiro > fSaldo:
        print("ERROR",  
        "\nSaldo insuficiente")
    else:
        fSaldo -= fRetiro
        print(f"Operacion exitosas: ",
        f"\nAhora cuentas con ${fSaldo:.2f} en tu cuenta")

elif iOpcion == 3: 

    print("3. Mostrar dinero disponible")

    print(f"\nOperacion exitosas: ",
    f"\nAhora cuentas con ${fSaldo:.2f} en tu cuenta")
elif iOpcion == 4:
    print("Gracias vuelva pronto")
else:
    print("Opcion NO Valida ")